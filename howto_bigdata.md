How to deal with large quantities (> 2 TB) of experimental data

## Windows version

In my efforts, Crashplan stuggled with large backups. Instead I am using Backblaze, which seems to work a little better under the hood.

Windows Backup solution does not work for large drives, it gets confused and claims that the target drive is full when it is not. This might have to do with extremely inefficient version control. For this amount of data, you have to give up on version control.


## Set up Backblaze

+ Exclude local backup drives in the settings
+ Set the "temporary data drive" to one of the externals

Make sure each drive you want backed up has a ".bzvol" file somewhere in its top-level directory (this should be there automatically when you set up BackBlaze)

### Leaving a drive disconnected

If a computer needs to be disconnected for more than a month, try "Pausing" Backblaze using [the instructions given here.](https://help.backblaze.com/entries/21809372-What-happens-to-my-backups-when-I-m-away-or-on-vacation-)

If the computer is unreachable for greater than 6 months, Backblaze will delete your data and there's nothing you can do about that.

### Copying data on Windows

If you prefer a GUI, some people prefer Acronis Disk Backup. I found this software difficult to use given how simple the task was, and so I recommend using the built-in Windows utility robocopy

Always use the command prompt for large amounts of data:

	robocopy D:\William G: /e

Copies the contents of the directory "William" to the base directory of drive G. The option "/e" is essential; without it Windows will mangle everything. Please note that this is a more stable alternative to dragging and dropping, and it appears to be faster than both Windows Explorer and Teracopy

To make a hard drive clone without re-copying old files

	robocopy D:\William\orig G:\William\clone /e /z /mir /W:1 /R:2 /log:C:\William\Desktop\robolog.txt /XF "G:\.bzvol"

The "/mir" is the scary flag that deletes files from the destination if they are not on the source. The "/z" ensures that the copy can be restarted in case of an interruption. the "/W:1" ensures that the copy doesn't pause for too long when it encounters a nasty hidden windows file, and the "/R:2" makes sure that it only attempts the nasty files twice. The "/log" keeps a list of skipped and failed files. The "/XF" excludes the following file, in this case the backblaze log file (Backblaze explodes if you clone the .bzvol file).
Note: MIR can't tell if a file was renamed, sometimes it will just re-copy the entire directory.

**Watch which directory you list as the source and the destination, if you mess this up then terrible things will happen**

### Verify the backup

After the first backup (and every so often afterwards), it is a good idea to check the backup to make sure that it is happening correctly. Right now I just spot-check files, but a much smarter method would involve selecting random files (or even entire directories) and comparing their md5 hashes. I do not yet have a batch script that will do this step

## My current SOP for data backup

Make a two raw data copies on separate hard drives immediately after doing experiments. Put one in a cabinet and forget about it; use the other one to process and crunch the data. Once the actively-modified one is sufficiently different, consider copying it back over (or, even better, onto a new drive). Use a cloud storage service to backup the active drive.
+ Remember that raw data export is not the slow step.

# Miscellaneous

Things I find helpful to have recorded somewhere, but which I am not currently using

## Set up CrashPlan

You should be able to use your Stanford Credentials to access [https://su-backup.stanford.edu](https://su-backup.stanford.edu) using the "Single Sign-On" option

Your username is the "XXX" in XXX@stanford.edu, your password should be the same as your Stanford password

The "backup server" address is also `https://su-backup.stanford.edu`

There is a patch for Crashplan that will increase the ambient RAM usage for faster backup. Can also backup other directories than the C: drive by tweaking the "home" path in one of the settings files.
