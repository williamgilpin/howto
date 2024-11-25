# Using AMD POD

AMD POD Setup
+ Open an account by following directions on wiki https://cloud.wikis.utexas.edu/wiki/spaces/RCTFusers/pages/31976153/POD+Accounts 
+ AMD GPU servers docs https://cloud.wikis.utexas.edu/wiki/spaces/RCTFusers/pages/31976113/AMD+GPU+servers
+ AMD POD resources and access https://cloud.wikis.utexas.edu/wiki/spaces/RCTFusers/pages/31976509/POD+Resources+and+Access

AMD ROCm PyTorch Integration
+ PyTorch blogpost https://pytorch.org/blog/amd-extends-support-for-pt-ml/
+ ROCm docs for AMD Radeon GPUs https://rocm.docs.amd.com/projects/radeon/en/latest/
+ Installing ROCm for torch (NOTE: we don't need to do this) https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/3rd-party/pytorch-install.html
+ HIP (ROCm) semantics https://pytorch.org/docs/stable/notes/hip.html
+ AMD POD GPU and ROCM docs https://cloud.wikis.utexas.edu/wiki/spaces/RCTFusers/pages/31976113/AMD+GPU+servers

## Log in to your account

    ssh <YOUR_UT_EID>@amdgcomp01.ccbb.utexas.edu

Your login credentials should be the same as your UT EID login. There is also `amdgcomp01` and `amdgcomp02` and `amdgcomp03`. These are identical GPU servers with these architecture specs:
+ Dual 64-core EPYC 7V13 CPUs (128 cores total)
+ 512 GB RAM
+ 8 AMD Radeon Instinct MI-100 GPUs w/32GB onboard RAM each

## General guidelines and quotas

AMD POD uses a ZFS file system.

+ `$HOME` is your home directory, mounted at `/stor/home/<YOUR_UT_EID>`. You have 100GB of storage.
+ `$WORK` is your group's shared work directory, mounted at `/stor/work/<YOUR_GROUP_ALLOCATION>`. To see which groups you belong to, use the linux `groups` command in your shell. Disk quota varies depending on the group, but is typically in the multi-TB range.
+ `$SCRATCH` is your scratch space, used for temporary storage and compute output. Files not accessed within 30 days are typically deleted. This is mounted at `/stor/scratch/<YOUR_GROUP_ALLOCATION>`. Disk quota is typically in the multi-TB range.

You can check environment variables with the bash command `printenv`

$HOME and $WORK are backed up weekly to a spinning disk between Friday and Monday mornings, and these backups are not incremental. Once a year, the data on the backup server is archived to TACC's Ranch tape archive.

$HOME also gets weekly read-only snapshots (containing files that change, i.e. update or deletion) and these are stored in the `~/.zfs/snapshot` directory. Contact rctf-support@utexas.edu to remove snapshots if they exceed your disk space quota. Another option, for any directory that becomes too big, is to move it to your scratch space via rsync (or scp), and then create a symbolic link (symlink).

    mkdir -p /stor/scratch/<YOUR_GROUP_ALLOCATION>/<YOUR_UT_EID>/home_extra
    rsync -avrP <BIG_DIR_PATH> /stor/scratch/<YOUR_GROUP_ALLOCATION>/<YOUR_UT_EID>/home_extra/<BIG_DIR>/
    rm -rf <BIG_DIR_PATH>
    ln -sf /stor/scratch/<YOUR_GROUP_ALLOCATION>/<YOUR_UT_EID>/home_extra/<BIG_DIR>/ <BIG_DIR_PATH>

Large files should always be transferred directly to $WORK or $SCRATCH, instead of $HOME because a Home directory snapshot could be taken, which would take up your disk space. A convenient option is to create a symlinks in Home that link to Work and Scratch. More guidelines can be found in https://cloud.wikis.utexas.edu/wiki/spaces/RCTFusers/pages/31976509/POD+Resources+and+Access

## Running Jobs
The POD compute servers do not have a batch system! To run processes unattended, you should use command line utility **nohup** or terminal multiplexer tools **screen** or **tmux**. 

But before running, check the RAM usage with `free -g` or `top` or `htop` or `who` or `ps -u`. You can also change the priority of your job with `renice +15 -p <PID_NUMBER>` or `renice +15 -u 'whoami'` to set priority for all jobs under a user.

FOr multi-processing, you can check the number of available cores and hyperthreads. It is important to understand the difference between cores and hyperthreads.

    cat /proc/cpuinfo | grep -c 'core id'           # actually the number of hyperthreads!
    cat /proc/cpuinfo | grep 'siblings' | head -1   # the real number of physical cores

## Github SSH Keys
For Git version control (i.e. git clone, pull, push, etc) you want to use ssh keys. This is very straightforward, just follow this guide https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

Essentially, do `ssh-keygen -t ed25519 -C "your_email@example.com"` and then go to your `.ssh/` folder and copy the contents of the public key `id_ed25519.pub` (or whatever you decided to name it, a common choice is just `id_rsa.pub`) you just created, into your Github > Settings > SSH Keys box. Note that the corresponding private key should never be shared or copied elsewhere and has the same filename except without the `.pub` extension. 

If you have multiple keys or your system only searches for a specific key name (i.e. only looks for `id_rsa`), you may have to register your newly private key to your ssh-agent. Simply start the agent in the background with `eval "$(ssh-agent -s)"` and then do `ssh-add ~/.ssh/id_ed25519` and now your system will automatically recognize the new key.

## Conda Environment

In `$HOME` use wget to download the Miniconda 64 bit Linux installer into the folder (go to the Miniconda page, find the first Linux installer, and right click to copy the link address). 

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

Follow the Miniconda instructions to run the installer bash script. When asked for an install location, specify `$HOME` if you are not already installing from there.

Add your conda install to your path (NOTE: match the name with the folder created by the installer. It should be named "miniconda3" but could also be "miniconda")

    export PATH="~/miniconda3/bin:$PATH"

test that everything is working

    conda info --envs

You can activate, install packages, etc as you would for a local conda environment. Simply do `conda activate <YOUR_CONDA_ENV>` and then run your code as normal. It is possible that upon activating for the first time you may be asked to do `conda init`, close the shell, re-open, and log in again for the `.bashrc` file to be updated.

If you'd prefer that conda's base environment not be activated on startup, run the following command when conda is activated: `conda config --set auto_activate_base false`. You can undo this by running `conda init --reverse $SHELL`

Now, you can create an environment by following the conda docs https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment. Specifically, you recommend you first make sure you are not in the base conda environemnt (deactivate if necessary), and then do:

    conda create -n <YOUR_ENV_NAME> python=3.12 pip

This sets you up with the latest stable release of Python 3 AND your a brand new pip (Python package manager). *This conda environment's pip is isolated from the system-wide pip* so you can do `pip install` instead of `conda install` without affecting your system or other environments. 

NOTE: All installation should be done within a conda environment. There clear benefits from having an isolated environment and not messing with the system-wide installs.

## Using Pytorch with GPU on AMD POD
AMD uses ROCm, which is their open source version of CUDA (what NVIDIA uses for GPU acceleration). To see what's already installed on the AMD POD, check out `ls /opt`. You should see three ROCm installations: `rocm-5.1.3`, `rocm-5.2.3` and `rocm-5.7.2`. Choosing the correct version is essential when installing the compatible version of PyTorch

For example, say you want to install a Pytorch version "torch~=2.0". Although you could go to the pytorch page https://pytorch.org/get-started/locally/ and find the latest version, you should instead go to the previous versions https://pytorch.org/get-started/previous-versions/ and browse a version that is compatible with both my desired torch version and my rocm options. Upon searching "ROCM 5.7" you find exactly what you need:

    pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/rocm5.7

You can check the installationn using `pip list` which should display:

```
torch                    2.2.2+rocm5.7
torchaudio               2.2.2+rocm5.7
torchvision              0.17.2+rocm5.7
```

Note that PyTorch + ROCm cannot be installed with conda (it's not currently supported!), only with pip. But this shouldn't be an issue because, when you are within a conda environment with its own pip, you can/should use `pip install` for everything.

Now, it is very important that you set the correct environment path variables, to be able to talk to the AMD Radeon GPU. Making sure to use the correct ROCm version that matches your PyTorch installation, simply do:

    export ROCM_HOME=/opt/rocm-5.7.2
    export LD_LIBRARY_PATH="/opt/rocm-5.7.2/hip/lib:$LD_LIBRARY_PATH"

HIP is just ROCm's C++ dialect that converts CUDA applications into portable C++ code. Its interface is designed to reuse the CUDA inferface (and so the syntax should be largely the same) https://pytorch.org/docs/stable/notes/hip.html

You can check the AMD GPUs using `rocm-smi` in an analogous fashion to NVIDIA's `nvidia-smi` command. Also `rocminfo` prints CPU information and `dpkg -l | grep rocm` gives you a list of installed packages for ROCm.

To confirm your installation and hceck that PyTorch can talk to the GPU via ROCm, you can start a python interactive session, `import torch` and run `torch.cuda.is_available()` and `torch.version.hip`. This should return `True` and your torch installation's HIP version, which in our case is `'5.7.31921-d1770ee1b'`.

## Example: Running Chronos on AMD POD
Some problems: 
+ The speedups for torchdynamo mostly come with GPU Ampere (Nvidia A-series) or higher.
+ Tensorfloat (tf32) requires Ampere or newer GPU Arch. How to get the equivalent behavior for AMD Radeon GPUs?
+ Unresolved driver issues when running on multiple GPUs with `torchrun` (Elastic Launch)

## Using JAX with GPU on AMD POD

Jax is currently not supported on the AMD POD but this may change soon.

## VSCode Integration
You can open up a directory on AMD POD in VSCode just like you'd do it in TACC. Open Remote Connection, add new Host, make sure it shows up in `.ssh/config` list of known hosts, then log in and open your directory. You can go to `remote.SSH.remotePlatform` in settings to change the system type (i.e. to Linux) if need be (although this should be done either automatically or confirmed when you open the remote connection for the first time).