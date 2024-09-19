# Python on Windows

## Using Windows Subsystem for Linux (WSL)

Most modern versions of Windows have the Windows Subsystem for Linux (WSL) pre-installed. This allows you to run a full Linux distribution on your Windows machine. This is the current recommended way to run Python on Windows. You can enable WSL by opening a PowerShell terminal as an administrator and running the following command:

```powershell
wsl --install
```
This will install the latest version of WSL and the Ubuntu distribution. You can then open a WSL Terminal by typing `wsl` or `Ubuntu` in the Windows search bar. You can find detailed instructions from Microsoft [here](https://learn.microsoft.com/en-us/windows/wsl/setup/environment).

Once you have installed WSL, you can use the WSL Terminal to install Python and other common packages. You will also use it to run any bash or Terminal commands that you encounter in documentation. On macOS systems, one often installs packages using `sudo brew install`. On WSL, you will use `sudo apt install`. 

We will start by installing Python. You can install Python 3 and pip by running the following commands in the WSL Terminal:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

We next will install git, which is a version control system that is commonly used in conjunction with GitHub, an online hosting service for code. You can install git by running the following command in the WSL Terminal:
```bash
sudo apt install git
```
You may receive a message that git is already installed. This is fine.

We will now install a text editor. You can install `nano` by running the following command in the WSL Terminal:
```bash
sudo apt install nano
```
You may receive a message that `nano` is already installed. You may also install other text editors like `vim` or `emacs` if you prefer. 

## DEPRECATED: Anaconda shell

Install Anaconda from the .exe installer available on the Anaconda website. Open the included Anaconda shell app, and then update the installed version

    > conda update --all

To change to a data drive on Windows

	> D:\William

To change directories on drive

	> cd code

To activate conda env

	> activate py3env


## DEPRECATED: Using git bash

We originally used git bash to run Python on Windows, via the instructions [here](https://scotch.io/tutorials/get-a-functional-and-sleek-console-in-windows). However, we ran into [some issues](https://groups.google.com/a/continuum.io/forum/#!topic/anaconda/VxL6QmcKgv4) with Anaconda, and the only solution was to manually put the environment on the path.

## DEPRECATED: Using Cygwin

Download and install the full Cygwin suite from their website. Open up the Cygwin Terminal application and go to the drive of interest. For the "C:" drive:

	$ cd /cygdrive/C

To run a program in the shell, make sure to use the "-i" flag

	$ python -i


## DEPRECATED: Using MinGW and msys

msys is the MinGW bash shell, but you have to add Anaconda to the path by creating a `.bashrc` or `.bashprofile` in your home directory (wherever the shell starts you out when if first opens). There is also a successor, msys2, that may have more active development




