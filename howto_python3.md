The easiest way to install Python 3 is to just use Homebrew

	$ brew install python3

Try using "pip3" the package manager for installing packages compatible with python3

	$ pip3 install numpy

Now check the install location
	
	$ ls /usr/local/bin/python*

	$ virtualenv -p /usr/bin/python3.3 py3env
	$ source py3env/bin/activate
