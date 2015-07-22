Follow the instructions [here](http://peterdowns.com/posts/first-time-with-pypi.html)

Remove all double braces
Explicitly put your password in both the pypi rc file and the pypi test rc file, to avoid a weird error 


## Updating a PyPi package

This is really only necessary when the actual package changes, you can mess with the demos and README on GitHub all you want because that's not stored on PyPI

+ Update the code
+ Update setup.py and increment the version number
+ Push to Github
+ Now update git tags:

    $ git tag 0.5 -m "latest version"
    $ git push --tags origin master

+ Now update the PyPI listing with the newest version:

    $ python setup.py sdist upload -r pypi