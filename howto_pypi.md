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

Follow the instructions [here](howto_python_project.md) for properly setting up a Python project. In the root directory, add a file `setup.cfg`

	[metadata]
	description-file = README.md

## Publish the project

First, register and upload it on the test server

	$ python setup.py register -r pypitest
	$ python setup.py sdist upload -r pypitest

If all goes okay, upload to the live server
	
	$ python setup.py register -r pypi
	$ python setup.py sdist upload -r pypi


## Updating the package

This is really only necessary when the actual package changes, you can mess with the demos and README on GitHub all you want because that's not stored on PyPI

+ Update the code
+ Update setup.py and increment the version number
+ Push to Github
+ Now update git tags:

    $ git tag 0.5 -m "latest version"
    $ git push --tags origin master

+ Now update the PyPI listing with the newest version:

    $ python setup.py sdist upload -r pypi


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

This will help avoid having to login elsewhere