# Hello World for Minecraft Pi Edition
# mcpi, MCPI: Minecraft Pi
from mcpi.minecraft import Minecraft
import param_MCPI as param
import time

mc = Minecraft.create(address='itkids001.local', port=param.PORT_MC)
mc.postToChat('Hello Minecraft Pi Edition')   

def build(listy, block):
    n = 0
    for i in range (len(listy)):
        m = 0
        for i in range (len(listy[m])):
            x = m
            y = n
            z = 0
            if listy[n][m] == 1:
                mc.setBlock(
                    x, y, z, block
                )       
            m = m + 1
        n = n + 1


locations = [
    [0, 0, 0],
    [1, 0, 0],
    [1, 2, 0],
    [1, 3, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]
]

for location in locations:
    x = location[0]
    y = location[1]
    z = location[2]
    mc.setBlock(
        x, y, z, param.GOLD_BLOCK
    )
    print(location, x, y, z)






