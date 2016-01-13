# Enable Remote Desktop on Windows 7

#### Setting preferences on the Windows computer

Allow things through the Firewall

+ Control Panel > All Control Panel Items > Windows Firewall > Allowed Programs
+ Check the box next to Remote Desktop. By default this should select the "Domain" check box

Enable Remote Desktop

+ Computer > Properties > Remote (tab) 
+ Check "Allow connections from computers running any..."

#### Setting up Microsoft Remote Desktop Connection

Download the Microsoft Remote Desktop App if it isn't pre-installed

Have to log out and log back in using `win\<my SUID>`
The password is my SUID password

Useful SOE IT links:

[HOW TO LOGIN TO AN ENCRYPTED WINDOWS 7 COMPUTER AS A DOMAIN/LOCAL USER](https://soeithelp.stanford.edu/entries/53099613-How-to-login-to-an-encrypted-Windows-7-computer-as-a-domain-local-user)

# Setting up the Remote Desktop Client on OSX

Click on the + sign, the only information you need to enter is your Stanford login credentials and the hostname or IP address of the Windows computer to which you want to connect. You can only do this once Remote desktop has successfully been enabled on that computer.

Your computer's hostname or IP can be found in many ways, [here is how to do it on Windows 7](http://windows.microsoft.com/en-us/windows/find-computer-name#1TC=windows-7)


# Enable Remote Desktop from outside of Stanford Network

Setup a VPN using the built-in OSX utility by following the [IT instructions here](https://uit.stanford.edu/service/vpn/mac_builtin)

Use Remote Desktop as you normally would.