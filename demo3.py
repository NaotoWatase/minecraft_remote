# Hello World for Minecraft Pi Edition
# mcpi, MCPI: Minecraft Pi
from mcpi.minecraft import Minecraft
import param_MCPI as param
import time

mc = Minecraft.create(address='192.168.1.16', port=param.PORT_MC)
mc.postToChat('Hello Minecraft Pi Edition')

N = 0
M = 0
H = 0
S = 0

x = 0
y = 4
z = 0

block_type = 0

while H < 3:
    H = H + 1
    while N < 11:      
        mc.setBlocks(
            -x, y, -z,
            x, y, z, param.GOLD_BLOCK
            )
        x = x + 1
        y = y + 1
        z = z + 1
        N = N + 1
        time.sleep(0.1)
        
