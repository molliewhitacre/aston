from aston import Datafile
import os
import re
import struct
import time
import numpy as np
from xml.etree import ElementTree

class AgilentMWD(Datafile.Datafile):
    def __init__(self,*args,**kwargs):
        super(AgilentMWD,self).__init__(*args,**kwargs)
        #self.filename = os.path.split(self.filename)[0] + '/mwd.ch'

    def _cacheData(self):
        #Because the spectra are stored in several files in the same
        #directory, we need to loop through them and return them together.
        if self.data is not None: return
        
        self.ions = []
        dtraces = []
        foldname = os.path.dirname(self.rawdata)
        #if foldname == '': foldname = os.curdir
        for i in [os.path.join(foldname,i) for i in os.listdir(foldname)]:
            if i[-3:].upper() == '.CH':
                wv, dtrace = self._readIndFile(i)
                
                #generate the time points if this is the first trace
                if len(self.ions) == 0:
                    f = open(i,'rb')

                    f.seek(0x11A)
                    start_time = struct.unpack('>i',f.read(4))[0] / 60000.
                    #end_time 0x11E '>i'
                    f.close()
                    
                    #TODO: 0.4/60.0 should be obtained from the file???
                    dtraces.append(start_time + \
                                       np.arange(len(dtrace)) * (0.4/60.0))
                
                #add the wavelength and trace into the appropriate places
                self.ions.append(wv)
                dtraces.append(dtrace)
        self.data = np.array(dtraces).transpose()
                

    def _readIndFile(self, fname):
        f = open(fname,'rb')

        f.seek(0x254)
        sig_name = str(f.read(struct.unpack('>B',f.read(1))[0]))
        #wavelength the file was collected at
        wv = float(re.search("Sig=(\d+),(\d+)",sig_name).group(1))

        f.seek(0x284)
        del_ab = struct.unpack('>d',f.read(8))[0]

        data = np.array([])

        f.seek(0x401)
        loc = 0
        while True:
            rec_len = struct.unpack('>B',f.read(1))[0]
            if rec_len == 0: break
            data = np.append(data, np.empty(rec_len))
            for _ in range(rec_len):
                inp = struct.unpack('>h',f.read(2))[0]
                if inp == -32768:
                    inp = struct.unpack('>i',f.read(4))[0]
                    data[loc] = del_ab*inp
                elif loc == 0:
                    data[loc] = del_ab*inp
                else:
                    data[loc] = data[loc-1] + del_ab*inp
                loc += 1
            f.read(1) #this value is always 0x10?
        f.close()
        return wv, data

    def _updateInfoFromFile(self):
        d = {}
        #TODO: fix this so that it doesn't rely upon MWD1A.CH?
        f = open(self.rawdata,'rb')
        f.seek(0x18)
        d['name'] = f.read(struct.unpack('>B',f.read(1))[0]).decode()
        f.seek(0x94)
        d['r-opr'] = f.read(struct.unpack('>B',f.read(1))[0]).decode()
        f.seek(0xE4)
        d['m'] = f.read(struct.unpack('>B',f.read(1))[0]).decode()
        #try:
        f.seek(0xB2)
        d['r-date'] = f.read(struct.unpack('>B',f.read(1))[0]).decode()
        #except: pass #TODO: find out why this chokes
        f.seek(0x244)
        d['m-y-units'] = f.read(struct.unpack('>B',f.read(1))[0]).decode()
        f.seek(0x254)
        #TODO: replace signal name with reference_wavelength?
        d['signal name'] = f.read(struct.unpack('>B',f.read(1))[0]).decode()
        d['r-type'] = 'Sample'
        f.close()
        self.info.update(d)

class AgilentDAD(Datafile.Datafile):
#header data in DAD1.sd
#80 byte repetition
#offset = 0xA4, format = 'IIfIfffQIIdddd'
# 750 entries
#f.seek(0xA4); struct.unpack('<IddffIQIIdddd', f.read(80))

#time series in DAD1.sg
#all doubles, starts at 0x44
#750x 54 double entries
    def __init__(self,*args,**kwargs):
        super(AgilentDAD,self).__init__(*args,**kwargs)

    def _cacheData(self): 
        if self.data is not None: return
        
        fhead = open(self.rawdata[:-3]+'.sd','rb')
        fdata = open(self.rawdata[:-3]+'.sp','rb')

        fhead.seek(0x50)
        nscans = struct.unpack('Q',fhead.read(8))[0]
        fhead.seek(0xA4)

        self.ions = []
        for scn in range(nscans):
            t = struct.unpack('<IdddIQIIdddd', fhead.read(80))
            
            npts = t[7]
            if scn == 0:
                #TODO: this will fail if the wavelengths collected 
                #change through the run.
                self.data = np.zeros((nscans,npts+1))
                self.ions = [t[8] + x*t[3] for x in range(npts)]

            self.data[scn] = t[1]
            
            fdata.seek(t[5]+16)
            self.data[scn,1:] = \
                struct.unpack('<'+npts*'d',fdata.read(npts*8))

        fhead.close()
        fdata.close()

    def _updateInfoFromFile(self):
        d = {}
        tree = ElementTree.parse(os.path.join( \
                os.path.dirname(self.rawdata),'sample_info.xml'))
        for i in tree.iterfind('Field'):
            tagname = i.find('Name').text
            tagvalue = i.find('Value').text
            if tagname == 'Sample Name':
                d['name'] = tagvalue
            elif tagname == 'Sample Position':
                d['r-vial-pos'] = tagvalue
            elif tagname == 'Method':
                d['m'] = tagvalue.split('/')[-1]
        d['r-opr'] = ''
        d['r-date'] = time.ctime(os.path.getctime(self.rawdata))
        d['r-type'] = 'Sample'
        self.info.update(d)

class AgilentCSDAD(Datafile.Datafile):
    '''Interpreter for *.UV files from Agilent Chemstation'''
    def __init__(self,*args,**kwargs):
        super(AgilentCSDAD,self).__init__(*args,**kwargs)

    def _cacheData(self): 
        #TODO: the chromatograms this generates are not exactly the
        #same as the ones in the *.CH files. Maybe they need to be 0'd?
        f = open(self.rawdata,'rb')

        f.seek(0x116)
        nscans = struct.unpack('>i',f.read(4))[0]

        self.times = nscans*[0]
        self.data = nscans*[{}]
        npos = 0x202
        for i in range(nscans):
            f.seek(npos)
            npos += struct.unpack('<H',f.read(2))[0]
            self.times[i] = struct.unpack('<L',f.read(4))[0] / 60000.
            nm_srt = struct.unpack('<H',f.read(2))[0] / 20.
            nm_end = struct.unpack('<H',f.read(2))[0] / 20.
            nm_stp = struct.unpack('<H',f.read(2))[0] / 20.
            f.read(8)
            s = {}
            v = struct.unpack('<h',f.read(2))[0] / 2000.
            s[nm_srt] = v
            for j in range(1,int((nm_end-nm_srt)/nm_stp)):
                ov = struct.unpack('<h',f.read(2))[0]
                if ov == -32768:
                    v = struct.unpack('<i',f.read(4))[0] / 2000.
                else:
                    v += ov / 2000.
                s[nm_srt+j*nm_stp] = v
            self.data[i] = s

    def _updateInfoFromFile(self):
        d = {}
        f = open(self.rawdata,'rb')
        f.seek(0x18)
        d['name'] = f.read(struct.unpack('>B',f.read(1))[0]).decode().strip()
        f.seek(0x94)
        d['r-opr'] = f.read(struct.unpack('>B',f.read(1))[0]).decode()
        f.seek(0xE4)
        d['m'] = f.read(struct.unpack('>B',f.read(1))[0]).decode().strip()
        f.seek(0xB2)
        d['r-date'] = f.read(struct.unpack('>B',f.read(1))[0]).decode()
        f.seek(0x146)
        d['m-y-units'] = f.read(struct.unpack('>B',f.read(1))[0]).decode()
        f.seek(0xD0)
        d['r-inst'] = f.read(struct.unpack('>B',f.read(1))[0]).decode()
        #TODO: are the next values correct?
        f.seek(0xFE) 
        d['r-vial-pos'] = str(struct.unpack('>h',f.read(2))[0])
        f.seek(0xFE) 
        d['r-seq-num'] = str(struct.unpack('>h',f.read(2))[0])
        d['r-type'] = 'Sample'
        f.close()
        self.info.update(d)
