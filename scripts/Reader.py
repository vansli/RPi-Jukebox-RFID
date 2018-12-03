# Forked from Francisco Sahli's https://github.com/fsahli/music-cards/blob/master/Reader.py

import string
#import csv
import os.path
import sys

from evdev import InputDevice, categorize, ecodes, list_devices, ecodes
from select import select
class Reader:

	def is_Keyboard(self, device):
		device_key_list = device.capabilities()[ecodes.EV_KEY]

		if self.mandatory_keys.issubset(device_key_list) and self.reserved_key.isdisjoint(device_key_list):
			return True
		else:
			return False

	def __init__(self):
		path = os.path.dirname(os.path.realpath(__file__))
		self.keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"
		self.mandatory_keys = {i for i in range(ecodes.KEY_ESC, ecodes.KEY_D)}
		self.reserved_key = {0}
		if not os.path.isfile(path + '/deviceName.txt'):
			sys.exit('Please run RegisterDevice.py first')
		else: 
			with open(path + '/deviceName.txt','r') as f:
				deviceName = f.read()
			devices = [InputDevice(fn) for fn in list_devices()]
			for device in devices:
				if device.name == deviceName and self.is_Keyboard(device):
					self.dev = device
					break 		
			try:
				self.dev
			except:
				sys.exit('Could not find the device %s\n. Make sure is connected' % deviceName)
		
	def readCard(self):
		stri=''
		key = ''
		while key != 'KEY_ENTER':
		   r,w,x = select([self.dev], [], [])
		   for event in self.dev.read():
			if event.type==1 and event.value==1:
				stri+=self.keys[ event.code ]
				#print( keys[ event.code ] )
				key = ecodes.KEY[ event.code ]
return stri[:-1]