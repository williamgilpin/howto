
## Connect to Lab NAS server on OSX

In Finder:
Go > connect to server

Enter path: `smb://soe-nas/prakash-lab`”

It will prompt you for login credentials, which are:
+ Username: win\SUNet_ID
+ Password : your SUNet password

Please keep regular usage below 500 GB, there's not a lot of space.

## Connect to LAB NAS server on Windows

In Explorer:
"Map network drive"

Enter path: `\\soe-nas\prakash-lab`
+ Check “Connect using different credentials"

It will prompt you for login credentials, which are:
+ Username: win\SUNet_ID
+ Password : your SUNet password

Please keep regular usage below 500 GB, there's not a lot of space.

## Add and remove people from server access

Make sure that you have admin access to the server (request it from SOE IT)

Go to workgroups.stanford.edu

Click "add member"

Enter their Stanford username (ie, for johnsmith@stanford.edu, enter "johnsmith")


## Connect to boa and mamba on a Windows computer

Download Cisco Anyconnect from Stanford

Enter `su-vpn.stanford.edu` using your personal login credentials. This need to be running in order to find boa and mamba

Select "Map Network Drive"

Check the box for "different credentials"

Choose the Location `//mamba/DATA` or `//boa/ps`

Enter the lab's collective username and our standard password

Check the box "remember these credentials" and then click "Enter"

## Connect to boa and mamba on an OSX computer

Go into System Preferences and set up a VPN for su-vpn.stanford.edu

Activate it

In Finder, go to the menu bar and select "Go"

Enter mamba.stanford.edu and then hit enter

Enter the lab's collective username and our standard password
