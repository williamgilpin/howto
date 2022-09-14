
# Structuring a Python project

For your class projects, it will likely be useful to structure your code repository in a manner that maximizes its readability and extensibility. Some good examples are
+ [PyBadges](https://github.com/google/pybadges/)
+ [tslearn](https://github.com/tslearn-team/tslearn)
+ [darts](https://github.com/unit8co/darts)
+ [tigramite](https://github.com/jakobrunge/tigramite)

An example of a generic project structure might look something like the following. Generally we try not to crowd the root level of the repo with too many files except for README.md, setup.py, and any required dotfiles.

	projectname/
	├── projectname
	│	├── core.py
	│	├── utils.py
	│	├── __init__.py
	│	├── config.py
	│	└── assets
	│		└── keys.txt
	├── demos
	│	└── demos.ipynb
	├── docs
	│	├── index.html
	│	└── doc_buildfiles
	├── resources
	│	├── sample_dataset.txt
	│	├── example_output.txt
	│	├── figure_for_readme.png
	│	└── video_for_readme.gif
	├── tests
	│	├── test_core.py
	│	└── test_utils.py
	├── benchmarks
	│	├── run_benchmarks.py
	│	└── benchmark_data/
	│		├── benchmark_dataset1.txt
	│		└── benchmark_dataset2.txt
	├── .gitignore
	├── MANIFEST.in
	├── LICENSE.md
	├── setup.py
	└── README.md

## Miscellaneous

*Handling private data (not for distribution):* For one project I had a private API key that was stored locally on my computer. I first protecting this by adding the file name to `.gitignore`. However, since this is a non-Python file that I want linked to the installed package locally, I added a `MANIFEST.in` file to my project’s base directory, in order to ensure that `setup.py` collected this file. I also added the line `include_package_data=True,` in `setup.py`

*Global variables.* If you need a certain variable, like an API key, to become a global variable accessible to multiple files in the project, add a `config.py` file that specifies global variables. This file is then invoked at the top of every other project file that needs access to those variables, using `from .config import _API_KEY` (or any global variable name)
Sources: 
+ [Can I use __init__.py to define global variables?](https://stackoverflow.com/questions/1383239/can-i-use-init-py-to-define-global-variables)
+ [Using Python's os.path, how do I go up one directory?](https://stackoverflow.com/questions/9856683/using-pythons-os-path-how-do-i-go-up-one-directory)
+ [Including non-Python files with setup.py](https://stackoverflow.com/questions/1612733/including-non-python-files-with-setup-py)



