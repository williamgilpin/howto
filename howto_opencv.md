## Installing OpenCV on OSX Yosemite (with Static Libraries)

Follow the instructions [here](http://blogs.wcode.org/2014/10/howto-install-build-and-use-opencv-macosx-10-10/)
[These](http://shiffman.net/2011/01/23/how-to-build-opencv-static-libraries-mac-os-x/) are also great instructions

## Instructions

Unzip it and add the folders SharedLibs and StaticLibs within the repository

Download opencv from the source website

Install the OSX program CMAKE

In CMAKE:
+ Add the OpenCV repository as the source
+ Add the SharedLibs Folder as the build
+ Click Configure
+ Select Unix-Makefile and hit "okay"


In the red output that appears:
Uncheck BUILD_SHARED_LIBS
Uncheck BUILD_TESTS
For the variable CMAKE_OSX_SYSROOT, add the SDK path (check in Terminal that this folder still exists) “/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.19.sdk”.
Add x86_64 to CMAKE_OSX_ARCHITECTURES, this tells it to compile against the current system
Uncheck WITH_1394
Uncheck WITH_FFMPEG

Now navigate to the StaticLibs folder and make:
$ cd <path/to/your/opencv/staticlibs/folder/>
$ make (This will take awhile)
$ sudo make install


