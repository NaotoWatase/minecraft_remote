# Hello World for Minecraft Pi Edition
# mcpi, MCPI: Minecraft Pi
from mcpi.minecraft import Minecraft
import param_MCPI as param
import time

mc = Minecraft.create(address='192.168.1.16', port=param.PORT_MC)
mc.postToChat('Hello Minecraft Pi Edition')

type = 1

scale = 60

limit = 10

x = 0
y = 0
z = 0

listy = []

a = 0
b = 0

if type == 0:
    for i in range (scale):
        listy = listy + [(scale - 1)  - i]
if type == 1:
    for i in range (scale):
        b = b + 1
        listy = listy + [(limit - 1) - a]  
        if limit > b:   
            a = a + 1
        else:
            b = 0
            a = 0

print(listy)

for i in range (scale):
    x = listy[i] 
    y = i
    z = listy[i]
    mc.setBlocks(
        -x, y, -z,
        x, y, z, param.GOLD_BLOCK
    )



