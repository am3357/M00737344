import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(0,0,0)]*360 #black background
client.put_pixels(leds)
def block(k):
    while k <360:
        for led in range(k,k+4):
            leds[led]=(0,0,0)
            client.put_pixels(leds)
            k=k+15
    
def swipe(k):
    while k >-1:
        block(k)
        k=k-1
        time.sleep(0.2)
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

leds[55]=(0,0,255)
leds[115]=(0,0,255)
leds[175]=(0,0,255)
leds[235]=(0,0,255)
leds[355]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

leds[58]=(0,0,255)
leds[118]=(0,0,255)
leds[178]=(0,0,255)
leds[238]=(0,0,255)
leds[358]=(0,0,255)
time.sleep(0.1)
client.put_pixels(leds)

time.sleep(2)
leds = [(0,0,0)]*360
#code up to here plays ADAM!! in LEDs
client.put_pixels(leds)

led = 0
while led<30:
    for row in range(2):
        leds[led+row*60] = (0,255,255)
    for row in range(4,6):
        leds[59-led+row*60] = (0,255,255)
    client.put_pixels(leds)
    time.sleep(0.1)
    led=led+1
while led>29:
    for row in range(2):
        leds[led+row*60]=(255,255,0)
    for row in range(4,6):
        leds[59-led+row*60]=(255,255,0)
    client.put_pixels(leds)
    time.sleep(0.1)
    led=led+1
    if led == 60:
        break
while led>59:
    for row in range(2,3):
        leds[led+row*60] = (255,0,255)
    for row in range(3,4):
        leds[59-led+row*60] = (255,0,255)
    client.put_pixels(leds)
    time.sleep(0.1)
    led=led+1
    if led==120:
        break
leds = [(0,0,0)]*360
#screen change
for led in range(59,-1,-1):
    
        if led<5:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==5:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(119,59,-1):
    
        if led<64:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==66:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==64:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(179,119,-1):
    
        if led<123:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==127:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==123:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(239,179,-1):
    
        if led<182:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==188:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==187:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==186:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==185:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==184:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==183:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==182:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(299,239,-1):
    
        if led<241:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==249:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==241:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(359,299,-1):
    
        if led==300:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==310:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
#A
for led in range(59,12,-1):

        if led<15:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==19:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==18:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==17:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==16:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==15:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(119,72,-1):
    
        if led<75:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==80:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==75:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(179,132,-1):
    
        if led<135:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==141:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==135:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(239,192,-1):
    
        if led<195:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==201:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==195:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(299,252,-1):
    
        if led<255:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==260:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==255:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(359,312,-1):
    
        if led<315:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==319:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==318:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==317:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==316:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==315:
            leds[led]=(125,0,200)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
#D
for led in range(59,23,-1):
    
        if led<31:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==31:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(119,83,-1):
    
        if led<90:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==92:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==90:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(179,143,-1):
    
        if led<149:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==153:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==149:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(239,203,-1):
    
        if led<208:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==214:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==213:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==212:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==211:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==210:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==209:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==208:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(299,263,-1):
    
        if led<267:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==275:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==267:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(359,323,-1):
    
        if led==326:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==336:
            leds[led]=(125,125,50)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
#A
for led in range(59,38,-1):

        if led<41:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==51:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==41:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(119,98,-1):

        if led<101:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==111:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==110:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==101:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==102:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(179,158,-1):

        if led<161:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==171:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==169:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==163:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==161:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(239,218,-1):

        if led<221:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==231:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==228:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==224:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==221:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(299,278,-1):

        if led<281:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==291:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==287:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==285:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==281:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(359,338,-1):

        if led<341:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==351:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==346:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==341:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
#M
for led in range(59,53,-1):
    
        if led<55:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==55:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(119,113,-1):
    
        if led<115:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==115:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(179,173,-1):
    
        if led<175:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==175:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(239,233,-1):
    
        if led<235:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==235:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(299,293,-1):
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(359,353,-1):
    
        if led<355:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==355:
            leds[led]=(125,125,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
#!
for led in range(59,56,-1):
    
        if led<58:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==58:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(119,116,-1):
    
        if led<118:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==118:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(179,176,-1):
    
        if led<178:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==178:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(239,236,-1):
    
        if led<238:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==238:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(299,296,-1):
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
            
            
for led in range(359,356,-1):
    
        if led<358:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==358:
            leds[led]=(190,190,160)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
#!
leds = [(0,0,0)]*360
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
swipe(56)




