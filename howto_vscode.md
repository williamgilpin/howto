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



### Troubleshooting

+ VSCode is running hot on my MacBook

+ + I had this issue on Catalina in 2022, and the only fix I could find was upgrading macOS to the latest release