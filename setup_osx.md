### General notes

Make sure system name is "william" to avoid having weird file name issues when going between computers

Have a folder called "NO_BACKUP" that is excluded from both Time Machine and Backblaze. This is good for temporary/placeholder files that you don't want to devote resources to backing up. Consider doing this with the Downloads folder as well.

Do not use any software from [here](https://www.reddit.com/r/piracy/wiki/guides)

### Programs List

Homebrew -- Install this first to get command-line download of many important packages

KeepingYouAwake -- useful utility for preventing computer from sleeping.

Backblaze

Miniconda

XCode + Command Line Utilities

Prey

TeX / MacTeX

Sublime Text 3

Fiji / ImageJ
+ [Save As Movie plugin](https://sites.google.com/site/qingzongtseng/save-as-movie)

Unarchiver
+ Nice general-purpose GUI utility for opening files

Install the google cloud SDK
+ watch out for the `.bash_profile` and `.bash_rc`, these likely need to be checked individually

#### command line utilities:
homebrew
ffmpeg
imagemagick
[istats command line gem](http://chris911.github.io/iStats/)
unrar (opens rar files)
sox (working with audio files, making spectrograms)





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


