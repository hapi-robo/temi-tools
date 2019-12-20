#!/bin/sh
#
# Returns the APK's package-name
#
# Usage
#	  ./get_package_name.sh <apk>
#
#

# display usage instructions
usage()
{
  echo ""
  echo "usage: get_package_name.sh apk_filename"
  echo ""
  echo "Returns the APK's package-name"
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
