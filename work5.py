import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(255,255,255)]*360 #black background
client.put_pixels(leds)

def less1(k):
    for x in range(k-1,-1,-1):
        leds[x]=(0,0,255)
        time.sleep(0.01)
        client.put_pixels(leds)
def more1(k):
    for x in range(k+1,60):
        leds[x]=(0,0,255)
        time.sleep(0.01)
        client.put_pixels(leds)
#def exact1(k):
#    less1(k)
#    time.sleep(0.1)
#    more1(k)
#    time.sleep(0.1)
#    client.put_pixels(leds)
#exact1(5)
def exact(k):
    while True:
        less1(k)
        time.sleep(0.01)
        client.put_pixels(leds)
        more1(k)
        time.sleep(0.01)
        client.put_pixels(leds)
exact(30)

