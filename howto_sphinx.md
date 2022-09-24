


# Creating a documentation website from docstrings

This guide shows how to convert Python code with well-formatted docstrings into a dedicated documentation website for your project, using autodocumentation. Examples of autodocs can be seen [here] and [here]

1. Install Sphinx in your working environment. Depending on the formatting of your docstrings, you may need to also install an extension that allows sphinx to correctly parse them. I use [Google-style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/), which are supported in sphinx by default

	$ conda activate project_env
	$ conda install sphinx

2. In your project repository, make a top-level directory named `docs`. For example, in a recent project [`dysts`](https://github.com/williamgilpin/dysts), My directory has the following structure

	my_proj/
	├── benchmarks/
	│	└── ...
	├── docs/
	│	├── spbuild/
	│	│	└── ...
	│	├── .nojekyll
	│	├── Makefile
	│	├── conf.py
	│	├── index.html
	│	├── index.rst
	│	└── make.bat
	├── my_proj/
	│	└── ...
	├── tests/
	│	└── ...
	├── benchmarks/
	│	└── ...
	├── ...
	└── README.md

We have used `...` to denote miscellaneous files that are either unrelated to documentation, or which will be automatically generated (we won't touch them).

3. Navigate to your `docs` directory and run the sphinx quickstart

	 $ mkdir docs
	 $ cd docs
	 $ sphinx-quickstart

3. The quickstart will walk you through the various options. I normally accept all the defaults, but I make sure to enable autodoc when asked about it. For version numbers, for code-in-progress I usually start with low decimals like 0.1, with version 1.0 coming later as a release candidate (ready for public consumption), and major releases with new features, refactoring, or backwards-incompatible changes reserved for whole numbers (2.0, 2.0, etc).




4. Add the following lines to the `conf.py` file, in order to include an explicit local path to the "core" folder of your module or library

    import os
	import sys
	sys.path.insert(0, os.path.abspath('../..'))

5. Sphinx has many [extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html), which are used to modify the style and extent of documentation. These can be activated/deactivated by changing the `extensions` variable in the `conf.py` file. Currently, my `conf.py` file contains the following lines:

	extensions = [
		'sphinx.ext.autodoc',
		'nbsphinx',
		'sphinx.ext.napoleon'
	]

You can also modify other features of the configuration file. For example, to exclude certain files or directories from autodocumentation, you can edit the `exclude_patterns` variable in `conf.py`. Currently mine looks like

	exclude_patterns = ['_build', '_templates', 'Thumbs.db', '.DS_Store']

Finally, you can also tweak the visual appearance of your documentation by modifying the `html_theme` variable. Currently, I use the default theme, but [many others exist](https://www.sphinx-doc.org/en/master/usage/theming.html)

	html_theme = 'alabaster'

6. Once the configuration is set up, Navigate in your terminal to the docs directory and run sphinx.

    $ make html

Sphinx should start attempting to render HTML from your project's docstrings. If you run into an error, make sure that you are in the `docs` folder, and that the conda environment in which you install sphixn is currently active.

If all was successful, you should find the documentation rendered as an HTML file in the `_build` directory.

7. We now want to host our project documentation using GitHub pages. Still within your `docs` directory, create a file that will tell GitHub pages to avoid attempting to re-render the HTML pages that sphinx just created. In the Terminal, run

	$ touch .nojekyll

*(Optional) GitHub Pages will ignore any files starting with an underscore. Depending on the contents of your `.gitignore`, files containing the name `build` may also be ignored. In this case, edit the contents of the sphinx `Makefile` to point to the new `newbuilddirname/html/` directory.

8. Add a new `index.html` to your `docs` directory that redirects to the `index.html` inside the new build directory. You can make this HTML file in VSCode or another text editor, or directly in the terminal with emacs or vim. In any case, `index.html` should contain only the following line

		<meta http-equiv="refresh" content="0; url=./build/html/index.html" />

If you renamed your `build` folder in the previous step in order to get around your `.gitignore` restrictions, then you will need to rename it in the url here as well. 

9. Assuming that your project has a working GitHub repository, push all of your changes to the main branch on GitHub. In the GitHub UI, navigate to your project's settings. These are usually found under a URL of the form

	https://github.com/myusername/my_project/settings/pages

In this interface, make sure that "Source" is set to "Deploy from a Branch" and that the "Branch" is set as "main" followed by "/docs". You can edit other settings from this page, if you want to use a custom domain or enforce various security settings. Once you have configured things, save your settings.

GitHub pages should now find your rendered sphinx HTML files, and (after some time delay), they will appear online at

	http://username.github.io/my_project/build/html/index.html



<!-- # Hosting project documentation using GitHub pages

Make a sister directory to the project repo so that it doesn't get commited to your main GitHub repo

Put the 'HTML' folder generated by Sphinx (local compile) into this repository

Initialize this directory on GitHub using the standard method

Now create a gh-pages branch and push the changes to that branch as well:

	git checkout -b gh-pages
	git add .
	git push origin gh-pages

This is a less optimal solution because you have to re-copy the entire folder of documentation each time a change is made. I'm still working on a smoother fix.

For example, for my project [pypdb] I go through the following checklist when committing new documentation to the main branch:

+ Remove temporary copies of main file from ipynb directory
+ Export HTML file of all notebooks and put in the right directories
+ Update all documentation:

	+ Compile sphinx
	+ Retrieve HTML folder from output
	+ Put this HTML folder in the Documentation GitHub repository
	+ push to master
	+ push to gh-pages branch

+ Update version number in setup.py
+ push to GitHub
+ Update Github tags
+ Update PyPI
+ Test pip install in a clean environment -->


# Rebuilding documention

You can update your project's documentation by re-running `make html`. 

Delete all directories beginning with an underscore. Running `make clean` will delete everything under `_build`, but the output of extensions like `autosummary` will not be deleted, which can cause issues. 

# Using Read The Docs instead of GitHub Pages

For various reasons, you might prefer to host your project's documentation on [ReadTheDocs](https://readthedocs.org/) instead of GitHub. This can be accomplished by activating a Web Hook in the settings of the GitHub repository so that every commit will update the docs

If you are using a custom docstring style or otherwise have a dependency outside of core sphinx, then in the ReadTheDocs Project Admin page, enable virtualenv and include a requirements.txt file:

	numpydoc

Put this file in the root of the documentation, docs/. You may also get an ImportError with autodoc that requires you to put a copy of the repository's setup.py in docs/. Why this is necessary is a profound and uninteresting mystery.

# Problems

1. Updating my documentation does not update my docs.

+ Sphinx builds from the module from the version that is installed in the environment. It does *not* use the current local setup.py; it uses whatever was most recently installed in the environment. See [here](https://stackoverflow.com/questions/44693301/sphinx-is-caching-python-module-somewhere-where)
+ If `make html` isn't picking up changes, try touching various .rst files

	$ touch index.rst
	$ touch mymodulename.rst
+ Try forcing a re-build 

	$ sphinx-build -E -b html -d _build/doctrees   . _build/html

+ If all else fails, try deleting the current files inside the `_build` directory and re-running `make html` 


2. Sphinx is not finding the correct directory for documentation

 Edit the `conf.py` file to include an explicit absolute local path to the "core" folder of your module or library:

     sys.path.insert(0,"/Users/myname/python_files/my_project/my_project")


# Useful links

[Sphinx for Dummies](https://codeandchaos.wordpress.com/2012/07/30/sphinx-autodoc-tutorial-for-dummies/)

[Sphinx guide](https://eikonomega.medium.com/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365)

[Sphinx with GitHub Pages]](https://github.com/sphinx-doc/sphinx/issues/3382)