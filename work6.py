import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(255,255,255)]*360 #black background
client.put_pixels(leds)

def less(k):
    for x in range(0,259,-1):
        x=k-1
        leds[x]=(0,0,255)
        client.put_pixels(leds)
less(5)
