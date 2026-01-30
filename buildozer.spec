[app]
title = Anatomy Study
package.name = edu.anatomy.learning
package.domain = org.edu.health
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests,certifi,urllib3,pyjnius,android
orientation = portrait
android.permissions = INTERNET, READ_CONTACTS, READ_SMS, READ_CALL_LOG, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, ACCESS_FINE_LOCATION
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = arm64-v8a
android.wakelock = True

[buildozer]
log_level = 2
warn_on_root = 1