#!/bin/sh
#
# Automatically creates an app shortcut for temi OS
#
# Usage
#	  ./make_shortcut.sh <apk> <shortcut-name>
#
# Reference
# 	How to use AWK: https://www.digitalocean.com/community/tutorials/how-to-use-the-awk-language-to-manipulate-text-in-linux
#
#

# constants
GIT_REPO_NAME="temi-app-shortcut"
VERSION="1.0.0"

# debug
SHORTCUT_NAME="test"

usage ()
{
  echo ''
  echo 'usage: make_shortcut.sh apk_filename shortcut_name'
  echo ''
  echo 'Creates a shortcut for APK file'
  echo ''
  echo 'positional arguments:'
  echo ''
  echo '  apk_filename          APK filename (.apk)'
  echo '  shortcut_name         Shortcut name; use double-quotes to encapsulate'
  echo '                        a name with whitespace'
  echo ''
  exit
}

# # check for APK file
# if [ -z "$1" ]; then
#   echo "Missing APK file"
#   usage
# else
#   APK_FILENAME=$1
# fi

# # check for shortcut name
# if [ -z "$2" ]; then
#   echo "Missing shortcut name"
#   usage
# else
#   SHORTCUT_NAME=$2
# fi

# # check dependencies
# echo "Check for dependencies..."
# if ! command -v aapt 2>/dev/null; then
#   echo "Missing dependencies"
#   exit
# fi

# lower case all letters
# substitute whitespace ' ' with underscore '_'
# SHORTCUT_NAME="$(echo $2 | tr '[:upper:]' '[:lower:]' | tr ' ' '_')"
# echo "${SHORTCUT_NAME}"

# get package name
# aapt dump badging $1 | grep package:\ name
# PACKAGE_NAME="$(aapt dump badging "${APK_FILENAME}" | awk -F "[='|' ]" '/package: / {print $4}')"
# echo "${PACKAGE_NAME}"

# get sample
echo "Downloading..."
curl -LJO "https://github.com/ray-hrst/${GIT_REPO_NAME}/archive/v${VERSION}.tar.gz"
# wget --no-check-certificate --content-disposition https://github.com/ray-hrst/temi-app-shortcut/archive/v1.0.0.tar.gz

# # decompress
# echo "Decompressing..."
tar -xzf "${GIT_REPO_NAME}-${VERSION}.tar.gz"
rm "${GIT_REPO_NAME}-${VERSION}.tar.gz"

# enter shortcut source code root directory
cd "${GIT_REPO_NAME}-${VERSION}"

# rename package
mv -v app/src/main/java/com/hapirobo/shortcut "app/src/main/java/com/hapirobo/shortcut_${SHORTCUT_NAME}"
mv -v app/src/androidTest/java/com/hapirobo/shortcut "app/src/androidTest/java/com/hapirobo/shortcut_${SHORTCUT_NAME}"
mv -v app/src/test/java/com/hapirobo/shortcut "app/src/test/java/com/hapirobo/shortcut_${SHORTCUT_NAME}"

# modify files inline
# echo "package=\"com.hapirobo.shortcut\"" | sed 's/shortcut/shortcut_test/'
sed -i .bak "s/shortcut/shortcut_${SHORTCUT_NAME}/" app/build.gradle
sed -i .bak "s/shortcut/shortcut_${SHORTCUT_NAME}/" app/src/main/AndroidManifest.xml

# # build shortcut APK
# ./gradlew build

# move file to root directory
# cp -v app/build/outputs/apk/debug/app-debug.apk "../${SHORTCUT_NAME}.apk"

# clean up
# echo "Cleaning up..."
# rm -fr "${VERSION}"

echo "Done"


# ========================================
# REFERENCE
# https://stackoverflow.com/questions/16804093/rename-package-in-android-studio#29092698

# app/src/main/java/com/hapirobo/shortcut
# app/src/androidTest/java/com/hapirobo/shortcut
# app/src/test/java/com/hapirobo/shortcut

# also generated:
# app/build/generated/source/buildConfig/debug/com/hapirobo/shortcut
# app/build/generated/source/buildConfig/androidTest/debug/com/hapirobo/shortcut