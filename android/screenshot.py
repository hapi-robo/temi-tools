"""Take screenshots

Usage:
	If there is more than one ADB on your system, you may run into problems.
	Use the ADB that is found in the SDK directory:

		sdk/platform-tools/adb connect 192.168.0.188
	
	Go to the following directory and run monkeyrunner with this script:
		
		sdk/tools/bin/monkeyrunner screenshot.py

Notes:
	Default installation directory for ADB:

		/usr/lib/android-sdk/platform-tools/

"""
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# connects to the current device
device = MonkeyRunner.waitForConnection()

# take screenshot and write to file
device.takeSnapshot().writeToFile('out.png', 'PNG')
