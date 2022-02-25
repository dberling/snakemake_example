import numpy as np
from mypackage.functions import spike_thresholding

# load filtered data
filtered_ansig_times = np.load(snakemake.input[0])
filtered_ansig = np.load(snakemake.input[1])

# metadata
n_channels = np.shape(filtered_ansig)[1]
# extract spikes
spiketrains = [spike_thresholding(
    signal=filtered_ansig[:,ch_idx], times=filtered_ansig_times, threshold_std=float(snakemake.wildcards.spike_threshold_std)
) for ch_idx in range(n_channels)]

# count n_spikes per channel
n_spikes = [len(spiketrains[ch_idx]) for ch_idx in range(n_channels)]

# save analysis data
np.save(arr=spiketrains, file=snakemake.output[0], allow_pickle=True)
np.save(arr=n_spikes, file=snakemake.output[1])
