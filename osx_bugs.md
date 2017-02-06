# OSX bugs

A running list of bugs and catches I've encountered with OSX Yosemite

## MATLAB looks fuzzy on a Retina computer

You need to update your Java Runtime Environment.

## Keynote can't save files or export them

Take screenshots and do whatever you can to save your work. If you try closing the file you will get the opportunity to duplicate before discard. Before you discard, try making a new document and copying all your slides into it.

All of you movie links will break for no reason. You need to manually re-import using Inspector, because right-clicking and choosing "replace" will only work for media that you've copied into Photos, which you don't use because it's 2016. If replace keeps failing, try copying your slides manually into a new document.

## Volume suddenly jumps to the right

This seems to happen sometimes when using Flash on Chrome, for some reason the system volume preferences change mysteriously. It can be fixed in System Settings > Sound by dragging the slider back to the middle

## Mission Control / Spaces / hotkeys stop working

In the terminal, type `kilall Dock` to restart the Dock

Answer found on [Stackexchange](http://apple.stackexchange.com/questions/170488/osx-yosemite-mission-control-stopped-working)

## System PReferences says No IP address, but I appear to be connected to the internet

This tends to happen after altering your internal IP address using a command-line tool like ipconfig. The Wifi menu bar icon will show "loading" or error, but you can browse the web normally.

In System Preferences, choose Network > Wifi > Assist Me > Diagnostic

Go through the wizard and it should be able to figure out what's going on.

## External hard drive not ejected properly, and now it won't mount

Connect the drive

	diskutil list

Find the identifier, something like `disk2` probably

	diskutil eject disk2

Now plug it into a different USB port on your computer and it will probably mount.

This advice was taken from [Stackexchange](http://apple.stackexchange.com/questions/243559/sometimes-mac-doesnt-recognise-my-external-hard-drive)

Other advice is to just leave it alone for 15-30 minutes while OSX figures out what's going on. This advice is from [this Stackexchange thread](http://superuser.com/questions/432831/mac-finder-wd-my-passport-wont-mount)

## An external hard drive will not mount, even after proper ejection

I have encountered this issues with Western Digital drives containing Time Machine backups. It may be related to when Spotlight is re-indexing my computer. In terminal, type:

	diskutil list

You should get output that lists all the drives connected the computer. My disk looks something like

	/dev/disk0
	   #:                       TYPE NAME                    SIZE       IDENTIFIER
	   0:      GUID_partition_scheme                        *500.3 GB   disk0
	   1:                        EFI EFI                     209.7 MB   disk0s1
	   2:          Apple_CoreStorage                         499.4 GB   disk0s2
	   3:                 Apple_Boot Recovery HD             650.1 MB   disk0s3
	/dev/disk1
	   #:                       TYPE NAME                    SIZE       IDENTIFIER
	   0:                  Apple_HFS Macintosh HD           *499.1 GB   disk1
	                                 Logical Volume on disk0s2
	/dev/disk2
	   #:                       TYPE NAME                    SIZE       IDENTIFIER
	   0:      GUID_partition_scheme                        *1.0 TB     disk2
	   1:                        EFI EFI                     209.7 MB   disk2s1
	   2:                  Apple_HFS Pawhuska                999.8 GB   disk2s2

If you don't see your hard drive then this won't work. To mount "Pawhuska" above:

	diskutil mount /dev/disk2s2
