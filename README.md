# temi Scripts

This repository contains scripts that may be useful when working with [temi](https://www.robotemi.com/).

These scripts have currently been tested on:
* Ubuntu 18.04

## Usage
### package_name.sh
Returns the package name for an APK file.
```
usage: package_name.sh apk_filename

Returns the APK's package-name

dependencies:
  This script depends on having the Android-SDK installed and having the
  the ANDROID_HOME environment variable set appropriately.

positional arguments:

  apk_filename          APK filename (.apk)
```

### shortcut.sh
This script creates an APK (visible on temi's launcher) that launches another APK. This can be used to run APKs that are hidden from temi's launcher.
```
usage: shortcut.sh package_name shortcut_name

Creates a shortcut for APK file

dependencies:
  - curl
  - Android-SDK with the ANDROID_HOME environment variable
    set appropriately.

positional arguments:

  package_name          APK's package name
  shortcut_name         Shortcut name; use double-quotes to encapsulate
                        a name with whitespace
```

### jp_keyboard_config.sh
Configure's Japanese keyboard for temi. 

Connect to a temi robot using ADB, then from a terminal:
```
./jp_keyboard_config.sh
```
