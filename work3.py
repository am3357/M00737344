import opc
import time
import random

client = opc.Client('localhost:7890')

leds = [(255,255,255)]*360 #black background
client.put_pixels(leds)
