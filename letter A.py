import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(255,255,255)]*360 #white background
client.put_pixels(leds)

leds[300]=(0,0,255)
time.sleep(2)
client.put_pixels(leds)

leds[241]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[182]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[123]=(0,0,255)
leds[183]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[64]=(0,0,255)
leds[184]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[5]=(0,0,255)
leds[185]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[66]=(0,0,255)
leds[186]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[127]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[188]=(0,0,255)
leds[187]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[249]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[310]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)






