# My OSX configuration

Details of my installed programs and applications, as well as any special hacks, in the event I ever lose my system.

KeepingYouAwake -- useful utility for preventing computer from sleeping.

Backblaze -- My preferred option for hard drive backup, although Crashplan is an alternative. In the future, I'll use whichever one has more flexible options for external hard drives that I anticipate needing to backup only once every few months

Miniconda

XCode + Command Line Utilities

Prey

Sublime Text 3

Fiji / ImageJ
+ [Save As Movie plugin](https://sites.google.com/site/qingzongtseng/save-as-movie)



#### command line utilities:
homebrew
ffmpeg
imagemagick



### Chrome

#### Plugins/Extensions

eHistory -- selective blacklisting of certain sites in search history, like news websites and other links that I'm unlikely to need to find again. Can also search and delete specific sites (like news and entertainment sites) from history

the Great Suspender -- pause inactive tabs
uBlock Origin -- the current best ad blocker
Tampermonkey -- good for more aggressive popup blocking, but a little bit memory-expensive
Flashcontrol -- block all flash by default
Copy All URLs -- allows all current tab names to be saved to the clipboard. can then paste them back in to re-open. very useful for making persistent sessions without relying on Chrome to remember recent tabs that were opened at very different times. One limitation is the preamble that the Great Suspender adds to all urls--it's best to "un-suspend" all tabs before using this extension

Previously:
Ghostery
AdBlock Plus


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
