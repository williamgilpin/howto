
# Structuring a Python project

I recently needed to structure a Python project for distribution. I based the structure and approach of my project';s repository on [Google PyBadges](https://github.com/google/pybadges/)

My project was a simple stock portfolio management and rebalancing library, which puts in calls to the Tiingo API in order to pull historical stock data. For this reason, my project needed to store an API key that would not actually be distributed with the project. My final project is here:

[portbalance](https://github.com/williamgilpin/portbalance)

The final structure is:

	root/
	├── portbalance
	│	├── portbalance.py
	│	├── __init__.py
	│	├── config.py
	│	└── assets
	│		└── keys.txt
	├── demos
	│	└── demos.ipynb
	├── resources
	│	└── sample_portfolio.txt
	├── tests
	│	└── test_portbalance.py
	├── .gitignore
	├── MANIFEST.in
	├── LICENSE
	├── setup.py
	└── README.md


## Structuring `setup.py` with global variables

For my project I had a private API key that was stored locally on my computer. I first protecting this by adding the file name to `.gitignore	`. However, since this is a non-Python file that I want linked to the installed package locally, I added a `MANIFEST.in` file to my project’s base directory, in order to ensure that `setup.py` collected this file. I also added the line `include_package_data=True,` in `setup.py`

Because I wanted the API key to become a global variable accessible to multiple files in the project, I added a `config.py` file that figured out all of the global variables. This file was then run at the top of every other project file that needed access to those variables, using `from .config import _API_KEY`

I also had an `__init__.py` file that basically just imported the package

I based this approach on these resources:
+ [Can I use __init__.py to define global variables?](https://stackoverflow.com/questions/1383239/can-i-use-init-py-to-define-global-variables)
+ [Using Python's os.path, how do I go up one directory?](https://stackoverflow.com/questions/9856683/using-pythons-os-path-how-do-i-go-up-one-directory)
+ [Including non-Python files with setup.py](https://stackoverflow.com/questions/1612733/including-non-python-files-with-setup-py)

## Adding tests

+ I used unittests, since it is built-in and can accommodate doctests 
https://github.com/google/pybadges/blob/master/tests/test_precalculated_text_measurer.py
https://www.blog.pythonlibrary.org/2016/07/07/python-3-testing-an-intro-to-unittest/

[Running unittest with typical test directory structure](https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure)






