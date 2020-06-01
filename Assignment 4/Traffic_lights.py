# PB1 | PB13
# ABHISHEK WAHANE | ATHARVA BARVE
# B1 Batch

# Consider a suitable scenario of traffic signaling considering a crossroad and demonstrate traffic control using Raspberry- Pi/Beagle board/ Arduino etc.

import RPi.GPIO as a
import time 
a.setmode(a.BCM) 
TRIG=5
ECHO=6
a.setup(1,a.OUT)
a.setup(8,a.OUT)
a.setup(TRIG,a.OUT)
a.setup(ECHO,a.IN) 

a.output(TRIG,False) 
time.sleep(2)
a.output(TRIG,True) 
time.sleep(0.00001)
a.output(TRIG,False) 

while a.input(ECHO)==0:
    pulse_start=time.time()
while a.input(ECHO)==1:
    pulse_end=time.time()

pulse_duration=pulse_end-pulse_start
distance=pulse_duration*17150 
distance=round(distance,2) 
print("distance",distance,"cm")

if(distance < 5):
    a.output(1,a.HIGH)
    time.sleep(5)
    a.output(1,a.LOW)
elif(distance > 5):
    a.output(8,a.HIGH)
    time.sleep(5)
    a.output(8,a.LOW)
a.cleanup()
    
    
    
    
    
    
    
    
    
    

