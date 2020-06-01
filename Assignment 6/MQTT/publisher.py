# PB1 | PB13
# ABHISHEK WAHANE | ATHARVA BARVE
# B1 Batch

# Publisher - To demonstrate MQTT/COAP/XMPP protocols using message broker to subscribe and publish sensor data.

import time
import RPi.GPIO as GPIO
import paho.mqtt.client as paho
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

PinTrigger = 16
PinEcho = 18
#ED = 7

GPIO.setup(PinTrigger, GPIO.OUT)
GPIO.setup(PinEcho, GPIO.IN)
#GPIO.setup(LED, GPIO.OUT)

broker="broker.hivemq.com"

def on_connect(client2,userdata,flags,rc):
        print("Publisher connected with result code" + str(rc))
        time.sleep(2)
        
client2 = paho.Client("client-002")
print("CONNECTING TO BROKER.........",broker)
client2.connect(broker)
client2.on_connect = on_connect

client2.loop_start()


try:
    while 1:
        GPIO.output(PinTrigger, GPIO.LOW)
        #GPIO.output(LED, GPIO.LOW)
        print("Waiting for sensor to configure...")
        time.sleep(2)
        print('Calculating the distance...')
        GPIO.output(PinTrigger, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(PinTrigger, GPIO.LOW)
        while GPIO.input(PinEcho) == 0:
            start_time = time.time()
        while GPIO.input(PinEcho) == 1:
            end_time = time.time()
        duration = end_time - start_time
        distance = round(duration * 17150, 2)
        print("PUBLISHING....")
        client2.publish("Vidya/Khushi",str(distance))
        time.sleep(2)
        
except KeyboardInterrupt:
        client2.loop_stop()
        client2.disconnect()
