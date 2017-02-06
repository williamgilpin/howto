## Installing Miniconda

Use miniconda to avoid installing tons of packages you won't use
Download the installer for whichever python distro you want as default; you can always make an environemnt with a different flavor of python (I used python 2.7 since that's the OSX default)


	 $ bash ./[long file name].sh


--can also just use the default GUI installer for Anaconda (I used miniconda because anaconda isntalled in a weird place)


Can install packages accessible to every conda environment
	
	$ conda install numpy

### Making and using virtual environments

Now try making a new virtual environment via conda

	 $ conda create -n cenv python=2.7
	(cenv) $ source activate cenv
	(cenv) $ echo "local environment install only:"
	(cenv) $ conda install django
	(cenv) $ source deactivate


Updating conda

	 $ conda update conda


Duplicating an environment

	 $ conda list --export > exported-packages.txt
	 $conda create -n py3clone --file exported-packages.txt
-OR-

	 $ conda create -n newname --clone oldname

Removing and environment

	 $ conda remove -n myenv --all


### Broken conda installation

During an update after several months without use, conda stopped working. To recover the installation without deleting all the environments follow the guide [here](http://conda.pydata.org/docs/troubleshooting.html)

Download the same installer as your original install (mine was Python 2.7) and then run it with the -f option:

	bash Miniconda3-latest-MacOSX-x86_64.sh -f

Make sure you install to the same location as your previous installation. You will have a chance to pick your path; I had to purposely change mine to the location of the previous install:

	/Users/william/miniconda

