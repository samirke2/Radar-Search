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
source.exclude_dirs = bin, .buildozer, venv, __pycache__, .git, .github

# (list) Application requirements
# تم ضبط المكتبات لتتوافق مع بيئة البناء الناجحة
requirements = python3,kivy==2.3.0,requests,numpy

# (str) Supported orientations
orientation = portrait
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION

android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = False

p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
