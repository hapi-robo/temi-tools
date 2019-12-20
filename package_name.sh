#!/bin/sh
#
# Returns the APK's package-name
#
# Usage
#	  ./package_name.sh <apk-filename>
#
# Dependencies
#   - Android SDK, see: https://www.androidcentral.com/installing-android-sdk-windows-mac-and-linux-tutorial
#

# display usage instructions
usage()
{
  echo ""
  echo "usage: package_name.sh apk_filename"
  echo ""
  echo "Returns the APK's package-name"
  echo ""
  echo "dependencies:"
  echo "  This script depends on having the Android-SDK installed and having the"
  echo "  the ANDROID_HOME environment variable set appropriately."
  echo ""
  echo "positional arguments:"
  echo ""
  echo "  apk_filename          APK filename (.apk)"
  echo ""
  exit
}

# check for APK file
if [ -z "$1" ]; then
  echo "Missing APK file"
  usage
else
  APK_FILENAME=$1
fi

# get package name
PACKAGE_NAME="$(aapt dump badging "${APK_FILENAME}" | awk -F "[='|' ]" '/package: / {print $4}')"
echo "${PACKAGE_NAME}"
