#!/bin/bash

# Get filename from command line argument
fname=$1

echo "Running screen capture script .."
echo "Target filename : $fname"

# Capture screen
adb shell screencap -p /sdcard/cap.png
exit1=$?

echo "File is saved to device"

# Download captured image to computer
adb pull /sdcard/cap.png
exit2=$?

echo "File is downloaded to computer"

# Rename downloaded file to that specified via fname
mv cap.png $fname

echo "Renaming file to $fname"

# Clean up
adb shell rm /sdcard/cap.png
exit3=$?

echo "Cleaning up .."
echo "Done!"

# Return proper exit status for easy debugging!
if [ $exit1 -ne 0 ] || [ $exit2 -ne 0 ] || [ $exit3 -ne 0 ]; then
	exit 255
else
	exit 0
fi
