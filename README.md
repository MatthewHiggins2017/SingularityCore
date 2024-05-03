# Singularity Core


## Introduction

**Singularity Core** is a python-based wrapper to manage a library of singularity containers which can be created and deployed from definition files (.def), as outlined in the Singularity Documentation (https://docs.sylabs.io/guides/3.8/user-guide/). An overview of the best pratices for using and building singularity containers can be found in the [(wiki)](https://github.com/MatthewHiggins2017/SingularityCore/wiki).

**When to Use:**
* If creating a pipeline which incoporates multiple software packages but they are incompatible in the same conda environment. 
* When you want reproducibility when deploying a given pipeline across multiple different machines regardless of the underlying operating system.

**Wiki**:
* [Introduction to Singularity](https://github.com/MatthewHiggins2017/SingularityCore/wiki/Intro)
* [Building containers from Scratch](https://github.com/MatthewHiggins2017/SingularityCore/wiki/BuildFromScratch)
* [Building containers from Conda](https://github.com/MatthewHiggins2017/SingularityCore/wiki/BuildFromConda)


**Features**:
* Ensure pipelines are robust and reproducible by deploying containers.
* Deploy only the containers you required with the **Install** command, saving time and space. 
* Add new containers to the library using the **Add** command. 


-----------------------------------------------------------------------


## Installation

**Dependencies:**
* [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)


```
# Clone Repo Using GitHub CLI
gh repo clone MatthewHiggins2017/SingularityCore

# Navigate Into Repo
cd ./SingularityCore

# Create Singularity Environment
conda env create -f SINGULARITY.yml -name SINGULARITY

# Activate Singularity Environment.
conda activate SINGULARITY

# Install SingularityCore python package
python setup.py install 

```

------------------------------------------------------------------------------


## Deploying Containers With Install Command

To deploy a Singularity container it first has to be built from a definition file (.def) which are located in the library. The resulting container will be a (.sif) file and be stored in a hidden directory at root as shown below:

```
# User Root
~/.SingularitySIFCore/

# Absolute Path
/home/matt_h/.SingularitySIFCore/

```

**Note** = This hidden directory is created upon running SingularityCore if it does not already exist.


The command options to create deploy singularity containers of interest on local machine as specified according to defintion files provided in the SingularityCore repo library are shown below:

```

# Deploy singularity containers as defined in alias list. 
SingularityCore Install --AliasList FLYE

# Deploy all singularity containers in library.
SingularityCore Install --All


```

-------------------------------------------------------------------------

## Adding Containers To SingularityCore Library

When you want to add a Singularity container to the library you can use the command below:

```
SingularityCore Add --DirectoryPath /path/to/directory/containing/definitionfile --UpdateGit
```

**Important Note** = The Singularity Container Alias will match the prefix of the definition file. For example if FLYE.def is provided, the container will subsequently be named FLYE.

Parameter Breakdown:

* The DirectoryPath parameter will point to a local directory which should contain the definition file (.def) for you instance and also any other files which are required to create the instance and pointed to via the (.def) file for example a (.YML) file if deploying from conda environment.

* The UpdateGit parameter will update the SingularityCore repositry on Github. Note, this will only be possible if you have read-write permission. 
