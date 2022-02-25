# example data-analysis project with snakemake

This example uses data published along the following publication:

Brochier, T., Zehl, L., Hao, Y., Duret, M., Sprenger, J., Denker, M., Grün, S. & Riehle, A. (2018). Massively parallel recordings in macaque motor cortex during an instructed delayed reach-to-grasp task, Scientific Data, 5, 180055. http://doi.org/10.1038/sdata.2018.55

## Learn more about snakemake

Please consult the following ressources to learn more about snakemake:

* first impression: https://snakemake.github.io/

* journal article: https://f1000research.com/articles/10-33/v2 

* comprehensive tutorial: https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html

## Check out the slides on this project

Find presentation slides and a heuristic Snakefile in the folder "/presentation"

## Run this workflow

### Linux (will be easiest as I set it up on linux and all software can be directly set up with conda via .yml file)

#### install miniconda

* https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

#### create conda env from yml-file

* run "conda env create -f snakemake_ephy_example.yml"

#### activate conda env

* run "conda activate snakemake_ephy_example"

#### add local python package via conda-develop

* run "conda-develop base-mypackage/"

#### run snakemake

* run "snakemake"

### Others (unfortunately, more basic instructions only, but I am happy to help you, ask me)

* install miniconda 
	* https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
* follow instructions to create conda environment with the following packages
	* conda-build, matplotlib, numpy, neo, quantities, scipy, snakemake
* activate the environment
* if possible, use conda-develop to install the local python package "base-mypackage"
	* run "conda-develop base-mypackage/"
	* you can alternatively install it manually
* execute workflow by running "snakemake"


