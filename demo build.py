# Hello World for Minecraft Pi Edition
# mcpi, MCPI: Minecraft Pi
from mcpi.minecraft import Minecraft
import param_MCPI as param
import time

mc = Minecraft.create(address='itkids001.local', port=param.PORT_MC)
mc.postToChat('Hello Minecraft Pi Edition')   

def build(listy, block):
    for i in range (len(listy)):
        x = listy[i] 
        y = i
        z = listy[i]
        mc.setBlocks(
            -x, y, -z,
            x, y, z, block
        )

listy = [
    19,
    18,
    18,
    17,
    16,
    15,
    14,
    13,
    12,
    11,
    10,
    9,
    8,
    7,
    6,
    5,
    4,
    3,
    2,
    1,
]


build(listy, block = param.GOLD_BLOCK)

