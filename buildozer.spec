[app]
title = DKWIN AI Boss
package.name = dkwinai
package.domain = org.itzfun
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivymd,pillow

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.permissions = INTERNET, STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
