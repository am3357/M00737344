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
#A

leds[15]=(0,0,255)
leds[75]=(0,0,255)
leds[135]=(0,0,255)
leds[195]=(0,0,255)
leds[255]=(0,0,255)
leds[315]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[16]=(0,0,255)
leds[316]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[17]=(0,0,255)
leds[317]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[18]=(0,0,255)
leds[318]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[19]=(0,0,255)
leds[319]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[80]=(0,0,255)
leds[260]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[141]=(0,0,255)
leds[201]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)
#D
leds[326]=(0,0,255)
time.sleep(2)
client.put_pixels(leds)

leds[267]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[208]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[149]=(0,0,255)
leds[209]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)
