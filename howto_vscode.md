# Visual Studio Code



### Set up remote access to a local session

+ Apply for access to the private beta [here](https://code.visualstudio.com/docs/remote/vscode-server). The first step is

	wget -O- https://aka.ms/install-vscode-server/setup.sh | sh

+ Download the required software and install it locally.

+ On remote, move to the directory that you want to share:

	cd ~/my_project

+ From within that folder, run

	code-server

+ Copy and paste the resulting link, which you can use to access that session remotely

Can manage virtual environment and other Terminal tasks by opening a Terminal from within the VSCode interface

### Troubleshooting

+ VSCode is running hot on my MacBook

+ + I had this issue on Catalina in 2022, and the only fix I could find was upgrading macOS to the latest release

+ My local connection to VSCode is throwing strange errors

+ + If you have a separate VSCode session running on remote as a local instance, you can sometimes get bugs. My preferred workflow is to keep the server running on remote, but avoid opening the application on it. 