#!/usr/bin/env python

import colorsys
import math
import time

import unicornhat as unicorn


import gpiozero
import time

led = gpiozero.LED(4)

while True:
	led.on()
	time.sleep(1)
	led.off()
	time.sleep(1)
