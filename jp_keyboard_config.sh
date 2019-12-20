#!/bin/sh
#
# Configures temi's Japanese keyboard
#	- Black theme
#	- QWERTY keyboard
#
# Usage
#	Connect to a temi robot using ADB, then from a terminal:
#	./jp_keyboard_config.sh
#
# Dependencies
#   - Android SDK, see: https://www.androidcentral.com/installing-android-sdk-windows-mac-and-linux-tutorial
#

# stop the app process and clear out all the stored data
adb shell pm clear com.google.android.inputmethod.japanese

# push custom configurations (attached file)
adb push assets/com.google.android.inputmethod.japanese_preferences.xml /data/data/com.google.android.inputmethod.japanese/shared_prefs/com.google.android.inputmethod.japanese_preferences.xml