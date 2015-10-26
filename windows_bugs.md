# Windows 7 bugs

A running list of bugs and catches I've encountered with Windows 7, and if/how I was able to fix them

## iPython notebook and Python crash with Errno 10055, internet access breaks

The maximum number of connections is too low. I think that this problem is aggravated if the computer is frequently accessed using remote Desktop. So far the only fix I've found involves editing the registry:

http://stackoverflow.com/questions/15144846/errno-10055-cannot-connect-in-python-network-related-code-on-windows?lq=1
http://stackoverflow.com/questions/7006939/how-to-change-view-ephemeral-port-range-in-windows-machines

https://support.microsoft.com/en-us/kb/196271

## Mounting a mapped network windows drive from a OSX

1. Enable sharing of the drive from within Windows
2. Email IT to get the drive whitelisted with the firewall
3. From your Mac, use the Finder "Go to Server" and enter `smb://other_username:*@server.name.here`
		other_username is the full username on the remote server. For Stanford's domain, that's
		win\username (note direction of slash)
4. Enter your Windows password

## Hard drive mysteriously fills up

+ Run WinDirStat as an Administrator by right clicking on it
+ If the glut comes from the Windows folder, go ahead and delete Windows > Temp
+ If the origin of the glut appears to be cab_xxxx files, try deleting all of the files from Windows > Logs > CBS
+ + If you hit any admin errors or failed deletes, just skip those files
+ Empty the recycling bin