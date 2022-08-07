# Hello World for Minecraft Pi Edition
# mcpi, MCPI: Minecraft Pi
from mcpi.minecraft import Minecraft
import param_MCPI as param
import time

mc = Minecraft.create(address='itkids001.local', port=param.PORT_MC)
mc.postToChat('Hello Minecraft Pi Edition')   


mc.setBlock(0,0,0, 3)

blockObj = mc.getBlock(0,0,0)
print(blockObj)
if blockObj == 9 or blockObj == 8:
    print("ok")
else:
    print("have a problem") 


