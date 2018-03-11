#!/usr/bin/env python3

import evdev
import os

device = evdev.InputDevice('/dev/input/event5')

quadDown = False
currX = 0
currY = 0
firstX = 0
firstY = 0
gotFirstX = False
gotFirstY = False

dX = 100
dY = 100

for event in device.read_loop():
	if event.type == 1 and event.code == 328 and event.value == 0:
		os.popen("xte 'keydown Super_L' 'keydown s' 'keyup s' 'keyup Super_L'")

	if event.type == 1 and event.code == 335:	# event.value: 0 is a relase, 1 is a tap
		if not quadDown:
			quadDown = True
			gotFirstX = False
			gotFirstY = False
		else:
			quadDown = False

			# xte 'keydown Super_L' 'keydown s' 'keyup s' 'keyup Super_L' ///FOR FULL VIEW

			if dX < abs(currX - firstX) > abs(currY - firstY):
				if currX - firstX > dX:
					os.popen("xte 'keydown Control_L' 'keydown Alt_L' 'key Left' 'keyup Control_L' 'keyup Alt_L'")
				elif firstX - currX > dX:
					os.popen("xte 'keydown Control_L' 'keydown Alt_L' 'key Right' 'keyup Control_L' 'keyup Alt_L'")
			elif dY < abs(currY - firstY) > abs(currX - firstX):
				if currY - firstY > dY:
					os.popen("xte 'keydown Control_L' 'keydown Alt_L' 'key Up' 'keyup Control_L' 'keyup Alt_L'")
				elif firstY - currY > dY:
					os.popen("xte 'keydown Control_L' 'keydown Alt_L' 'key Down' 'keyup Control_L' 'keyup Alt_L'")

	elif quadDown and event.type == 3 and event.code == 0:	#IF X VALUE
		currX = event.value
		if not gotFirstX:
			gotFirstX = True
			firstX = currX
	elif quadDown and event.type == 3 and event.code == 1:	#IF Y VALULE
		currY = event.value
		if not gotFirstY:
			gotFirstY = True
			firstY = currY
