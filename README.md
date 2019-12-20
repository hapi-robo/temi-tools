# temi Scripts

This repository contains scripts that may be useful when working with [temi](https://www.robotemi.com/).


## Usage
### package_name.sh
Returns the package name for an APK file. To be used with `shortcut.sh`
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
usage: shortcut.sh apk_filename shortcut_name

Creates a shortcut for APK file

dependencies:
  This script depends on having the Android-SDK installed and having the
  the ANDROID_HOME environment variable set appropriately.

positional arguments:

  package_name          APK's package name
  shortcut_name         Shortcut name; use double-quotes to encapsulate
                        a name with whitespace
```