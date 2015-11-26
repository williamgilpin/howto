# Windows 7 bugs

A running list of bugs and catches I've encountered with Windows 7, the greatest operating system on earth.

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

## KeyServer and CMGM program fails

Download a new version of the software at [http://sassafras.com/downloads](http://sassafras.com/downloads). Use the address `br-keyserver.stanford.edu` when setting it up, and also use this server address when registering software downloaded through Stanford CMGM. The CMGM wiki can be found [here](https://medwiki.stanford.edu/display/csbfpublic/Home).

+ Installing the Sassafras software takes a suspiciously long amount of time on my Windows 7 machine
+ The installer initially choked out due to a persistent background instance that couldn't be shut down from the Task Manager, even under admin access. Instead I had to resort to killing it by running CMD.exe as an admin and then using:

    >tasklist
    >Taskkill /F /IM keyacc32.exe

# Cannot connect over Ethernet, but Windows thinks it is connected

In the Command Prompt, try

	>ping www.google.com

If this works and all of the packets make it through, then the issue is a computer setting and not a hardware issue---your terminal is successfully connecting to the network. If this is the case, try flushing the DNS.

Run "CMD.exe" as an administrator,

	>ipconfig /flushdns

Try playing with Windows Firewall, and check for other applications (like anti-virus software) that might be interfering. An exhaustive list of possible issues can be found [here](http://www.tomshardware.com/answers/id-1735863/ping-browse.html)

If you reset your firewall settings, make sure you re-enable [Remote Access in the Windows Firewall settings](howto_remote.md)


# CrashPlan doesn't do anything

Make sure you really kill it before trying to restart the program. Go into the Task Manager, enter the "Processes" tab, and kill every process you can find that starts with "CrashPlan"

# CrashPlan can't connect to the backup engine

First test your internet connect (see the ping issue described above)

Make sure you have at least 1 GB of RAM allocated for each TB that will get backed up

If you can't even start the app, you have to do a clean reinstall (this is insane.)









