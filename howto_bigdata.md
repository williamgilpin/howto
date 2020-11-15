Our 2017 Laboratory protocol for maintaining large quantities (> 10 TB) of experimental data

## Set up Backblaze

+ Exclude local backup drives in the settings
+ Set the "temporary data drive" to one of the externals

Make sure each drive you want backed up has a ".bzvol" file somewhere in its top-level directory (this should be there automatically when you set up BackBlaze)

To speed up the initial upload

+ From the Backblaze control panel, go into "Settings" > "Performance" and slide the "Manual Throttle" all the way to the right. 
+ If you have multiple cores, consider enabling multiple backup threads. A good set of criteria for when this should be helpful is given [here](https://www.backblaze.com/blog/backblaze-online-backup-4/)
+ A good sanity check is to see whether the "Latest File Upload Speed" reported in the Performance panel is consistent with your internet upload speed (we just estimated this using online services)
+ If you need to use your computer for any intensive computations during this time, consider automatic throttling and removing multithreading while you are running your task.
+ Backblaze currently won't back up files if the hard drive has less than 1.1x the size of the largest file that needs to backed up. You can get around this by setting up a "Temporary Data Drive" that BackBlaze uses for scratch instead of the target hard drive.

### Leaving a drive disconnected

If a computer needs to be disconnected for more than a month, try "Pausing" Backblaze using [the instructions given here.](https://help.backblaze.com/entries/21809372-What-happens-to-my-backups-when-I-m-away-or-on-vacation-)

If the computer is unreachable for greater than 6 months, Backblaze will delete your data. I hope that they will reconsider this policy in the future, especially if they launch an "Enterprise" version of their service.

## Local Windows desktop computer

In our efforts, Crashplan stuggled with large backups. Instead we ended up using Backblaze, which seemed to work a little better with continuous uploading.

For local storage, in our experience, Windows Backup solution did not work for large drives---it got confused and claimed that the target drive was full when it was not. This might have to do with the version control system; for this amount of data, we were unable to find a storage solution with reliable version control.

### Copying data on Windows

If you prefer a GUI, some people prefer Acronis Disk Backup. I found this software difficult to use given how simple the task was, and so I recommend using the built-in Windows utility robocopy

Always use the command prompt for large amounts of data:

	robocopy D:\William G: /e

Copies the contents of the directory "William" to the base directory of drive G. The option "/e" is essential; without it Windows will mangle everything. Please note that this is a more stable alternative to dragging and dropping, and it appears to be faster than both Windows Explorer and Teracopy

To make a hard drive clone without re-copying old files

	robocopy D:\William\orig G:\William\clone /e /z /mir /W:1 /R:2 /XF "G:\.bzvol"

/mir is the scary flag that deletes files from the destination if they are not on the source. 
/e preserves the directory structure and copies empty folders
/z ensures that the copy can be restarted in case of an interruption. 
/W:1 ensures that the copy doesn't pause for too long when it encounters a nasty hidden windows file
/R:2 makes sure that it only attempts the nasty files twice.
/XF excludes the following file, in this case the backblaze log file (Backblaze explodes if you clone the .bzvol file).
/log:C:\William\Desktop\robolog.txt will export the terminal status updates to a text file on your desktop instead of printing them
Note: MIR can't tell if a file was renamed, sometimes it will just re-copy the entire directory.

**Watch which directory you list as the source and the destination, if you mess this up then problems will occur**

*Note: if you run a copy and there are files in the source which were moved to the Recycle Bin, for some reason these files will get copied over as well. Empty the Recycling Bin before initiating a transfer in order to prevent this from happening.*

### Verify the backup

After the first backup (and every so often afterwards), it is a good idea to check the backup to make sure that it is happening correctly. Right now I just spot-check files, but a much smarter method would involve selecting random files (or even entire directories) and comparing their md5 hashes. We have a buggy script that does this step, but it's not reliable enough to share yet.

## My current SOP for data backup

Make a two raw data copies on separate hard drives immediately after doing experiments. Put one in a cabinet and forget about it; use the other one to process and crunch the data. Once the actively-modified one is sufficiently different, consider copying it back over (or, even better, onto a new drive). Use a cloud storage service to backup the active drive.
+ Remember that raw data export is not the slow step.

# Miscellaneous

Things I find helpful to have recorded somewhere, but which I am not currently using

## Set up CrashPlan as a Stanford user

You should be able to use your Stanford Credentials to access [https://su-backup.stanford.edu](https://su-backup.stanford.edu) using the "Single Sign-On" option

Your username is the "XXX" in XXX@stanford.edu, your password should be the same as your Stanford password

The "backup server" address is also `https://su-backup.stanford.edu`

There is a patch for Crashplan that will increase the ambient RAM usage for faster backup. Can also backup other directories than the C: drive by tweaking the "home" path in one of the settings files.


## Links and posts I found useful

https://community.spiceworks.com/topic/209883-robocopy-only-copy-new-changed-files
http://stackoverflow.com/questions/20982968/what-is-robocopys-restartable-option
https://community.spiceworks.com/topic/358653-robocopy-incremental-copy-mir-or-xo-what-s-your-choice

## Tiff compression

Using imagemagick

	convert im1.tif -depth 16 -compress LZW im1_small.tif

For batch compression of tiff files

	mogrify -path output_directory -compress LZW input_directory/*.tif

I need to check whether this preserves 16-bit tiffs or if an additional argument is needed.
To run this on every image in a sub directory, you need to use bash language

	for /D %f in (*) do mogrify -compress LZW %f/*tif

For Unix you might need to use %%f, I haven't tested this though

**IT looks like LZW is not always effective on 16 bit tiffs, it might be easier to either use 8 bit tiffs or ZIP (although I did not find that ZIP reduced file size by a meaningful amount)

Convert 16-bit tiff to 8-bit tiff with imagemagick:

	convert name_of_16bit.tif -depth 8 name_of_8bit.tif

To extract metadata from an image (in order to check whether microscope metadata got corrupted)

	identify -verbose image.tif


## Other backup services

We looked into Google Drive and Amazon Cloud Drive Unlimited before deciding on Backblaze.
