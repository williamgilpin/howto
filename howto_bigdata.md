How to deal with large quantities (> 2 TB) of experimental data

## Windows version

Crashplan and pretty much any cloud storage option is out of the question for backups larger than 500 GB. Even if it works, the upload time is dozens of days

Windows Backup solution does not work for large drives, it gets confused and claims that the target drive is full when it is not. This might have to do with extremely inefficient version control. For this amount of data, you ahve to give up on version control.

WD drives come with Acronis True Image, which is usually shareware but which appears to be free for the purpose of disk cloning. This is probably the best option for just cloning a drive, particular if you have multiple drives with separate backups.

### Run an Acronis disk clone backup

You must buy the Acronis full software for $30 if you want to run scheduled cloning

+ In the Acronis Software, select "Clone Disk" and then the "automatic wizard" choice. 
+ Select GPT-style for the backup type (not bootable, but better for large amounts of data)


### Verify the backup

After the first backup (and every so often afterwards), it is a good idea to check the backup to make sure that it is happening correctly. To do this, 

*try some sort of stochastic checksum tool?**

## Set up CrashPlan

You should be able to use your Stanford Credentials to access [https://su-backup.stanford.edu](https://su-backup.stanford.edu) using the "Single Sign-On" option

Your username is the "XXX" in XXX@stanford.edu, your password should be the same as your Stanford password

The "backup server" address is also `https://su-backup.stanford.edu`

There is a patch for Crashplan that will increase the ambient RAM usage for faster backup. Can also backup other directories than the C: drive by tweaking the "home" path in one of the settings files.

## Set up Backblaze

+ Exclude local backup drives in the settings
+ Set the "temporary data drive" to one of the externals

Make sure each drive you want backed up has a ".bzvol" file somewhere in its top-level directory (this should be there automatically when you set up BackBlaze)

### Leaving a drive disconnected

If a computer needs to be disconnected for more than a month, try "Pausing" Backblaze using [the instructions given here.](https://help.backblaze.com/entries/21809372-What-happens-to-my-backups-when-I-m-away-or-on-vacation-)

If the computer is unreachable for greater than 6 months, Backblaze will delete your data and there's nothing you can do about that.

### Copying data on Windows

Always use the command prompt for large amounts of data:

	robocopy D:\William G: /e

Copies the contents of the directory "William" to the base directory of drive G. The option "/e" is essential; without it Windows will mangle everything. Please note that this is a more stable alternative to dragging and dropping, and it appears to be faster than both Windows Explorer and Teracopy

To make a hard drive clone without re-copying old files

	robocopy D:\William\orig G:\William\clone /e /z /mir /W:1 /R:2 /log:C:\William\Desktop\robolog.txt

The "/mir" is the scary flag that deletes files from the destination if they are not on the source. The "/z" ensures that the copy can be restarted in case of an interruption. the "/W:1" ensures that the copy doesn't pause for too long when it encounters a nasty hidden windows file, and the "/R:2" makes sure that it only attempts the nasty files twice. The "/log" keeps a list of skipped and failed files
Note: MIR is dumb and can't tell if a file was renamed, sometimes it will just re-copy the entire directory.

**Watch which directory you list as the source and the destination, if you mess this up then terrible things will happen**

## Current SOP for data backup

Make a two raw data copies on separate hard drives immediately after doing experiments. Put one in a cabinet and forget about it; use the other one to process and crunch the data. Once the actively-modified one is sufficiently different, consider copying it back over (or, even better, onto a new drive). Use a cloud storage service to backup the active drive.
+ Remember that raw data export is not the slow step.
