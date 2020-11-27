#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
id1 = 0

while True:
	reader = SimpleMFRC522()
	time.sleep(0.1)
	try:
		id, text = reader.read()
		if id != id1:
			print(id)
			print(text)
			id1 = id
	finally:
		GPIO.cleanup()
