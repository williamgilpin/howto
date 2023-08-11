# Using TACC cluster

Useful information

+ TACC getting started [guide](https://wikis.utexas.edu/display/CoreNGSTools/Getting+started+at+TACC)
+ TACC conda and advanced [guide](https://wikis.utexas.edu/display/bioiteam/Linux+and+stampede2+Setup+--+GVA2021#Linuxandstampede2SetupGVA2021-MovingbeyondthepreinstalledcommandsonTACC)
+ Run Jupyter in browser via [TACC Vis portal](https://vis.tacc.utexas.edu/).
+ Notes on getting started with Python and conda [here](https://www.wgilpin.com/cphy/labs/getting_started_with_python.html)
+ Notes on using SSH and configuring Lonestar6 [here](https://issm.ess.uci.edu/trac/issm/wiki/lonestar)

## Log in to your account

    ssh USERNAME@ls6.tacc.utexas.edu 

You will be prompted to enter your password and provide a two-factor authentication. Currently, you need to type in a physical six-digit code from your phone; you can't approve a push notification (as far as I'm aware).


## General guidelines and quotas

+ `$HOME` is your home directory on TACC. This has a strict storage limit of 10 GB, but it is backed up. This is not a suitable place for long-term storage of large files. I mainly just keep basic scripts there. Check your disk usage with `du -sh ./*/`
+ + This directory recieves a full backup every few months, and an incremental backup every few days. You can open a support ticket to retrieve files, if needed.

+ `$WORK` does not have the same storage limit, but it is also not backed up. For machine learning, I have found it necessary to install conda within `$WORK`, since environments can get pretty large

Most of the time you want to work in the `$WORK` folder. This is also the best place to install large programs, due to the file size limits on other partitions. 

    cd $WORK


## Submitting a job

Now submit your job

	sbatch FILENAME.sbatch

Check on your job status

	squeue -u USERNAME

# Using conda on Lonestar

Since conda is not installed by default, you cannot currently use `module load conda` as you would on Stampede

In your user folder, make a directory called `src` and then use wget to download the Miniconda 64 bit Linux installer into the folder (go to the Miniconda page, find the first Linux installer, and right click to copy the link address). 

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

Follow the Miniconda instructions to run the installer bash script. When asked for an install location, specify `$WORK`

Add your conda install to your path

    export PATH="~/miniconda/bin:$PATH"

test that everything is working

    conda info --envs

You can activate, install packages, etc as you would for a local conda environment. 

As of writing, automatically loading conda environments within batch scripts can be a bit challenging. Currently, the following lines work within a `.sbatch` file. See full sbatch template [here](#template)

    module load gcc
    source ~/work/miniconda3/etc/profile.d/conda.sh
    conda init bash
    conda activate ~/work/mambaforge/envs/dedalus
    python kolmo.py


# Using mamba on Lonestar6

Install from the command line. During installation, manually install mambaforge to $WORK instead of the top level

You will need to manually add the condaforge bin to your path

    export PATH="~/work/mambaforge/bin:$PATH"

Also try manually running init

    ~/work/mambaforge/condabin/mamba init

# Using PyTorch on Lonestar6

In a clean conda environment, install torch and torchvision

    conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c nvidia

To use a GPU, make sure that you load a matching version of CUDA in all of your `.sbatch` scripts

    module load cuda/12.0

# Using Jupyter notebooks on TACC

In a web browser, visit the [TACC Vis portal](https://vis.tacc.utexas.edu/).

Create a job with your desired resources and partition. Leave the "reservation" field blank.

# Using JAX with GPU on TACC

Make sure that you install in your environment a version of JAX that matches the version of CUDA that you are running. The available JAX versions are listed in the [JAX installation guide](https://github.com/google/jax#installation)

For example, installing CUDA 12 

    pip install --upgrade "jax[cuda12_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

Next, make sure that all of your `.sbatch` scripts load the matching CUDA version

    module load cuda/12.0

You can check that everything is working by opening a Python prompt and running

    import jax
    jax.devices()

A GPU should appear somewhere

# Using zsh shell on TACC

*Instructions by [Jeffrey Lai](https://github.com/jbial)*

Instructions for downloading zsh + oh-my-zsh on LS6:

First download zsh from source:

    wget -O zsh.tar.xz https://sourceforge.net/projects/zsh/files/latest/download
    mkdir zsh && unxz zsh.tar.xz && tar -xvf zsh.tar -C zsh --strip-components 1
    cd zsh

Compile it into the home directory:

    ./configure --prefix=$HOME
    make
    make install

Place the following lines at the bottom of `$HOME/.bashrc`

    rm -rf $HOME/.zcompdump*
    exec $HOME/bin/zsh -l

Restart the shell to run zsh (`reset`  or `zsh`). Then install oh-my-zsh:

    sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

Then place the following line at the top of the `$HOME/.zshrc file`

    export FPATH=$HOME/share/zsh/5.9/functions:$FPATH

Finally, restart the shell and enjoy the features of oh-my-zsh!

## Template for SLURM on TACC {template}

```
#!/bin/bash
# Job name:
#SBATCH --job-name=myjob
#
# Account to charge:
#SBATCH --account=PHY22025
#
# Pick partition to run on:
#SBATCH --partition=gpu-a100
#
# File where job progress and standard output is written
#SBATCH --output=myjob.out
#
# File where job errors are written
#SBATCH --error=myjob.err      
#
# Request only one node:
#SBATCH --nodes=1
#
# memory per node: (uses full node memory if set to zero)
#SBATCH --mem=0  
#
# number of tasks
#SBATCH --ntasks=1
#
# Processors per task:
#SBATCH --cpus-per-task=2
#
# Wall clock limit: HH:MM:SS. Max is 48 hours on most nodes
#SBATCH --time=05:30:00
#
## Command(s) to run
python scripts/my_program.py 
```

For this example, you can check standard out and errors while the job is in progress by running 

    cat myjob.err
    cat myjob.out

