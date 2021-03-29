# Windows 7 bugs

A running list of bugs and catches I've encountered with our Windows server.

## iPython notebook and Python crash with Errno 10055, internet access breaks

The maximum number of connections is too low. I think that this problem is aggravated if the computer is frequently accessed using remote Desktop. So far the only fix I've found involves editing the registry:

http://stackoverflow.com/questions/15144846/errno-10055-cannot-connect-in-python-network-related-code-on-windows?lq=1
http://stackoverflow.com/questions/7006939/how-to-change-view-ephemeral-port-range-in-windows-machines

https://support.microsoft.com/en-us/kb/196271

## Conda throws `SSL: CERTIFICATE_VERIFY_FAILED`

Try [temporarily disabling SSL](https://github.com/conda/conda/issues/1166)

	conda config --set ssl_verify false
	conda update --all
	conda config --set ssl_verify true


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

# Cannot eject external hard drive

+ Make sure that nothing is accessing the drive, including open Explorer windows
+ Log out of your user account, then log back in. Or try putting hte computer to sleep, and then waking it

## KeyServer and Stanford CMGM program fails

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

# Forced automatic restarts

Windows sometimes forces the computer to restart at night, even when scripts (and even data transfers) are running. In addition to corrupting data, we have had a few cases where interrupting certain tasks corrupted the entire operating system.

For Windows Ultimate and Enterprise, this can be disabled by changing one of the group policy settings as described [here](http://www.makeuseof.com/tag/disable-forced-restarts-windows-update/)

# CrashPlan doesn't work

Go into the Task Manager, enter the "Processes" tab, and kill every process you can find that starts with "CrashPlan"

# CrashPlan can't connect to the backup engine

First test your internet connect (see the ping issue described above). Make sure you have at least 1 GB of RAM allocated for each TB that will get backed up. If you can't even start the app, you have to do a clean reinstall.


# Getting HCImage Live working and capable of performing Batch Export

+ Install HCImageLive with all of the default settings

+ When asked to repair C++, agree to do so

+ When asked to install DCAM, agree to do so

+ Our setup uses Active Silicon firebird, so select this option in the popup menu and then proceed with the installation using all of the defaults.

+ Exit the DCAM installer interface


# Mathematica ParallelTable[] fails inexplicably due to symbols having garbled contexts

If, at any point in your code, you import a package or module (either internal or external), you need to put that import in the body of the function being Tabled.





