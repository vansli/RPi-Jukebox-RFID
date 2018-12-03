#!/usr/bin/python3
# rotary volume knob
# these files belong all together:
# RPi-Jukebox-RFID/scripts/rotary-encoder.py
# RPi-Jukebox-RFID/scripts/ky040.py
# RPi-Jukebox-RFID/misc/sampleconfigs/phoniebox-rotary-encoder.service.stretch-default.sample
# See wiki for more info: https://github.com/MiczFlor/RPi-Jukebox-RFID/wiki

#
# circuit diagram
# (capacitors are optionally)
#
#       .---------------.                      .---------------.
#       |               |                      |               |
#       |           CLK |------o---------------| GPIO 27       |
#       |               |      |               |               |
#       |           DT  |------)----o----------| GPIO 17       |
#       |               |      |    |          |               |
#       |           SW  |------)----)----------| GPIO 22       |
#       |               |      |    |          |               |
#       |           +   |------)----)----------| 3.3V          |
#       |               |      |    |          |               |
#       |           GND |------)----)----------| GND           |
#       |               |      |    |          |               |
#       '---------------'      |    |          '---------------'
#            KY-040            |    |              Raspberry
#                              |    |
#                             ---  ---
#                       100nF ---  --- 100nF
#                              |    |
#                              |    |
#                              |    |
#                             ===  ===
#                             GND  GND
#

import RPi.GPIO as GPIO
from ky040 import KY040
import os, time
from subprocess import check_call


def rotaryChangeCW():
   check_call("./scripts/playout_controls.sh -c=volumeup", shell=True)
def rotaryChangeCCW():
   check_call("./scripts/playout_controls.sh -c=volumedown", shell=True)

def switchPressed():
   check_call("./scripts/playout_controls.sh -c=mute", shell=True)


if __name__ == "__main__":

   CLOCKPIN = 27
   DATAPIN = 17
   SWITCHPIN = 22

   GPIO.setmode(GPIO.BCM)

   ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChangeCW, rotaryChangeCCW, switchPressed)

   ky040.start()

   try:
      while True:
         time.sleep(0.2)
   finally:
      ky040.stop()
      GPIO.cleanup()






