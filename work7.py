import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(255,255,255)]*360 #black background
client.put_pixels(leds)

def block(k):
    while k <360:
        for led in range(k,k+4):
            leds[led]=(0,0,0)
            client.put_pixels(leds)
            k=k+15
    
def swipe(k):
    while k >-1:
        block(k)
        k=k-1
        time.sleep(0.5)
        client.put_pixels(leds)
swipe(56)
    
