# PB1 | PB13
# ABHISHEK WAHANE | ATHARVA BARVE
# B1 Batch

# To Interface following sensors such as Temperature or Ultrasonic or Gas sensors with Raspberry-Pi/Beagle board/ Arduino etc. and display readings on console.

import sys
import RPi.GPIO as gpi
import Adafruit_DHT as gp1
import time
gpi.setwarning(False)
gpi.setmode(gpi.BCM)
gpi.setup(27, gpi.OUT)
gpi.setup(22, gpi.OUT)

while true:
	hum,temp=gp1.read_retry(11,17)
	if(temp>31):
		print 'temp:{0:0.1f}'.format(temp)
		gpi.output(27, gpi.HIGH)
		time.sleep(1)
	else:
		gpi.output(27, gpi.LOW)
	if(hum > 60):
		print 'hum:{1:0.1f}'.format(hum)
		gpi.output(22, gpi.HIGH)
	else:
		pi.output(22, gpi.LOW) 
