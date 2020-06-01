# PB1 | PB13
# ABHISHEK WAHANE | ATHARVA BARVE
# B1 Batch

# To sense the data from sensors and send it to cloud system in simple text files, excel sheets or databases system


import sys
import urllib2
from time import sleep
import Adafruit_DHT as dht


myAPI = '14WBRBZAWNENS39O'
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

def DHT11_data(): 
    humi, temp = dht.read_retry(dht.DHT11, 23)
    print ('H= {}'.format(humi))
    print ('T={}'.format(temp))
    return humi, temp

while True:
    try:
        humi, temp = DHT11_data()
        if isinstance(humi, float) and isinstance(temp, float):
            humi = '%.2f' % humi
            temp = '%.2f' % temp
            conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s' % (temp, humi))
            print conn.read()
            conn.close()
        else:
            print ('Error')
#    sleep(20)
    except:
        break
