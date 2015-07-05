Use miniconda to avoid installing tons of packages you won't use
Download the installer for whichever python distro you want as default; you can always make an environemnt with a different flavor of python (I used python 2.7 since that's the OSX default)


>> bash ./[long file name].sh


--can also just use the default GUI installer for Anaconda (I used miniconda because anaconda isntalled in a weird place)


Can install packages accessible to every conda environment
>> conda install numpy


Now try making a new virtual environment via conda
>> conda create -n cenv python=2.7
(cenv) >> source activate cenv
(cenv) >> echo "local environment install only:"
(cenv) >> conda install django
(cenv) >> source deactivate


Updating conda
>> conda update conda


Duplicating an environment
>> conda list --export > exported-packages.txt
>> conda create -n py3clone --file exported-packages.txt
-OR-
>> conda create -n newname --clone oldname

Removing and environment
>> conda remove -n myenv --all
