Here is a useful [tutorial for TORQUE and Maui](https://kb.iu.edu/d/avmy)

Can literally just write a function wrapper.sh that has a set of commands

	$ source activate py3env
	$ cd my_stuff
	$ python3 < my_program.py

can parallelize using the python library joblib

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