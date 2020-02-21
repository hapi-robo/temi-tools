#!/bin/sh
#
# Captures a screenshot from the device
#
# usage: screenshot.sh <ip-address>
#
# positional arguments:
#
#   ip-address             Device's IP address
#
#

# SCRIPT_DIR=`dirname "$0"`
SDK_PATH="/home/ray/Android/Sdk/"
CURRENT_TIME=$(date "+%Y%m%d_%H%M%S")


# display usage instructions
usage()
{
  echo ""
  echo "usage: screenshot.sh <ip-address>"
  echo ""
  echo "Captures a screenshot from the device."
  echo ""
  echo "positional arguments:"
  echo ""
  echo "  ip-address             Device's IP address"
  echo ""
  exit 1
}

# check for device's IP address
if [ "$#" -ne 1 ]; then
  echo "Incorrect number of arguments" >&2
  usage
fi

# if ! [ -e "$1" ]; then
#   echo "$1 not found" >&2
#   usage
# fi

# if path does not exist, generate a new virtual environment
if [ ! -d "${SDK_PATH}" ]; then
    echo "Path not found"
fi

# connect to device
"${SDK_PATH}"/platform-tools/adb connect $1

# run monkeyscript
"${SDK_PATH}"/tools/bin/monkeyrunner screenshot.py

# disconnect from device
"${SDK_PATH}"/platform-tools/adb disconnect

# change filename
mv out.png ${CURRENT_TIME}.png

# done
echo ${CURRENT_TIME}.png