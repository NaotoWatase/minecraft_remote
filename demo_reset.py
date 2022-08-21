# Hello World for Minecraft Java Edition 1.12.2 or earlier
from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
import time,math

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Hello Minecraft Java Edition 1.12.2')




mc.setBlocks(-100, -1, -100,  100, -1, 100,  param.GRASS_BLOCK)
mc.setBlocks(-100, 0, -100,  100, 64, 100,  param.AIR)
