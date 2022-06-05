# Hello World for Minecraft Pi Edition
# mcpi, MCPI: Minecraft Pi
from mcpi.minecraft import Minecraft
import param_MCPI as param
import time

mc = Minecraft.create(address='192.168.1.16', port=param.PORT_MC)
mc.postToChat('Hello Minecraft Pi Edition')




for block in range (3):
    if range == 1:
        block = param.GOLD_BLOCK
    if range == 2:
        block = param.ILON_BLOCK
    if range == 3:
        block = param.DIAMOND_BLOCK
    for r in range (11): 
        mc.setBlocks(
            -x, y, -z,
            x, y, z, block
            )
        x = x + 1
        y = y + 1
        z = z + 1
        N = N + 1
        time.sleep(0.2)

        
