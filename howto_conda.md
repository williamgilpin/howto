## Installing Miniconda

Use miniconda to avoid installing tons of packages you won't use
Download the installer for whichever python distro you want as default; you can always make an environment with a different flavor of python (I initially used python 2.7 since that's the OSX default, but when I had to reinstall I switch to Python 3)


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
	 $ conda create -n py3clone --file exported-packages.txt

-OR-

	 $ conda create -n newname --clone oldname

Removing an environment

	 $ conda remove -n myenv --all



### Broken conda installation


#### Revert your environment

Some packages install a mess of dependencies, which can break parts of your code. To revert, enter your environment and then view your environment's revision history

	conda list --revisions

Pick which revision you want to go back to. For revision N, run

	conda install --revision N

Found this tip [here](http://blog.rtwilson.com/conda-revisions-letting-you-rollback-to-a-previous-version-of-your-environment/)

#### Attempt a partial re-installation

During an update after several months without use, conda stopped working. To recover the installation without deleting all the environments follow the guide [here](http://conda.pydata.org/docs/troubleshooting.html)

Download the same installer as your original install (mine was Python 2.7) and then run it with the -f option:

	bash Miniconda3-latest-MacOSX-x86_64.sh -f

Make sure you install to the same location as your previous installation. You will have a chance to pick your path; I had to purposely change mine to the location of the previous install:

	/Users/william/miniconda

You may need to edit your bash settings to help get the paths correct

	emacs /Users/william/.bash_profile

#### Completely re-installing

Occasionally conda on OSX will irreversibly and permanently fail with no meaningful way of recovering. Based on the GitHub reports, the developers appear to find these issues too difficult to troubleshoot on a case-by-case basis, and so they instead favor doing a clean re-installation.

The question is whether it is at all possible to recover one's existing environments. I am under the impression that this is very difficult to do because of the way that internal links to moved filed are built into conda. Instead I opted for a clean re-install, which unfortunately meant that I had to re-install various packages piecemeal as I required them

If you still have access to your old, broken conda installation, a list of what was installed can be found in

	/Users/william/miniconda/envs/example_env/lib/python3.4/site-packages

You can export a list of the dependencies using

	cd ~/miniconda_broken/envs/example_env/lib/python3.4//site-packages/
	ls -d */ > ~/example_env_dependencies.txt





