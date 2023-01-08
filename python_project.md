
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


## Other resources

*Handling private data (not for distribution):* For one project I had a private API key that was stored locally on my computer. I first protecting this by adding the file name to `.gitignore`. However, since this is a non-Python file that I want linked to the installed package locally, I added a `MANIFEST.in` file to my project’s base directory, in order to ensure that `setup.py` collected this file. I also added the line `include_package_data=True,` in `setup.py`

*Licensing:* For open source code that you intend to share, it is important to choose and include a license file that specifies the degree of attribution and credit you expect for others to use your code. You can read about the different licenses on [choosealicense.com](). I generally favor MIT or GPLv3 licenses for research code. Put this license in your project's root directory, and name it `LICENSE.md`.

```bash
	$ cd my_project_root
	$ touch LICENSE.md
```

*Global variables.* If you need a certain variable, like an API key, to become a global variable accessible to multiple files in the project, add a `config.py` file that specifies global variables. This file is then invoked at the top of every other project file that needs access to those variables, using `from .config import _API_KEY` (or any global variable name)
Sources: 
+ [Can I use __init__.py to define global variables?](https://stackoverflow.com/questions/1383239/can-i-use-init-py-to-define-global-variables)
+ [Using Python's os.path, how do I go up one directory?](https://stackoverflow.com/questions/9856683/using-pythons-os-path-how-do-i-go-up-one-directory)
+ [Including non-Python files with setup.py](https://stackoverflow.com/questions/1612733/including-non-python-files-with-setup-py)

*Version control for large files:* If you are using git, you can use the following command to ignore all files in a directory (e.g. `data/`) that are not tracked by git: `git update-index --assume-unchanged data/`

*Testing:* For testing, you can use the `unittest` module. For example, if you have a file `core.py` that contains a function `add(a, b)`, you can write a test file `test_core.py` that contains the following code:

	import unittest
	from core import add

	class TestCore(unittest.TestCase):
		def test_add(self):
			self.assertEqual(add(1, 2), 3)

	if __name__ == '__main__':
		unittest.main()

You can then run this test file using `python test_core.py` from the command line. For more information, see the [testing guide](http://www.wgilpin.com/howto/python_unit_testing.html).

*Documentation:* For online documentation, you can use [Sphinx](https://www.sphinx-doc.org/en/master/). For example, if you have a file `core.py` that contains a function `add(a, b)`, you can write a docstring for this function as follows:

```python
	def add(a, b):
		"""Adds two numbers together.

		Args:
			a (int): First number to add.
			b (int): Second number to add.

		Returns:
			int: Sum of a and b.
		"""
		return a + b
```

You can then use Sphinx to generate documentation for this function. For more information, see the [autodoc walkthrough](http://www.wgilpin.com/howto/howto_sphinx.html).

*Linting:* Linting tools automatically check source code for programmatic or stylistic errors. These include formatting of docstrings and code conventions, as well as unused variables and imports. For linting you can use [flake8](https://flake8.pycqa.org/en/latest/) and/or [pylint](https://pylint.pycqa.org/en/latest/). For example, if you have a file `core.py` that contains a function `add(a, b)`, you can lint this function as follows:

```bash
	$ flake8 core.py
	core.py:1:1: F401 'sys' imported but unused
	core.py:3:1: E302 expected 2 blank lines, found 1
	core.py:5:1: E302 expected 2 blank lines, found 1
	core.py:7:1: E302 expected 2 blank lines, found 1
	core.py:9:1: E302 expected 2 blank lines, found 1
```

*Code coverage:* Coverage refers to the fraction of your code that gets run when you invoke your unit tests. You can use [coverage.py](https://coverage.readthedocs.io/en/coverage-5.3/). For example, if you have a file `core.py` that contains a function `add(a, b)`, you can test the code coverage of this function as follows:

```bash
	$ coverage run test_core.py
	$ coverage report
	Name          Stmts   Miss  Cover
	---------------------------------
	core.py          10      0   100%
	test_core.py      6      0   100%
	---------------------------------
	TOTAL            16      0   100%
```

You can then use coverage.py to generate a more detailed report. For more information, see the [coverage.py documentation](https://coverage.readthedocs.io/en/coverage-5.3/).

*Continuous integration:* Larger projects might use continuous integration, in which a set of tests and checks is run automatically whenever code is pushed to the central repo, or a central branch within the repo. For continuous integration, you can use [Travis CI](https://travis-ci.org/). After installing travis, you can set up Travis CI to automatically run tests as follows:

```bash
	$ travis init
	$ git add .travis.yml
	$ git commit -m "Add Travis CI"
	$ git push
```

You can then use Travis CI to automatically run tests for this function. For more information, see the [Travis CI documentation](https://docs.travis-ci.com/).

*Code style:* For code style, you can use [black]() and [isort](). For example, if you have a file `core.py` that contains a function `add(a, b)`, you can automatically format this function as follows:

```bash
	$ black core.py
	$ isort core.py
```

You can then use black and isort to automatically fix some of these issues. For more information, see the [black documentation](https://black.readthedocs.io/en/stable/) and the [isort documentation](https://pycqa.github.io/isort/).

*Static type checking:* For static type checking, you can use [mypy](). For example, if you have a file `core.py` that contains a function `add(a, b)`, you can type check this function as follows:

```bash
	$ mypy core.py
	core.py:1: error: Cannot find implementation or library stub for module named 'core'
	core.py:1: note: See https://mypy.readthedocs.io/en/latest/running_mypy.html#missing-imports
	core.py:1: error: Cannot find implementation or library stub for module named 'core'
```

You can then use mypy to automatically fix some of these issues.

<!-- *Dependency management:* For dependency management, you can use [pip-tools](). For example, if you have a file `core.py` that contains a function `add(a, b)`, you can manage dependencies for this function as follows:

```bash
	$ pip-compile requirements.in
	$ pip-sync requirements.txt
```

You can then use pip-tools to automatically update dependencies. For more information, see the [pip-tools documentation]( -->
<!-- 
*Virtual environments:* For virtual environments, you can use [virtualenv](). For example, if you have a file `core.py` that contains a function `add(a, b)`, you can create a virtual environment for this function as follows:

```bash
	$ virtualenv venv
	$ source venv/bin/activate
	$ pip install -r requirements.txt
```

You can then use virtualenv to automatically update dependencies. For more information, see the [virtualenv documentation](https://virtualenv.pypa.io/en/latest/). -->

<!-- *Package management:* For package management, you can use [poetry](). For example, if you have a file `core.py` that contains a function `add(a, b)`, you can create a package for this function as follows:

```bash
	$ poetry init
	$ poetry add numpy
	$ poetry add pytest
	$ poetry add pytest-cov
	$ poetry add sphinx
	$ poetry add flake8
	$ poetry add coverage
	$ poetry add travis
	$ poetry add black
	$ poetry add isort
	$ poetry add pylint
	$ poetry add mypy
	$ poetry add pip-tools
	$ poetry add virtualenv
```

You can then use poetry to automatically update dependencies. For more information, see the [poetry documentation](https://python-poetry.org/docs/). -->


