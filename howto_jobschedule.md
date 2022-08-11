Here is a useful [tutorial for TORQUE and Maui](https://kb.iu.edu/d/avmy)

Can parallelize using the python library joblib. For parallel computations with joblib, the TORQUE script parameter ppn (processors per node) is the really handy parameter because it allows you to parallelize on a single node using joblib, instead of parallelize across nodes using mpi

### Move files back and forth

From local host to remote (currently in local):

    scp my_files.txt john@yale.edu:some/remote/directory

From remote host to remote (currently in local):

    scp john@yale.edu:some/remote/directory/my_files.txt /some/local/directory

Standard regular expressions (`*`) can be used to send groups of files back and forth

### Example workflow

Here is the list of files in order to run a Python 3 script in a virtual environment (which is necessary in order to include all of the necessary dependencies)

The wrapper.sh file, which is in a directory called all_my_python_files

    #!/bin/bash                                                                     
    python3 < my_python_script.py


The actual file submitted as a job, my_job.sh

    #!/bin/bash                                                                     
    #PBS -k o                                                                       
    #PBS -l nodes=1:ppn=16,walltime=70:00:00                                        
    #PBS -M someemail@gmail.com                                            
    #PBS -m abe                                                                     
    #PBS -N public_display_name                                                            
    #PBS -j oe                                                                      
    source ./venv/bin/activate
    cd all_my_python_files
    bash wrapper.sh

## Submitting the job

    qsub job.sh
    qstat
    qdel 

## Retrieving output files

On the local host (sends all files ending in "results.txt")

    scp your_username@remotehost.edu:my_output_fils/*results.txt /some/local/directory

