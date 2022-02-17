import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(255,255,255)]*360 #black background
client.put_pixels(leds)
def line2(k):
    k
def line(k):
    while k < 360:
        leds[k]=(255,0,0)
        k=k+60
        client.put_pixels(leds)
def slide(k,l):
    while k>l:
        line(k)
        k=k-1
        time.sleep(0.2)
        client.put_pixels(leds)
def pick(k,j,l,h,g): # k is the main led, j is last led, l is first, h and g are already used leds,h1 is the left side of m's used led and g1 is the right side of m's used led
    x=k-1
    y=k+1
    leds[k]=(200,50,250)
    while x>j-1 or y<l+1:
        leds[x]=(255,200,0)
        leds[y]=(255,200,0)
        time.sleep(0.1)
        client.put_pixels(leds)
        x=x-1
        y=y+1
        if x<j+1:
            x=j
        if y>l-1:
            y=l
        if x==h:
            leds[h]=(255,50,200)
            client.put_pixels(leds)
            x=h-1
        if y==g:
            leds[g]=(255,50,200)
            client.put_pixels(leds)
            y=g+1 
        if x==j and y==l:
            break
pick(30,-1,59,-1,-1)
pick(90,59,119,-1,-1)
pick(150,120,180,-1,-1)
pick(210,180,240,-1,-1)
pick(270,240,300,-1,-1)
pick(330,300,360,-1,-1)




