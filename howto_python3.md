
**As of 2018, Python 3 should already be installed by default on macOS**

Install Python 3 on OSX using Homebrew

	$ brew install python3

Try using "pip3" the package manager for installing packages compatible with python3

	$ pip3 install numpy

Now check the install location
	
	$ ls /usr/local/bin/python*

	$ virtualenv -p /usr/bin/python3.3 py3env
	$ source py3env/bin/activate
