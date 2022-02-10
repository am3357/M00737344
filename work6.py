import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(255,255,255)]*360 #black background
client.put_pixels(leds)

def pick(k,j,l,h,g): # k is the main led, j is last led, l is first, h and g are already used leds,h1 is the left side of m's used led and g1 is the right side of m's used led
    x=k-1
    y=k+1
    leds[k]=(255,95,0)
    while x>j-1 or y<l+1:
        leds[x]=(0,200,255)
        leds[y]=(0,200,255)
        time.sleep(0.1)
        client.put_pixels(leds)
        x=x-1
        y=y+1
        if x<j+1:
            x=j
        if y>l-1:
            y=l
        if x==h:
            leds[h]=(255,95,0)
            client.put_pixels(leds)
            x=h-1
        if y==g:
            leds[g]=(255,95,0)
            client.put_pixels(leds)
            y=g+1 
        if x==j and y==l:
            break
pick(7,0,15,-1,-1)
pick(66,60,75,-1,68)
pick(125,120,135,-1,129)
pick(184,180,195,-1,190)
leds[185]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
leds[186]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
leds[187]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
leds[188]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
leds[189]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
pick(243,240,255,-1,251)
pick(302,300,315,-1,312)
#A
pick(17,15,26,-1,-1)
leds[18]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
leds[19]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
leds[20]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
leds[21]=(255,95,0)
time.sleep(0.1)
pick(77,75,86,-1,82)
pick(137,135,146,-1,143)
pick(197,195,206,-1,203)
pick(257,255,266,-1,262)
pick(317,315,326,-1,321)
leds[318]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
leds[319]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
leds[320]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)

#D
pick(33,25,41,-1,-1)
pick(92,85,101,-1,94)
pick(151,145,161,-1,155)
pick(210,205,221,-1,216)
leds[211]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
leds[212]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
leds[213]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
leds[214]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
leds[215]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
pick(269,265,281,-1,277)
pick(328,325,341,-1,338)
#A
pick(53,40,55,43,-1)
pick(113,100,115,103,-1)
leds[112]=(255,95,0)
leds[104]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
pick(173,160,175,163,-1)
leds[171]=(255,95,0)
leds[165]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
pick(233,220,235,223,-1)
leds[230]=(255,95,0)
leds[226]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
pick(293,280,295,283,-1)
leds[289]=(255,95,0)
leds[287]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
pick(353,340,355,343,-1)
leds[348]=(255,95,0)
time.sleep(0.1)
client.put_pixels(leds)
#M
def eraser(k):
    x=55
    leds[x]=(255,255,255)
eraser(55)
