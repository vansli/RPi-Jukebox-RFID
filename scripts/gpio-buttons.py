#!/usr/bin/python3
from gpiozero import Button
from signal import pause
from subprocess import check_call

# 2018-10-31
# Added the function on holding volume + - buttons to change the volume in 0.3s interval
#
# 2018-10-15
# this script has the `pull_up=True` for all pins. See the following link for additional info: 
# https://github.com/MiczFlor/RPi-Jukebox-RFID/issues/259#issuecomment-430007446
#
# 2017-12-12
# This script was copied from the following RPi forum post:
# https://forum-raspberrypi.de/forum/thread/13144-projekt-jukebox4kids-jukebox-fuer-kinder/?postID=312257#post312257
# I have not yet had the time to test is, so I placed it in the misc folder.
# If anybody has ideas or tests or experience regarding this solution, please create pull requests or contact me.

def def_shutdown():
    check_call("./scripts/playout_controls.sh -c=shutdown", shell=True)

def def_mute():
    check_call("./scripts/playout_controls.sh -c=mute", shell=True)

def def_next():
    check_call("./scripts/playout_controls.sh -c=playernext", shell=True)

def def_prev():
    check_call("./scripts/playout_controls.sh -c=playerprev", shell=True)

def def_halt():
    check_call("./scripts/playout_controls.sh -c=playerpause", shell=True)

shut = Button(3, hold_time=2)
mute = Button(22,pull_up=True)

next = Button(9,pull_up=True)
prev = Button(8,pull_up=True)
halt = Button(12,pull_up=True)
spare1 = Button(6,pull_up=True)

shut.when_held = def_shutdown
mute.when_pressed = def_mute
next.when_pressed = def_next
prev.when_pressed = def_prev
halt.when_pressed = def_halt

pause()
