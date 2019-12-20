#!/bin/sh
#
# Automatically creates an APK shortcut for temi's Launcher OS
#
# Usage
#	  ./shortcut.sh <package-name> <shortcut-name>
#
# Dependencies
#   - curl
#   - Android SDK, see: https://www.androidcentral.com/installing-android-sdk-windows-mac-and-linux-tutorial
#
# MIT License
#
# Copyright (c) 2019 Raymond Oung
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#


# constants
DEFAULT_ANDROID_HOME=~/Android/Sdk # default location on Linux
GIT_REPO_NAME="temi-app-shortcut"
VERSION="1.0.2-alpha"

# display usage instructions
usage()
{
  echo ""
  echo "usage: shortcut.sh apk_filename shortcut_name"
  echo ""
  echo "Creates a shortcut for APK file"
  echo ""
  echo "dependencies:"
  echo "  - curl"
  echo "  - Android-SDK with the ANDROID_HOME environment variable"
  echo "    set appropriately."
  echo ""
  echo "positional arguments:"
  echo ""
  echo "  package_name          APK's package name"
  echo "  shortcut_name         Shortcut name; use double-quotes to encapsulate"
  echo "                        a name with whitespace"
  echo ""
  exit
}

# attempt to automatically set ANDROID_HOME environment variable
set_android_home()
{
	echo "ANDROID_HOME environment variable not set. Attempting to set automatically..."
	if [ -d "${DEFAULT_ANDROID_HOME}" ]; then
		export ANDROID_HOME=${DEFAULT_ANDROID_HOME}
		echo "export ANDROID_HOME=${ANDROID_HOME}"
		echo "[Success]"
	else
		echo "[Fail]"
		echo "Android SDK cannot be found. Please set the ANDROID_HOME environment to your Android-SDK's path."
	fi
}

# check path to Android SDK
if env | grep -q "^ANDROID_HOME="; then
	if [ -d "${ANDROID_HOME}" ]; then
		echo "ANDROID_HOME environment variable set to ${ANDROID_HOME}."
	else
		set_android_home
	fi
else
	set_android_home
fi

# check for APK file
if [ -z "$1" ]; then
  echo "Missing package file"
  usage
else
  PACKAGE_NAME=$1
fi

# check for shortcut name
if [ -z "$2" ]; then
  echo "Missing shortcut name"
  usage
else
  SHORTCUT_NAME=$2
fi

# get shortcut-template
echo "Downloading..."
curl -LJO "https://github.com/ray-hrst/${GIT_REPO_NAME}/archive/v${VERSION}.tar.gz"
# wget --no-check-certificate --content-disposition https://github.com/ray-hrst/temi-app-shortcut/archive/v1.0.0.tar.gz

# decompress
echo "Decompressing..."
tar -xzf "${GIT_REPO_NAME}-${VERSION}.tar.gz"
rm "${GIT_REPO_NAME}-${VERSION}.tar.gz"

# enter shortcut source code root directory
cd "${GIT_REPO_NAME}-${VERSION}"

# rename package
# lower case all letters
# substitute whitespace ' ' with underscore '_'
SHORTCUT_PACKAGE_NAME="$(echo ${SHORTCUT_NAME} | tr '[:upper:]' '[:lower:]' | tr ' ' '_')"

# modify files inline (Linux)
sed -i "s/shortcut_template/shortcut_${SHORTCUT_PACKAGE_NAME}/" app/build.gradle
sed -i "s/shortcut_template/shortcut_${SHORTCUT_PACKAGE_NAME}/" app/src/main/AndroidManifest.xml
sed -i "s/shortcut_template/shortcut_${SHORTCUT_PACKAGE_NAME}/" app/src/main/java/com/hapirobo/shortcut_template/MainActivity.java
sed -i "s/shortcut_template/shortcut_${SHORTCUT_PACKAGE_NAME}/" app/src/androidTest/java/com/hapirobo/shortcut_template/ExampleInstrumentedTest.java
sed -i "s/shortcut_template/shortcut_${SHORTCUT_PACKAGE_NAME}/" app/src/test/java/com/hapirobo/shortcut_template/ExampleUnitTest.java
sed -i "s/shortcut_name/${SHORTCUT_NAME}/" app/src/main/res/values/strings.xml
sed -i "s/com.hapirobo.package_name/${PACKAGE_NAME}/" app/src/main/res/values/strings.xml

# modify files inline (macOS?)
# sed -i .bak "s/shortcut_template/shortcut_${SHORTCUT_PACKAGE_NAME}/" app/build.gradle
# sed -i .bak "s/shortcut_template/shortcut_${SHORTCUT_PACKAGE_NAME}/" app/src/main/AndroidManifest.xml
# sed -i .bak "s/shortcut_template/shortcut_${SHORTCUT_PACKAGE_NAME}/" app/src/main/java/com/hapirobo/shortcut_template/MainActivity.java
# sed -i .bak "s/shortcut_template/shortcut_${SHORTCUT_PACKAGE_NAME}/" app/src/androidTest/java/com/hapirobo/shortcut_template/ExampleInstrumentedTest.java
# sed -i .bak "s/shortcut_template/shortcut_${SHORTCUT_PACKAGE_NAME}/" app/src/test/java/com/hapirobo/shortcut_template/ExampleUnitTest.java
# sed -i .bak "s/shortcut_name/${SHORTCUT_NAME}/" app/src/main/res/values/strings.xml
# sed -i .bak "s/com.hapirobo.package_name/${PACKAGE_NAME}/" app/src/main/res/values/strings.xml

# rename directories
mv -v app/src/main/java/com/hapirobo/shortcut_template "app/src/main/java/com/hapirobo/shortcut_${SHORTCUT_PACKAGE_NAME}"
mv -v app/src/androidTest/java/com/hapirobo/shortcut_template "app/src/androidTest/java/com/hapirobo/shortcut_${SHORTCUT_PACKAGE_NAME}"
mv -v app/src/test/java/com/hapirobo/shortcut_template "app/src/test/java/com/hapirobo/shortcut_${SHORTCUT_PACKAGE_NAME}"

# build shortcut-APK
./gradlew clean
./gradlew build

# move shortcut-APK to root directory
cp -v app/build/outputs/apk/debug/app-debug.apk "../${SHORTCUT_PACKAGE_NAME}_shortcut.apk"

# clean up
echo "Cleaning up..."
cd ../
rm -fr "${GIT_REPO_NAME}-${VERSION}"
echo "Done"
