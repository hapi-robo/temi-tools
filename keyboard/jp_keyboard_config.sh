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

# stop the app process and clear out all the stored data
adb shell pm clear com.google.android.inputmethod.japanese

# push custom configurations (attached file)
adb push com.google.android.inputmethod.japanese_preferences.xml /data/data/com.google.android.inputmethod.japanese/shared_prefs/com.google.android.inputmethod.japanese_preferences.xml