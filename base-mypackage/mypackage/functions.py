import numpy as np
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def spike_thresholding(signal, times, threshold_std):
    # calculate standard deviation
    std = np.std(signal)
    # get location of voltages exceeding threshold in positive direction
    up_bool = signal > threshold_std * std
    up_times = times[up_bool]
    # get locations of voltages exceeding threshold in negative direction
    down_bool = signal < -threshold_std * std
    down_times = times[down_bool]

    return list(np.sort(np.concatenate([up_times, down_times])))
