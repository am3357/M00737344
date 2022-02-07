import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(0,0,0)]*360 #black background
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

        



