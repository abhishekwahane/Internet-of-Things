# PB1 | PB13
# ABHISHEK WAHANE | ATHARVA BARVE
# B1 Batch

# Subscriber - To demonstrate MQTT/COAP/XMPP protocols using message broker to subscribe and publish sensor data.

import paho.mqtt.client as mymqtt
import time

MQTT_Server="broker.hivemq.com"
MQTT_Topic="Vidya/Khushi"

def on_connect(client,userdata,flags,rc):
        print("Connected with result code" + str(rc))
        client.subscribe(MQTT_Topic)
        
        
def on_message(client,userdata,msg):
    print(msg.topic+' '+str(msg.payload))
    
    
client=mymqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect(MQTT_Server,1883,60) 
client.loop_start()

try:
    while True:
        time.sleep(2)

except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()     
    
