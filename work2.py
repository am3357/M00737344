import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(0,0,0)]*360 #white background
client.put_pixels(leds)

for led in range(59,-1,-1):
    
        if led<5:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==5:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(119,59,-1):
    
        if led<64:
            leds[led]=(255,0,0)
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
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(179,119,-1):
    
        if led<123:
            leds[led]=(255,0,0)
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
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(239,179,-1):
    
        if led<182:
            leds[led]=(255,0,0)
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
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(299,239,-1):
    
        if led<241:
            leds[led]=(255,0,0)
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
            leds[led]=(255,0,0)
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
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
#A
for led in range(59,12,-1):

        if led<15:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==19:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==18:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==17:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==16:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==15:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(119,72,-1):
    
        if led<75:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==80:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==75:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(179,132,-1):
    
        if led<135:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==141:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==135:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(239,192,-1):
    
        if led<195:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==201:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==195:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(299,252,-1):
    
        if led<255:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==260:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==255:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(359,312,-1):
    
        if led<315:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==319:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==318:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==317:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==316:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==315:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
#D
for led in range(59,23,-1):
    
        if led<31:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==31:
            leds[led]=(0,255,0)
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
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==90:
            leds[led]=(0,255,0)
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
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==149:
            leds[led]=(0,255,0)
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
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==213:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==212:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==211:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==210:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==209:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==208:
            leds[led]=(0,255,0)
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
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==267:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(359,323,-1):
    
        if led==326:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==336:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
#A
for led in range(59,38,-1):

        if led<41:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==51:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==41:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(119,98,-1):

        if led<101:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==111:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==110:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==101:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==102:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(179,158,-1):

        if led<161:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==171:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==169:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==163:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==161:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(239,218,-1):

        if led<221:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==231:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==228:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==224:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==221:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(299,278,-1):

        if led<281:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==291:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==287:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==285:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==281:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(359,338,-1):

        if led<341:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==351:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==346:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==341:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
#M
for led in range(59,52,-1):
    
        if led<54:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==54:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(119,112,-1):
    
        if led<114:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==114:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(179,172,-1):
    
        if led<174:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==174:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(239,232,-1):
    
        if led<234:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==234:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(299,292,-1):
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(359,352,-1):
    
        if led<354:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==354:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(255,0,0)
            client.put_pixels(leds)
            time.sleep(0.01)
#!
for led in range(59,55,-1):
    
        if led<57:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==57:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(119,115,-1):
    
        if led<117:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==117:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(179,175,-1):
    
        if led<177:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==177:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(239,235,-1):
    
        if led<237:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==237:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(299,295,-1):
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
for led in range(359,355,-1):
    
        if led<357:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
        elif led==357:
            leds[led]=(0,255,0)
            client.put_pixels(leds)
            time.sleep(0.01)
        else:
            leds[led]=(0,0,255)
            client.put_pixels(leds)
            time.sleep(0.01)
    

    

