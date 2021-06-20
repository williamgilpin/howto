### Installing Xubuntu on an HP Stream 11

I tried this on an HP Stream 11 that was purchased in May 2015. The PC shipped with Windows 8.1

Redditor who succeeded:
https://www.reddit.com/r/Ubuntu/comments/31yy34/hp_stream_11_with_ubuntu_1410/

Ubuntu's instructions suggest using Rufus on an existing Windows computer to prepare the USB stick:
http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-windows
https://help.ubuntu.com/community/Installation/FromUSBStickQuick

Instead of Rufus:
http://www.pendrivelinux.com/universal-usb-installer-easy-as-1-2-3/
http://www.pendrivelinux.com/creating-an-xubuntu-live-usb-from-cd/

Xubuntu distro:
http://xubuntu.org/getxubuntu/

[Esc] then F9 (pick boot) or F10 (set boot order)

http://www8.hp.com/h20195/v2/GetPDF.aspx/c04477191.pdf
http://unix.stackexchange.com/questions/41738/booting-linux-from-usb-using-efi

In the F10 "Boot Settings" menu, Enable LEgacy Boot (this step is crucial). Then you can change the legacy boot order or rstart and select the boot at F9
https://neosmart.net/wiki/enable-legacy-boot-mode/


# Booting from Live USB fails due to BusyBox v1.18.5 (Ubuntu 1:1.18.5-1ubuntu4) built-in shell (ash)
Enter 'help' for a list of built-in commands.

**Note: I ended up asking a friend to use "Startup Disk Creator" on his Ubuntu system (with an Xubuntu i386 disk image) and it worked just fine. Below are some of the other things I attempted.**

Suggestions:
http://www.proposedsolution.com/solutions/ubuntu-booting-to-initramfs-prompt/

Start an elevated command prompt:
http://pcsupport.about.com/od/commandlinereference/f/elevated-command-prompt.htm

check the disk by running:

	chkdsk c: /f

You might have to restart windows and have it run the check when booting