import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(255,255,255)]*360 
client.put_pixels(leds)

led = 0
while led<30:
    for row in range(2):
        leds[led+row*60] = (0,255,0)
    for row in range(4,6):
        leds[59-led+row*60] = (0,255,0)
    client.put_pixels(leds)
    time.sleep(0.1)
    led=led+1
while led>29:
    for row in range(2):
        leds[led+row*60]=(255,0,0)
    for row in range(4,6):
        leds[59-led+row*60]=(255,0,0)
    client.put_pixels(leds)
    time.sleep(0.1)
    led=led+1
    if led == 60:
        break
while led>59:
    for row in range(2,3):
        leds[led+row*60] = (0,0,255)
    for row in range(3,4):
        leds[59-led+row*60] = (0,0,255)
    client.put_pixels(leds)
    time.sleep(0.1)
    led=led+1
    if led==120:
        break
