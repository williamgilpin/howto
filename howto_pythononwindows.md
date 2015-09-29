# Python on Windows

## Without another installed shell

Install Anaconda from the .exe installer available on the Anaconda website

Use the included Anaconda shell

Update the installed version

    > conda update --all

Change to to data drive on Windows

	> D:\William

Change directories on drive

	> cd code

Activate conda env

	> activate py3env


## Using Cygwin

Download and install the full Cygwin suite

Open up the Cygwin Terminal

Go to the drive of interest. For the "C:" drive:

	$ cd /cygdrive/C

To run a program in the shell, make sure to use the "-i" flag

	$ python -i

**I'm stuck here because python keeps crashing when run in cygwin**

## Using MinGW and msys

msys is a bash shell, but you have to add Anaconda to the path by creating a .bashrc or .bashprofile in the home directory (wherever the shell starts you out when if first opens). Note: there is a later version, msys2, that may have more active development

+ Install MinGW
+ Install msys
	+ edit msys apearance by right clicking the top bar of an open shell window
+ Install Emacs for Windows:
	+ Download 7zip archive from SourceForge and right click to extract with 7zip
	+ ?????




