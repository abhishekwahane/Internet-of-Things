# PB1 | PB13
# ABHISHEK WAHANE | ATHARVA BARVE
# B1 Batch

# To simulate an operation of obstacle detection and notifying it with buzzer or LED. You may additionally modify this to count objects entering the room

import RPi.GPIO as gpio
import time as t

gpio.setmode(gpio.BCM)
gpio.setwarrnings(False)
gpio.setup(23, gpio.IN)
gpio.setup(24,gpio.OUT)

try: 
	t.sleep(2)
	while True:
		if gpio.input(23):
			gpio.output(24,True)
			t.sleep(1)
			gpio.output(24, False)
			print ("Motion is detected")
		t.sleep(0.5)

except:
	gpio.cleanup()

		 

