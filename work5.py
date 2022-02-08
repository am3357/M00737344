import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(255,255,255)]*360 #black background
client.put_pixels(leds)

def less(k):
    for x in range(x>k):
        leds[k]=(0,0,255)
        time.sleep(2)
        client.put_pixels(leds)
less(30)
