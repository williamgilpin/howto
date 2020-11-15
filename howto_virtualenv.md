
# Python 2

## Make an environment from a list of desired packages

	emacs requirements.txt
	mkdir first_light
	virtualenv ./first_light/
	(virtualenv --python=/usr/bin/python3 venv)
	(virtualenb -p python3 venv)
	source ./first_light/bin/activate
	pip install -U -r requirements.txt
	deactivate

## Open environment
	
	$ source ./first_light/bin/activate

## Save Requirements
	
	$ pip freeze > requirements.txt

# Python 3

Just use the built-in alternative to  virtualenv:

	$ pyvenv-3.3 ./all_venvs/desired_venv_name
	$ source ./all_venvs/desired_venv_name/bin/activate

# Cluster management of virtual environment

On Sherlock cluster, must first run

	$ module load python/3.3.2

Otherwise will get error

	python: error while loading shared libraries: libpython3.3m.so.1.0: cannot open shared object file: No such file or directory

## Updating/importing libraries on a managed cluster

### Setup (can do this either within or outside of venv)

	$ easy_install-3.3 --user pip
	$ export PATH=~/.local/bin:$PATH
	$ pip3.3 install --user scipy numpy matplotlib
