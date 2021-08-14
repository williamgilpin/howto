Suppose we have written a Python package, like [pypdb](). Our goal is to make it possible for users to install the package using PyPI:

	$ pip install pypdb

## Initialization and setup

+ Make an account on [PyPI](https://pypi.org/account/register/). Note: Depending on your project scale, consider also making a matching account on [TestPyPI](https://test.pypi.org/account/register/) for testing
+ In your computer's home folder , create a `.pypirc` file, which allows authentication

	[distutils]
	index-servers =
	  pypi
	  pypitest

	[pypi]
	repository=https://pypi.python.org/pypi
	username=your_username
	password=your_password

Set the appropriate permissions

	$ chmod 600 ~/.pypirc

## Setup project structure

Follow the instructions [here](howto_python_project.md) for properly setting up a Python project. In the root directory, add a file `setup.cfg` containing the following

	[metadata]
	description-file = README.md

## Development and testing

During development, continuously update your local installation by having a Terminal window directed to the location of `setup.py`, and periodically run 

	pip install -I --no-dependencies .

This is much easier than trying to import locally from a path. The `no-dependencies` flag ensures that pip does not try to reinstall all of the dependencies, especially packages like numpy that may have been installed using conda.

## Updating existing package

Update `setup.py` to the latest version number. Pay attention to the number of digits after the decimal: 1.3 will be counted as a lower release number than 1.299

Update and push the new version number to GitHub

    $ git tag 0.5 -m "latest version"
    $ git push --tags origin master

Make a distribution

	python setup.py sdist bdist_wheel

Install twine using pip if needed. Now upload the new distribution via twine

	python3 -m twine upload --skip-existing -r pypi dist/* --verbose

Enter PyPI credentials when prompted to do so

# Troubleshooting


### Issues authenticating when uploading to PyPI from Terminal

You might need to make a file at `~/.pypirc` containing

	[distutils]
	index-servers =
	    pypi

	[pypi]
	repository: https://pypi.python.org/pypi
	username: <username>
	password: <pass>

This will help avoid having to login elsewhere. If you are having problems logging in, check the contents of this file