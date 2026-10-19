[app]

# (str) Title of your application
title = AI Radar Scanner

# (str) Package name
package.name = airadarscanner

# (str) Package domain (needed for android packaging)
package.domain = org.radar

version = 0.1

# (list) Source files to include (let it include python files, png templates, etc.)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,requests,numpy,opencv

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
