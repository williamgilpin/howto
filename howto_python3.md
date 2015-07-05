brew install python3

makes "pip3" the package manager for installing packages compatible with python3

# check the install location
ls /usr/local/bin/python*

virtualenv -p /usr/bin/python3.3 py3env
source py3env/bin/activate
