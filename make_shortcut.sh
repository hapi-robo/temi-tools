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

GIT_REPO_NAME="temi-app-shortcut"
VERSION="1.0.0"
APK_FILENAME=$1

# expect 2 arguments


# lower case all letters
# substitute whitespace ' ' with underscore '_'
SHORTCUT_NAME="$(echo $2 | tr '[:upper:]' '[:lower:]' | tr ' ' '_')"
echo "${SHORTCUT_NAME}"

# TEMI_APP_SHORTCUT="temi-app-shortcut"

# check dependencies
echo "Check for dependencies..."
if ! command -v aapt 2>/dev/null; then
	echo "Missing dependencies"
fi

# get package name
# aapt dump badging $1 | grep package:\ name
PACKAGE_NAME="$(aapt dump badging "${APK_FILENAME}" | awk -F "[='|' ]" '/package: / {print $4}')"
echo "${PACKAGE_NAME}"

# get sample
echo "Downloading..."
wget -nv "https://github.com/ray-hrst/${GIT_REPO_NAME}/archive/v${VERSION}.tar.gz"

# decompress
echo "Decompressing..."
tar -xzf "v${VERSION}.tar.gz" 
rm "v${VERSION}.tar.gz"

# enter shortcut source code root directory
cd "${GIT_REPO_NAME}-${VERSION}"
echo "${PWD}"

# rename package
# mv app/src/main/java/com/hapirobo/shortcut "app/src/main/java/com/hapirobo/shortcut_${SHORTCUT_NAME}" 
# mv app/src/androidTest/java/com/hapirobo/shortcut "app/src/androidTest/java/com/hapirobo/shortcut_${SHORTCUT_NAME}" 
# mv app/src/test/java/com/hapirobo/shortcut "app/src/test/java/com/hapirobo/shortcut_${SHORTCUT_NAME}" 

# modify files
app/build.gradle
# echo "package=\"com.hapirobo.shortcut\"" | sed 's/package=\"\(.*\)\"/package=\"com.oung.ray\"/'
cat app/build.gradle | sed 's/shortcut/shortcut_${SHORTCUT_NAME}/'
app/src/main/AndroidManifest.xml


# # build gradle
# ./gradlew build
# cp -v app/build/outputs/apk/debug/app-debug.apk "../${SHORTCUT_NAME}.apk"




# clean up
# echo "Cleaning up..."
# rm -fr "${VERSION}"

# echo "Done"


# ========================================
# REFERENCE
# https://stackoverflow.com/questions/16804093/rename-package-in-android-studio#29092698

# app/src/main/java/com/hapirobo/shortcut
# app/src/androidTest/java/com/hapirobo/shortcut
# app/src/test/java/com/hapirobo/shortcut

# also generated:
# app/build/generated/source/buildConfig/debug/com/hapirobo/shortcut
# app/build/generated/source/buildConfig/androidTest/debug/com/hapirobo/shortcut