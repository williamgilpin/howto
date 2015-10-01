# Sherlock cluster at Stanford University

The basis of scheduling jobs using the Sherlock cluster (these instructions probably work for other clusters, like FarmShare 

We are not currently paying for priority access to Sherlock, and so we will get booted from nodes if paying members opt to use their nodes. For this reason, please try to make your jobs persistent: they continously write their output to disk, and can also re-start if stopped. So if you have a giant 'for' loop of image processing, try to write each processed image to disk when you're done with it. 

If you need to keep track of the values of a bunch of variables, try writing the entire execution state of your program to disk every time the loop is called. So if you're doing a massing serial numerical integration, at the end of each timestep write the timestep number and the current values of all of your independent and dependent variables to disk. You have 15GB quota (40 TB if you choose to use the big data nodes), so write everything that you can to disk as often as you can and regret nothing.

## Getting started

Authenticate your computer using Kerberos. You might have to use a VPN if you are off-campus

	$ kinit username@stanford.edu
	$ ssh username@sherlock.stanford.edu

## Make a job script

   	$ emacs my_wonderful_cluster_submission.

## MATLAB jobs

Write as much as you can in a MATLAB script "matlabtest.m" that can just be run directly without further user input.

Now write a batch script that calls the MATLAB file. We'll use the terminal-based text editor emacs

    	$ emacs my_batch_script.sh

You're in the emacs editor window, here's an example script

       #!/bin/bash                                                                                                 
       matlab < matlabtest.m

If you need to change directory, etc, here is the place to use cd, ls, pwd, etc.

Now use emacs to write a batch script "tinytest.sbatch" that allocates resources and submits your script

	#!/bin/bash                                                                                                   
	#                                                                                                             
	#all commands that start with SBATCH contain commands that are just used by SLURM for scheduling              
	#################                                                                                             
	#set a job name                                                                                               
	#SBATCH --job-name=tinytest                                                                                   
	#################                                                                                             
	#a file for job output, you can check job progress                                                            
	#SBATCH --output=tinytest.out                                                                                 
	#################                                                                                             
	# a file for errors from the job                                                                              
	#SBATCH --error=tinytest.err                                                                                  
	#################                                                                                             
	#time you think you need; default is one hour                                                                 
	#in minutes in this case                                                                                      
	#SBATCH --time=1:00                                                                                           
	#################                                                                                             
	#quality of service; think of it as job priority                                                              
	#SBATCH --qos=normal                                                                                          
	#################                                                                                             
	#number of nodes you are requesting                                                                           
	#SBATCH --nodes=1                                                                                             
	#################                                                                                             
	#memory per node; default is 4000 MB per CPU                                                                  
	#SBATCH --mem=1000                                                                                            
	#you could use --mem-per-cpu; they mean what we are calling cores                                             
	#################                                                                                             
	#tasks to run per node; a "task" is usually mapped to a MPI processes.                                        
	# for local parallelism (OpenMP or threads), use "--ntasks-per-node=1 --cpus-per-tasks=16" instead            
	#SBATCH --ntasks-per-node=1                                                                                   
	#################                                                                                             

	#now run normal batch commands                                                                                
	module load openmpi/1.6.5/intel13sp1up1
	
	#you have to actually load matlab first
	module load matlab

	#run Intel MPI Benchmarks with mpirun                                                                         
	srun /usr/mpi/intel-13/openmpi-1.6.5-1/tests/IMB-3.2.4/IMB-MPI1

	#now call your bash file
	bash my_batch_script.sh

Now submit your job

	sbatch tinytest.sbatch

Check on your job

	squeue

Output should be written to tinytest.out, and any warnings thrown by the compiler should go to tinytest.err

### Notes

+ Look at the Sherlock wiki to see how to use the big data nodes for working on large numbers of image files
+ Use standard terminal commands like scp, etc to move files back and forth between your computer and the cluster



## Python jobs

### Sandboxing (recommended)

+For Python 3, use the built-in pyenv scripts
+For Python 2.7, use the package virtualenv


