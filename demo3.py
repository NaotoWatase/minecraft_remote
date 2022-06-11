# Hello World for Minecraft Pi Edition
# mcpi, MCPI: Minecraft Pi
from mcpi.minecraft import Minecraft
import param_MCPI as param
import time

mc = Minecraft.create(address='itkids001.local', port=param.PORT_MC)
mc.postToChat('Hello Minecraft Pi Edition')

type = 2
scale = 20
limit = 20
block = param.AIR



listy = []

a = 0
b = 0

if limit < 0:
    abso = -1
else:
    abso = 1

for i in range (scale):
    b = b + abso
    if type == 1:
        listy = listy + [(limit - abso) - a]
    if type == 2:
        listy = listy + [a]
    if abs(limit) > abs(b):   
        a = a + abso
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
        x, y, z, block
    )



