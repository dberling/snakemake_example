import matplotlib.pyplot as plt
import numpy as np
import neo
import quantities as pq

# load data
## raw data
reader = neo.io.BlackrockIO(filename=snakemake.input[0])
seg = reader.read_segment(
        time_slice=[float(snakemake.wildcards.tstart)*pq.s,float(snakemake.wildcards.tstop)*pq.s]
)
ansig = seg.analogsignals[0]
## metadata
fs = ansig.sampling_rate
n_channels = np.shape(ansig)[1]
## filtered data
filtered_ansig_times = np.load(snakemake.input[1])
filtered_ansig = np.load(snakemake.input[2])
## spikes
spiketrains = np.load(snakemake.input[3], allow_pickle=True)
## spike stats
n_spikes = np.load(snakemake.input[4])

# plot raw data and filtered data within times t1,t2
ch_idx = 0 # should be also set as config parameter of the snakemake workflow
fig, axs = plt.subplots(ncols=2, figsize=(10,5), sharey=True)
axs[0].set_title('raw data for channel %2i' %ch_idx)
axs[0].plot(ansig[:,ch_idx].times,ansig[:,ch_idx].magnitude)
axs[1].set_title('filtered data for channel %2i' %ch_idx)
axs[1].plot(filtered_ansig_times,filtered_ansig[:,ch_idx])
# plot spikes as vertical lines
[ax.axvline(t, color='tab:red') for t in spiketrains[ch_idx] for ax in axs]
# label axes
axs[0].set_ylabel('recorded voltage uV')
[ax.set_xlabel('time [s]') for ax in axs]
# slice time_axis
[ax.set_xlim(float(snakemake.wildcards.tstart),float(snakemake.wildcards.tstop)) for ax in axs]
fig.savefig(snakemake.output[0])

# plot spike statistics
plt.figure()
plt.bar(x=np.arange(n_channels), height=n_spikes)
plt.xlabel('channel index')
plt.ylabel('number of spikes recorded')
plt.text(s='threshold %2.1f x std(signal) \nrecording duration %2.3f s'%(float(snakemake.wildcards.spike_threshold_std), float(snakemake.wildcards.tstop)-float(snakemake.wildcards.tstart)),
         x=0.5,y=0.9,transform=plt.gca().transAxes)
plt.savefig(snakemake.output[1])

