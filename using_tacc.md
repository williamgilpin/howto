
Useful information

+ TACC getting started [guide](https://wikis.utexas.edu/display/CoreNGSTools/Getting+started+at+TACC)
+ TACC conda and advanced [guide](https://wikis.utexas.edu/display/bioiteam/Linux+and+stampede2+Setup+--+GVA2021#Linuxandstampede2SetupGVA2021-MovingbeyondthepreinstalledcommandsonTACC)
+ Run Jupyter in browser via [TACC Vis portal](https://vis.tacc.utexas.edu/).
+ Notes on getting started with Python and conda [here](https://www.wgilpin.com/cphy/labs/getting_started_with_python.html)
+ Notes on using SSH and configuring Lonestar6 [here](https://issm.ess.uci.edu/trac/issm/wiki/lonestar)

# General guidelines

+ $HOME is your home directory on TACC. This has a strict storage limit of 10 GB, but it is backed up. This is not a suitable place for long-term storage of large files. I mainly just keep basic scripts there. Check your disk usage with `du -sh ./*/`

+ $WORK does not have the same storage limit, but it is also not backed up. For machine learning, I have found it necessary to install conda within work, since environments can get pretty large

# Using conda on Lonestar

Since conda is not installed by default, you cannot currently use `module load conda` as you would on Stampede

In your user folder, make a directory called `src` and then use wget to download the Miniconda 64 bit Linux installer into the folder (go to the Miniconda page, find the first Linux installer, and right click to copy the link address). 

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

Follow the Miniconda instructions to run the installer bash script. When asked for an install location, specify $WORK

Add your conda install to your path

    export PATH="~/miniconda/bin:$PATH"

test that everything is working

    conda info --envs

You can activate, install packages, etc as you would for a local conda environment

# Using PyTorch on Lonestar6

In a clean conda environment, install torch and torchvision

    conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c nvidia



# Using Jupyter notebooks on TACC

In a web browser, visit the [TACC Vis portal](https://vis.tacc.utexas.edu/).

Create a job with your desired resources and partition. Leave the "reservation" field blank.

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

