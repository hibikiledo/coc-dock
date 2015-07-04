#!/bin/bash

# Terminate Clash of Clans
adb shell am force-stop com.supercell.clashofclans

# return exit code of adb
exit $?
