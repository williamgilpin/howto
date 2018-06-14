
Sometimes you have a bunch of helper functions or utilities that you've created for plotting or analyzing certain types of data. Putting these in a dedicated GitHub repo is overkill, but you'd like to have a single local directory with these files for the sake of easy version control, etc

Loosely based on [this stackexchange post](http://stackoverflow.com/questions/42214325/how-to-create-a-local-python-package-for-modules-that-i-use-for-several-differen)

### Setting up local packages for utilities

The directory structure needs to look something like this

	cd ~/Documents/plotting_tools


	plotting_tools/setup.py
	plotting_tools/plotting_tools/violin_plot_tools.py
	plotting_tools/plotting_tools/scatter_plot_tools.py

The setup.py should look something like this

	from distutils.core import setup

	setup(
	    name='analysis_utilities',
	    version='0.1',
	    description='utility library',
	    author='My Name',
	    author_email='name@emailservice.com',
	    requires=[ 'numpy', 'scipy', 'matplotlib',],
	    py_modules=['config'],
	    packages=['plotting_tools', ],
	    package_data={
	    	'plotting_tools': ['*'],
	    	'plotting_tools.violin_plot_tools': ['*'],
	    	'plotting_tools.extra_tools': ['*'],
	    	'plotting_tools.yet_another_submodule': ['*'],
	    },
	)

Note: things will go really bad if the files in your package are interdependent and need to import each other. Structure your code carefully to minimize these interdependencies (such as by defining a central "helper functions" library with no dependencies that gets imported first by __init__.py

If interdependices are unavoidable, make sure you import in the right order.


### Using the local packages

Make a new directory and accompanying virtual environement for a new project

Activate the virtual environment, then `cd` to the directory of the local utility package that you want to use

	cd ~/my_utilities/plotting_tools

Now run

	python setup.py install

Now return to your working directory, and you will be able to import/use packages as necessary. In your Python environment

	from plotting_tools.violin_plot_tools import *

If you need to edit/update `violin_plot_tools.py` then re-run `python setup.py install` after making the edits, then re-import the package


### Updating the packages

Alter the local package .py files as needed

In your project's virtual environment, change back to the local package directory and re-run

	python setup.py install

If you really have to, use
	
	python setup.py install --force

