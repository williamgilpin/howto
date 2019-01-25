### General notes

Make sure system name is "william" to avoid having weird file name issues when going between computers

Have a folder called "NO_BACKUP" that is excluded from both Time Machine and Backblaze. This is good for temporary/placeholder files that you don't want to devote resources to backing up. Consider doing this with the Downloads folder as well.

Do not use any software from [here](https://www.reddit.com/r/piracy/wiki/guides)

### Programs List

The Unarchiver (RAR and other file unzipper)

Details of my installed programs and applications, as well as any special hacks, in the event I ever lose my system.

Homebrew -- Install this first to get command-line download of many important packages

KeepingYouAwake -- useful utility for preventing computer from sleeping.

Backblaze -- My preferred option for hard drive backup, although Crashplan is an alternative. In the future, I'll use whichever one has more flexible options for external hard drives that I anticipate needing to backup only once every few months

Miniconda

XCode + Command Line Utilities

Prey

TeX / MacTeX

Transmission

Sublime Text 3

Fiji / ImageJ
+ [Save As Movie plugin](https://sites.google.com/site/qingzongtseng/save-as-movie)

Vox music player
+ Put the ".prefPane" file under `/Users/william/Library/PreferencePanes/VOX Preferences.prefPane` in order to use the media keys
+ Recent versions of this have ads and other weird stuff going on

Unarchiver
+ Nice general-purpose GUI utility for opening files

Backup and Sync (Google)
+ Have the online Google drive program sync with a local folder (for offline backups)
+ Designate a different "notes" folder that automatically gets synchronized with online

Install the google cloud SDK
+ watch out for the `.bash_profile` and `.bash_rc`, these likely need to be checked individually

#### command line utilities:
homebrew
ffmpeg
imagemagick
[istats command line gem](http://chris911.github.io/iStats/)
unrar (opens rar files)
sox (working with audio files, making spectrograms)



### Chrome

#### Plugins/Extensions

eHistory -- selective blacklisting of certain sites in search history, like news websites and other links that I'm unlikely to need to find again. Can also search and delete specific sites (like news and entertainment sites) from history

the Great Suspender -- pause inactive tabs
uBlock Origin -- the current best ad blocker
Tampermonkey -- good for more aggressive popup blocking, but a little bit memory-expensive

Copy All URLs -- allows all current tab names to be saved to the clipboard. can then paste them back in to re-open. very useful for making persistent sessions without relying on Chrome to remember recent tabs that were opened at very different times. One limitation is the preamble that the Great Suspender adds to all urls--it's best to "un-suspend" all tabs before using this extension

Previously:
Ghostery
AdBlock Plus
Flashcontrol (chrome now does this automatically)


## Upgrading from OSX Yosemite to macOS Sierra (10.12.4)

+ Python/Anaconda did not have any problems
+ Terminal settings remained intact
+ Mathematica needed to be updated to a version compatible with new OS
++ Did not need to re-authenticate license, just installed the new version and it worked out of the box

TeX / MacTeX broke
+ TeXshop would open, but would not compile old documents
+ Tried re-downloading and installing a more recent version of MacTeX and everything worked again (no need to uninstall previous)

Mail app broke
+ Old emails that were forwarded to my personal Gmail disappeared from Mail.app. However, they were still present in Gmail's web client, as well as on my iPhone. Interestingly, new emails that were forwarded to my Gmail account appeared normally
+ Try rebuilding the mailbox (takes several hours to re-index). I could not get this to work on Sierra.
+ Try going into Gmail's web client, and using custom searches to find the exact date range of missing emails. Then, "Mark all as Unread". This seems to force Mail.app to acknowledge them and re-download them all as unread messages, which you can then "Mark all as Read" within the app. Spotlight will then take a little while to re-index these messages.


# Programming stuff


Put this in `.bash_profile`


```
export CLICOLOR=1

export LSCOLORS=GxFxCxDxBxegedabagaced
export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
```

Light theme: tomorrow night
Dark theme: tomorrow night eighties



### Change default screenshots location

In terminal,

	defaults write com.apple.screencapture location /Users/william/Desktop/misc 

Or whatever folder you want screenshots to go in
From [here](https://www.laptopmag.com/articles/change-macs-default-screenshot-directory)


