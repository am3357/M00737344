import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(255,255,255)]*360 #white background
client.put_pixels(leds)

for led in range(59,5,-1):
        leds[led]=(0,0,255)
        leds[led-1]=(0,255,0)
        if led ==5:
            for led in range(4,0,-1):
             leds[led]=(0,0,255)   
        client.put_pixels(leds)
        time.sleep(0.02)
