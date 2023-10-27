# Using slurm to submit and schedule jobs

## Logging in

Log into your HPC cluster using `ssh` with your Terminal

    ssh USERNAME@CLUSTERNAME

## Interactive session

For Terminal-level operations, like file management, conda env setup, writing bash scripts, etc. it is better not to use the so-called "login nodes," which are the nodes that you are using when you first SSH into the cluster. Instead, you should start what's known as an "interactive session" on a compute node. 

Depending on your cluster's configuration, this may be done with the `srun` command. 

    srun --pty bash

However, some clusters have aliases for this command, such as `idev` on TACC clusters. 

    idev

or `sdev` on the Stanford Sherlock cluster

    sdev

These interactive jobs typically have a standard length and amount of compute associated with them. You can usually modify the default by adding an appropriate dotfile to your home directory; refer to your cluster's documentation for details.

## Creating a batch script

Suppose that the script that you want to run is a Python file called 'montecarlo.py'. In order to manage your job and its resources, you must create a second file that contains the instructions for the job scheduler. This file is called a "batch script" and typically has the extension `.sbatch`.

Here is a template for a typical batch script `montecarlo.sbatch`. Note the different parameters that are specified at the top of the file. These are the parameters that you will need to modify for your specific job's resource settings


```bash
#!/bin/bash
# Job name:
#SBATCH --job-name=myjob
#
# Account to charge:
#SBATCH --account=[lab account name]
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
python ./scripts/montecarlo.py 
```

This script will charge the usage to an account `[lab account name]`. On some clusters this is your username, while on others like TACC it is a charge code. Some clusters do not require this field (remove it).

Your batch job will output two files, in addition to any output produced by your script. The first is `myjob.out`, which contains the standard output / printing produced by your script. The second is `myjob.err`, which contains any errors that your script produces.

## Submitting, checking, and cancelling jobs

To submit your job, use the `sbatch` command

    sbatch montecarlo.sbatch

To check the status of your job, use the `squeue` command

    squeue -u USERNAME

To cancel your job, use the `scancel` command

    scancel JOBID

You can get the job ID from the output of `squeue`, or from the initial output of `sbatch` when you submit your job.

## Loading modules

For many packages, you will need to load a pre-installed module on the HPC before you can use it. For example, to use the Anaconda Python distribution on some HPC, you must first load the `anaconda3` module. This is done with the `module load` command. 

    module load anaconda3

This bash command should be placed at the top of your batch script, before the command to run your script. Often you will need to load very specific versions of libraries like `cuda` or `cudnn` for GPU computing. Likewise, `mpi` and `gcc` are very sensitive imports. 
Refer to your cluster's documentation for details on compatibility among different modules.

### Moving files between local and remote

Copy a file from local over to `$HOME`

	$ scp cfgen.py your_username@remotehost.edu:home

Copy a file over to local

    scp your_username@remotehost.edu:my_output_fils/*results.txt /some/local/directory

## Example: A MATLAB job

