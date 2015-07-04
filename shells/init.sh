#!/bin/bash

# open Clash of Clans
adb shell monkey -p com.supercell.clashofclans -c android.intent.category.LAUNCHER 1

# exit script with exit status of adb
exit $?
