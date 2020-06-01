# PB1 | PB13
# ABHISHEK WAHANE | ATHARVA BARVE
# B1 Batch

# To interface simple actuators such as stepper motor, relays etc. with Raspberry Pi/ ESP8266 boards / Beagle board/ Arduino Uno.


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

in1 = 14
in2 = 15
temp1 = 1
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

while(1):
    x= input (" r = run \n f = forward \n b = backward \n s = stop ")
    
    if x=='r':
        print("run")
        if(temp1==1):
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            x = 'z'
            print("forward")
        else:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            x = 'z'
            print("backward")
    elif x=='s':
        print("Stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        x='z'
    elif(x=='f'):
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            x = 'z'
            print("forward")
    elif(x=='b'):
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            x = 'z'
            print("backward")
    else:
            print("Enter r/f/b/s!!!")
