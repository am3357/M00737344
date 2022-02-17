import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(255,255,255)]*360 #black background
client.put_pixels(leds)
def spiral(k):
    leds[k]=(0,255,0)
    client.put_pixels(leds)
    l=k+1
    leds[l]=(255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
    p=l-60
    leds[p]=(255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
    for u in range(p-1,p-3,-1):
        leds[u]=(255,0,0)
        time.sleep(0.1)
        client.put_pixels(leds)
    for y in range(k-1,120+(k-1),+60):
        leds[y]=(255,0,0)
        time.sleep(0.1)
        client.put_pixels(leds)
    for t in range(y+1,y+4):
        leds[t]=(255,0,0)
        time.sleep(0.1)
        client.put_pixels(leds)
    for r in range(t-60,t-60*4,-60):
        leds[r]=(255,0,0)
        time.sleep(0.1)
        client.put_pixels(leds)
    for e in range(r-1,r-4,-1):
        leds[e]=(255,0,0)
        time.sleep(0.1)
        client.put_pixels(leds)
    for w in range(e-1,(60*3)+(k-2),+60):
        leds[w]=(255,0,0)
        time.sleep(0.1)
        client.put_pixels(leds)
    for q in range(w+1,w+6):
        leds[q]=(255,0,0)
        time.sleep(0.1)
        client.put_pixels(leds)
    for a in range(q-60,q-60*6,-60):
        leds[a]=(255,0,0)
        time.sleep(0.1)
        client.put_pixels(leds)
    for z in range(a-1,a-6,-1):
        leds[z]=(255,0,0)
        time.sleep(0.1)
        client.put_pixels(leds)
    for x in range(z-1,(60*3)+(k-3),+60):
        leds[x]=(255,0,0)
        time.sleep(0.1)
        client.put_pixels(leds)
spiral(183)
spiral(193)
spiral(203)
spiral(216)
spiral(226)
spiral(236) 
def rubber(k):
    while k <360:
            leds[k]=(0,0,0)
            client.put_pixels(leds)
            k=k+60
    
def swipe(k):
    while k >-1:
        rubber(k)
        k=k-1
        time.sleep(0.1)
        client.put_pixels(leds)
swipe(59)
    
