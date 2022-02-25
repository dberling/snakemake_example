configfile: "config.yml"

rule all:
    input:
        expand(
            "results/hist_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}_{spike_threshold_std}.png",
            file_name=config['file_name'],
            tstart=config['tstart'], tstop=config['tstop'], 
            lowcut=config['lowcut'], highcut=config['highcut'], 
            spike_threshold_std=config['spike_threshold_std']
        ),
        expand(
            "results/signal_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}_{spike_threshold_std}.png",
            file_name=config['file_name'],
            tstart=config['tstart'], tstop=config['tstop'], 
            lowcut=config['lowcut'], highcut=config['highcut'], 
            spike_threshold_std=config['spike_threshold_std']
        )
        
rule plot_figures:
    input:
        "{file_name}.ns6",
        "data/filtered_signal_times_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}.npy",
        "data/filtered_signal_voltages_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}.npy",
        "data/spiketrains_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}_{spike_threshold_std}.npy",
        "data/spike_stats_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}_{spike_threshold_std}.npy"
    output:
        "results/signal_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}_{spike_threshold_std}.png",
        "results/hist_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}_{spike_threshold_std}.png"
    script:
        "scripts/plot.py"

rule analyze:
    input:
        "data/filtered_signal_times_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}.npy",
        "data/filtered_signal_voltages_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}.npy"
    output:
        "data/spiketrains_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}_{spike_threshold_std}.npy",
        "data/spike_stats_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}_{spike_threshold_std}.npy"
    script:
        "scripts/analyze.py"

rule preprocess:
    input:
        "{file_name}.ns6",
    output:
        "data/filtered_signal_times_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}.npy",
        "data/filtered_signal_voltages_{file_name}_{tstart}_{tstop}_{lowcut}_{highcut}.npy"
    script:
        "scripts/preprocess.py"

rule download_data:
    output:
        "{file_name}.ns6"
    params:
        link = lambda wildcards: config['download_link_dict'][wildcards.file_name]
    shell:
        "curl -L {params.link} > {output}"
