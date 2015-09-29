# Alternative to ReadTheDocs (direct hosting of local output on GitHub)

Make a sister directory to the project repo so that it doesn't get commited to your main GitHub repo

Put the 'HTML' folder generated by Sphinx (local compile) into this repository

Initialize this directory on GitHub using the standard method

Now create a gh-pages branch and push the changes to that branch as well:

	git checkout -b gh-pages
	git add .
	git push origin gh-pages

This is a less optimal solution because you have to re-copy the entire folder of documentation each time a change is made

# Using Sphinx

Install Sphinx and numpydoc:

	$ conda install sphinx
	$ pip install numpydoc

Navigate to your local repository:
	 
	 $ mkdir docs
	 $ cd docs
	 $ sphinx-quickstart

It's fine to just accept all the default, but make sure you enable autodoc when you are asked about it.

Edit the conf.py file to include an explicit absolute path to the home folder of your module or library:

     sys.path.insert(0,"/Users/myname/python_files/pypdb/pypdb")

Make sure conf.py includes the following lines:

	extensions = [
	    'sphinx.ext.autodoc',
	    'sphinx.ext.coverage',
	    'numpydoc',
	]

Navigate to the	docs directory and run sphinx:

         $ make html

Format docstrings using .rst styling. Denote headings using :heading:

If make html isn't picking up changes, try touching various .rst files

	$ touch index.rst
	$ touch mymodulename.rst

Eventually one of them will force a rebuild. Can also try:

	$ sphinx-build -E -b html -d _build/doctrees   . _build/html

# Using Read The Docs



Acivate a Web Hook in the settings of the GitHub repository so that every commit will update the docs

In the Project Admin page, enable virtualenv and include a requirements.txt file:

	numpydoc

Put this file in the root of the documentation, docs/. You may also get an ImportError with autodoc that requires you to put a copy of the repository's setup.py in docs/. Why this is necessary is a profound and uninteresting mystery.

# Useful links

[Sphinx for Dummies](https://codeandchaos.wordpress.com/2012/07/30/sphinx-autodoc-tutorial-for-dummies/)