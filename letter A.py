import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(0,0,0)]*360 #white background
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

leds[326]=(0,0,255)
time.sleep(0.1)
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

leds[90]=(0,0,255)
leds[210]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[31]=(0,0,255)
leds[211]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[92]=(0,0,255)
leds[212]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[153]=(0,0,255)
leds[213]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[214]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[275]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[336]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[341]=(0,0,255)
leds[281]=(0,0,255)
leds[221]=(0,0,255)
leds[161]=(0,0,255)
leds[101]=(0,0,255)
leds[41]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[102]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[163]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[224]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[285]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[346]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[287]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[228]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[169]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[110]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[51]=(0,0,255)
leds[111]=(0,0,255)
leds[171]=(0,0,255)
leds[231]=(0,0,255)
leds[291]=(0,0,255)
leds[351]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[54]=(0,0,255)
leds[114]=(0,0,255)
leds[174]=(0,0,255)
leds[234]=(0,0,255)
leds[354]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[57]=(0,0,255)
leds[117]=(0,0,255)
leds[177]=(0,0,255)
leds[237]=(0,0,255)
leds[357]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

#code up to here plays ADAM!! in LEDs

