import neo
import quantities as pq
import numpy as np
from mypackage.functions import butter_bandpass_filter

# load data slice
reader = neo.io.BlackrockIO(filename=snakemake.input[0])
seg = reader.read_segment(time_slice=[float(snakemake.wildcards.tstart)*pq.s,float(snakemake.wildcards.tstop)*pq.s])
ansig = seg.analogsignals[0]

# metadata
fs = ansig.sampling_rate
n_channels = np.shape(ansig)[1]
unit = ansig.units

# filter with buttworth filter
filtered_ansig = ansig.copy()
for ch_idx in range(n_channels):
    filtered_ansig[:,ch_idx].magnitude[:,0] = butter_bandpass_filter(
        data=ansig[:,ch_idx].magnitude[:,0],lowcut=float(snakemake.wildcards.lowcut),highcut=float(snakemake.wildcards.highcut),fs=fs.magnitude
    ) * unit

# save data in numpy format
np.save(arr=filtered_ansig.times.magnitude, file=snakemake.output[0])
np.save(arr=filtered_ansig.magnitude, file=snakemake.output[1])
