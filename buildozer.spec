[app]
title = My Khalid App
package.name = khalidapp
package.domain = org.khalid
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.9.12,hostpython3==3.9.12,kivy==2.2.1,kivymd==1.1.1,pillow==9.4.0

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.ndk = 25b
android.ndk_api = 21
