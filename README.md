# SimpleSleepTimer (SST)
A simple python script and associated bat file which simplifies setting your windows computer to turn off after a given time.

The script is based upon the OS module and the windows CLI shutdown command. The first time the script is executed a .txt file will be created,
it will be used to store the shutdown time as a unix time stamp, this is used to calculate the remaining time till shutdown.
This means the script requires writes permissions.

#### How to use:
Python 3 is required to run this script, download and install it from https://www.python.org/downloads/ if you haven't already.
Now simply execute the .bat file. If you wish to relocate this .bat file, you can right-click and create a shortcut, and then move that.

Available commands will be displayed once you launch the script, but basic use of it is to write the desired time in hours:minutes and then hit enter.
I.E. If you want your computer to shut down after one hour and thirty minutes you'd write 1:30 and then hit enter.

This script should work on any version of windows, it is however only tested on Win10.
