# Hello World for Minecraft Pi Edition
# mcpi, MCPI: Minecraft Pi
from mcpi.minecraft import Minecraft
import param_MCPI as param
import time

mc = Minecraft.create(address='itkids001.local', port=param.PORT_MC)
mc.postToChat('Hello Minecraft Pi Edition')   



def art(block, eath, size, X, Y, Z):
    x = X
    y = Y 
    z = Z

    n = 0
    for i in range (size):
        for i in range (eath - 1):
            mc.setBlock(
                x, y, z, block
            )
            mc.setBlock(
                x, y, -z, block
            )
            x = x + 1
            z = z + 1

        for i in range (eath):
            mc.setBlock(
                x, y, z, block
            )
            mc.setBlock(
                x, y, -z, block
            )
            x = x + 1
            z = z - 1
        n = n + 1
        x = X + n
        y = Y + n
        z = Z



art(param.IRON_BLOCK, 20, 20, 20, 0, 0)




