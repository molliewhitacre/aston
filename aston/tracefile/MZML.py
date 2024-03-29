import re
import zlib
import base64
from xml.etree import ElementTree as ET
import numpy as np
from aston.trace.Trace import AstonSeries
from aston.tracefile.TraceFile import ScanListFile
from aston.spectra.Scan import Scan


def t_to_min(x):
    """
    Convert XML 'xs: duration type' to decimal minutes, e.g.:
    t_to_min('PT1H2M30S') == 62.5
    """
    g = re.match('PT(?:(.*)H)?(?:(.*)M)?(?:(.*)S)?', x).groups()
    return sum(0 if g[i] is None else float(g[i]) * 60. ** (1 - i) \
                for i in range(3))


#class mzXML(TraceFile):
class mzXML(object):
    ext = 'MZXML'
    traces = ['#ms']

    ns = {'m': 'http://sashimi.sourceforge.net/schema_revision/mzXML_2.1'}

    @property
    def data(self):
        # get all the scans under the root node
        r = ET.parse(self.filename).getroot()
        s = r.findall('*//m:scan', namespaces=self.ns)

        for scn in s:
            #scn.get('peaksCount')
            # extract out the actual scan data
            pks = scn.find('m:peaks', namespaces=self.ns)
            dtype = {'32': '>f4', '64': '>f8'}.get(pks.get('precision'))
            d = np.frombuffer(base64.b64decode(pks.text), dtype)
            mz = d[::2]
            abn = d[1::2]

    def total_trace(self, twin=None):
        #TODO: use twin
        #TODO: only get the scans with totIonCurrent; if none found
        # calculate from the data

        r = ET.parse(self.filename).getroot()
        s = r.findall('*//m:scan', namespaces=self.ns)
        d = np.array([float(i.get('totIonCurrent')) for i in s])
        t = np.array([t_to_min(i.get('retentionTime')) for i in s])
        return AstonSeries(d, t, name='TIC')


class mzML(ScanListFile):
    ext = 'MZML'
    traces = ['#ms']

    ns = {'m': 'http://psi.hupo.org/ms/mzml'}

    def scans(self, twin=None):
        if twin is None:
            twin = (-np.inf, np.inf)
        r = ET.parse(self.filename).getroot()
        pgr = r.find('.//m:referenceableParamGroupList', namespaces=self.ns)

        spectra = r.findall('*//m:spectrum', namespaces=self.ns)
        for s in spectra:
            q = './/m:cvParam[@accession="MS:1000016"]'
            time_elem = s.find(q, namespaces=self.ns)
            if time_elem is None:
                continue
            time = time_elem.get('value')

            #FIXME: won't find these properties if a paramGroupRef exists
            for i in ['MS:1000514', 'MS:1000617', 'MS:1000786']:
                q = './/m:cvParam[@accession="' + i + '"]/..'
                x_elem = s.find(q, namespaces=self.ns)
                if x_elem is not None:
                    x = self.read_binary(x_elem, pgr)
                    break
            else:
                #check paramGroupRef
                q0 = './/m:referenceableParamGroupRef'
                bin_arrs = s.findall(q0 + '/..', namespaces=self.ns)
                for ba in bin_arrs:
                    ref = ba.find(q0, namespaces=self.ns).get('ref')
                    q = 'm:referenceableParamGroup[@id="' + ref + '"]'
                    pg = pgr.find(q, namespaces=self.ns)
                    q = './/m:cvParam[@accession="MS:1000514"]/..'
                    if pg.find(q, namespaces=self.ns) is not None:
                        x = self.read_binary(ba, pgr)
                        break
                    q = './/m:cvParam[@accession="MS:1000617"]/..'
                    if pg.find(q, namespaces=self.ns) is not None:
                        x = self.read_binary(ba, pgr)
                        break
                    q = './/m:cvParam[@accession="MS:1000786"]/..'
                    if pg.find(q, namespaces=self.ns) is not None:
                        x = self.read_binary(ba, pgr)
                        break
                else:
                    continue

            q = './/m:cvParam[@accession="MS:1000515"]/..'
            y_elem = s.find(q, namespaces=self.ns)
            if y_elem is not None:
                y = self.read_binary(y_elem, pgr)
            else:
                #check paramGroupRef
                q0 = './/m:referenceableParamGroupRef'
                bin_arrs = s.findall(q0 + '/..', namespaces=self.ns)
                for ba in bin_arrs:
                    ref = ba.find(q0, namespaces=self.ns).get('ref')
                    q = 'm:referenceableParamGroup[@id="' + ref + '"]'
                    pg = pgr.find(q, namespaces=self.ns)
                    q = './/m:cvParam[@accession="MS:1000515"]/..'
                    if pg.find(q, namespaces=self.ns) is not None:
                        y = self.read_binary(ba, pgr)
                        break
                else:
                    continue

            yield Scan(x, y, name=time)

    def read_binary(self, ba, param_groups=None):
        """
        ba - binaryDataArray XML node
        """
        if ba is None:
            return []

        pgr = ba.find('m:referenceableParamGroupRef', namespaces=self.ns)
        if pgr is not None and param_groups is not None:
            q = 'm:referenceableParamGroup[@id="' + pgr.get('ref') + '"]'
            pg = param_groups.find(q, namespaces=self.ns)
        else:
            pg = ba

        if pg.find('m:cvParam[@accession="MS:1000574"]', \
                   namespaces=self.ns) is not None:
            compress = True
        elif pg.find('m:cvParam[@accession="MS:1000576"]',\
                     namespaces=self.ns) is not None:
            compress = False
        else:
            #TODO: no info? should check the other record?
            pass

        if pg.find('m:cvParam[@accession="MS:1000521"]', \
                   namespaces=self.ns) is not None:
            dtype = 'f'
        elif pg.find('m:cvParam[@accession="MS:1000523"]',\
                     namespaces=self.ns) is not None:
            dtype = 'd'
        else:
            #TODO: no info? should check the other record?
            pass

        datatext = ba.find('m:binary', namespaces=self.ns).text
        if compress:
            rawdata = zlib.decompress(base64.b64decode(datatext))
        else:
            rawdata = base64.b64decode(datatext)
        return np.fromstring(rawdata, dtype=dtype)

    def total_trace(self, twin=None):
        r = ET.parse(self.filename).getroot()

        # get it from the chromatogram list
        c = r.find('.//m:cvParam[@accession="MS:1000235"]/..', \
                   namespaces=self.ns)
        if c is not None:
            q = './/m:cvParam[@accession="MS:1000595"]/..'
            index = self.read_binary(c.find(q, namespaces=self.ns))
            q = './/m:cvParam[@accession="MS:1000515"]/..'
            values = self.read_binary(c.find(q, namespaces=self.ns))
            return AstonSeries(values, index, name='tic')

        ## otherwise try to extract it from the individual records
        #spectra = r.findall('*//m:spectrum/', namespaces=self.ns)
        #for s in spectra:
        #    # TIC
        #    s.find('m:cvParam[@accession="MS:1000285"]', namespaces=self.ns)
        #    # time
        #    s.find('.//m:cvParam[@accession="MS:1000016"]', \
        #           namespaces=self.ns)

        #TODO: call parent function if no TIC found


def write_mzxml(filename, df, info=None, precision='f'):
    """
    Precision is either f or d.
    """
    for r in df.values:
        df.columns
        pass


def write_mzml(filename, df, info=None):
    r = ET.Element('mzML')

    c = ET.SubElement(r, 'cvList', {'count': '1'})
    cva = {'id': 'MS', 'fullName': 'Proteomics Standards Initiative Mass ' + \
           'Spectrometry Ontology', 'version': '1.18.2', \
           'URI': 'http://psidev.cvs.sourceforge.net/*checkout*/psidev/psi' + \
           '/psi-ms/mzML/controlledVocabulary/psi-ms.obo'}
    ET.SubElement(c, 'cv', cva)

    c = ET.SubElement(r, 'fileDescription')
    c = ET.SubElement(c, 'fileContent')
    acc = {'ms': ('MS:1000579', 'MS1 spectrum'), \
           'uv': ('MS:1000806', 'absorption spectrum')}
    #TODO: need to select which kind of spectrum this is
    ET.SubElement(c, 'cvParam', {'cvRef': 'MS', 'accession': acc[0], \
                                 'name': acc[1]})

    c = ET.SubElement(r, 'softwareList', {'count': '1'})
    #TODO: should use version in here
    c = ET.SubElement(c, 'software', {'id': 'Aston', 'version': ''})
    ET.SubElement(c, 'cvParam', {'cvRef': 'MS', 'accession': 'MS:1001457', \
                                 'name': 'data processing software'})

    c = ET.SubElement(r, 'instrumentConfigurationList', {'count': '1'})
    c = ET.SubElement(c, 'instrumentConfiguration', {'id': 'IC1'})
    ET.SubElement(c, 'cvParam', {'cvRef': 'MS', 'accession': 'MS:1000031', \
                                 'name': 'instrument model'})

    c = ET.SubElement(r, 'dataProcessingList', {'count': '1'})
    c = ET.SubElement(c, 'dataProcessing', {'id': 'DP1'})
    c = ET.SubElement(c, 'processingMethod', {'order': '1', \
                                              'softwareRef': 'Aston'})
    ET.SubElement(c, 'cvParam', {'cvRef': 'MS', 'accession': 'MS:1000544', \
                                 'name': 'Conversion to mzML'})

    #TODO: add startTimeStamp
    c = ET.SubElement(r, 'run', {'defaultInstrumentConfigurationRef': 'IC1', \
                                 'id': 'R1'})
    sl = ET.SubElement(c, 'spectrumList', {'count': len(df.index), \
                                           'defaultDataProcessingRef': 'DP1'})
    #TODO: write out each spectrum
