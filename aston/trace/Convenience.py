import numpy as np
from pandas import Series


def _apply_f(f, s, s2):
    """
    Convenience function for all of the math stuff.
    """
    if type(s2) == int or type(s2) == float:
        # s2 is a number, so make an array of the same size
        # with just that number in it
        d = s2 * np.ones(s.index.shape)
    elif s2 is None:
        d = None
    elif all(s2.index == s.index):
        # same times, so can do math directly
        d = s2.data
    else:
        # retime s2 so it matches up with s
        d = _retime(s2, s.index)
        # TODO: needs to be smarter with retiming, so
        #nonoverlapping times don't break this

    new_data = np.apply_along_axis(f, 0, s.values, d)
    return Series(new_data, s.index, s.columns)


def add(s1, s2):
    return _apply_f(lambda x, y: x + y, s1, s2)


def sub(s1, s2):
    return _apply_f(lambda x, y: x - y, s1, s2)


def mul(s1, s2):
    return _apply_f(lambda x, y: x * y, s1, s2)


def div(s1, s2):
    return _apply_f(lambda x, y: x / y, s1, s2)


#def and(s1, s2):
#    pass


def _retime(s, new_times, fill=0.0):
    from scipy.interpolate import interp1d
    if new_times.shape == s.index.shape:
        if np.all(np.equal(new_times, s.index)):
            return s
    f = lambda d: interp1d(s.index, d, \
        bounds_error=False, fill_value=fill)(new_times)
    return np.apply_along_axis(f, 0, s.values)


def retime(s, new_times):
    return Series(_retime(s), new_times, name=s.name)


def adjust_time(s, offset=0.0, scale=1.0):
    adj_s = s.copy()
    adj_s.index = adj_s.index * scale + offset
    return adj_s


def twin(s, st_t, en_t):
    if twin is None:
        return s

    if st_t is None:
        st_idx = 0
    else:
        st_idx = (np.abs(s.index - st_t)).arg_min()

    if en_t is None:
        en_idx = -1
    else:
        en_idx = (np.abs(s.index - en_t)).arg_min()

    return s[st_idx:en_idx]


def scan(df, time, to_time=None):
    """
    Returns the spectrum from a specific time.
    """
    #TODO: option for averaging spectra instead of summing?
    idx = (np.abs(df.index - time)).argmin()

    if to_time is None:
        # only take the spectra at the nearest time
        mz_abn = df.values[idx, :].copy()
    else:
        # sum up all the spectra over a range
        en_idx = (np.abs(df.index - to_time)).argmin()
        idx, en_idx = min(idx, en_idx), max(idx, en_idx)
        mz_abn = df.values[idx:en_idx + 1, :].copy().sum(axis=0)
    return np.vstack([df.columns, mz_abn])


def as_2d(df):
    """
    Returns two matrices, one of the data and the other of
    the times and trace corresponding to that data.

    Useful for making two-dimensional "heat" plots.
    """
    ions = df.columns
    ext = (df.index[0], df.index[-1], min(ions), max(ions))
    grid = df.values[:, np.argsort(df.columns)].transpose()
    return ext, grid


def as_text(s, width=80, height=20):
    raise NotImplementedError
    #break s.index into width chunks
    #find max and min of each chunk along with start and stop?


def as_sound(df, speed=60, cutoff=50):
    import scipy.io.wavfile
    import scipy.signal

    # make a 1d array for the sound
    to_t = lambda t: (t - df.index[0]) / speed
    wav_len = int(to_t(df.index[-1]) * 60 * 44100)
    wav = np.zeros(wav_len)

    # create an artificial array to interpolate times out of
    tmask = np.linspace(0, 1, df.shape[0])

    # come up with a mapping from mz to tone
    min_hz, max_hz = 50, 1000
    min_mz, max_mz = min(df.columns), max(df.columns)

    def mz_to_wv(mz):
        """
        Maps a wavelength/mz to a tone.
        """
        try:
            mz = float(mz)
        except:
            return 100
        wv = (mz * (max_hz - min_hz) - max_hz * min_mz + min_hz * max_mz) \
                / (max_mz - min_mz)
        return int(44100 / wv)

    # go through each trace and map it into the sound array
    for i, mz in enumerate(df.columns):
        if float(mz) < cutoff:
            # clip out mz/wv below a certain threshold
            # handy if data has low level noise
            continue
        print(str(i) + '/' + str(df.shape[1]))
        inter_x = np.linspace(0, 1, wav[::mz_to_wv(mz)].shape[0])
        wav[::mz_to_wv(mz)] += np.interp(inter_x, tmask, df.values[:, i])

    # scale the new array and write it out
    scaled = wav / np.max(np.abs(wav))
    scaled = scipy.signal.fftconvolve(scaled, np.ones(5) / 5, mode='same')
    scaled = np.int16(scaled * 32767)
    scipy.io.wavfile.write('test.wav', 44100, scaled)


def as_colors(dfs):
    """
    Given a dataframe containing UV-Vis data, return an array
    of RGB values corresponding to how the UV-Vis run would look.
    """
    gaussian = lambda wvs, x, w: np.exp(-0.5 * ((wvs - x) / w) ** 2)
    colors = []

    #from http://www.brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html
    xyz_rgb = [[3.2404542, -1.5371385, -0.4985314],
               [-0.9692660, 1.8760108, 0.0415560],
               [0.0556434, -0.2040259, 1.0572252]]
    xyz_rgb = np.array(xyz_rgb)

    for df in dfs:
        wvs = df.columns.values.astype(float)

        # set up an array modelling visual response to
        # a full spectrum
        #TODO: use http://www.ppsloan.org/publications/XYZJCGT.pdf
        vis_filt = np.zeros((3, len(wvs)))
        vis_filt[0] = 1.065 * gaussian(wvs, 595.8, 33.33) \
                    + 0.366 * gaussian(wvs, 446.8, 19.44)
        vis_filt[1] = 1.014 * gaussian(np.log(wvs), np.log(556.3), 0.075)
        vis_filt[2] = 1.839 * gaussian(np.log(wvs), np.log(449.8), 0.051)

        #from aston.peaks.PeakModels import gaussian
        #vis_filt[0] = gaussian(wvs, w=40, x=575)  # red
        #vis_filt[1] = gaussian(wvs, w=40, x=535)  # green
        #vis_filt[2] = gaussian(wvs, w=40, x=445)  # blue

        # multiply response matrix by data to get list of colors
        ab = df.values.copy()
        #trans = 10 ** (-ab)
        xyz = np.dot(ab, vis_filt.T)
        rgb = np.dot(xyz_rgb, xyz.T).T
        colors.append(rgb)

    # normalize and invert data
    #mincolor = min(np.min(c) for c in colors)
    maxcolor = max(np.max(c) for c in colors)

    for i in range(len(colors)):
        colors[i][colors[i] < 0] = 0
        #colors[i][colors[i] > 1] = 1
        #colors[i] -= mincolor
        colors[i] /= maxcolor #- mincolor
        colors[i] = 1 - np.abs(colors[i])

    return colors


def color_strips(folder, fs, width=10, twin=None, names=None, norm_all=True):
    import os.path as op
    from matplotlib.colors import ListedColormap
    import matplotlib.pyplot as plt
    from aston.tracefile.Common import TraceFile

    dfs = []
    if norm_all:
        for f in fs:
            df = TraceFile(op.join(folder, f)).data
            if twin is not None:
                df = df.select(lambda t: t >= twin[0] and t < twin[1])
            dfs.append(df)
        colors = as_colors(dfs)
    else:
        colors = []
        for f in fs:
            df = TraceFile(op.join(folder, f)).data
            if twin is not None:
                df = df.select(lambda t: t >= twin[0] and t < twin[1])
            colors.append(as_colors([df])[0])

    for i, c in enumerate(colors):
        color_mask = np.meshgrid(0, np.arange(c.shape[0], 0, -1) - 1)[1]
        ax = plt.subplot(1, len(colors), i + 1)
        ax.imshow(color_mask, cmap=ListedColormap(c), \
                  extent=(0, width, df.index[0], df.index[-1]))
        ax.xaxis.set_ticks([])
        if i != 0:
            ax.yaxis.set_ticks([])
        else:
            ax.set_ylabel('Retention Time (min)')
        if names is not None:
            ax.set_xlabel(names[i])
    plt.show()


def dump(df):
    pass


def load(df_str):
    pass
