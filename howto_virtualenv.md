
NOTE: Only use these directions if using Python 2

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
	
	$pip freeze > requirements.txt

## Make a Python 3 environment

Just use the built-in virtualenv:

	$ pyvenv-3.3 /home/username/all_venvs/desired_venv_name
	$ source /home/username/all_venvs/desired_venv_name/bin/activate

On cluster, must first run

	$ module load python/3.3.2

Otherwise will get error

	python: error while loading shared libraries: libpython3.3m.so.1.0: cannot open shared object file: No such file or directory
