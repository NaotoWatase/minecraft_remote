# Hello World for Minecraft Pi Edition
# mcpi, MCPI: Minecraft Pi
from mcpi.minecraft import Minecraft
import param_MCPI as param

mc = Minecraft.create(address='itkids001.local', port=param.PORT_MC)
mc.postToChat('Hello Minecraft Pi Edition')
mc.setBlocks(-100, -1, -100,  100, -1, 100,  param.GRASS_BLOCK)
mc.setBlocks(-100, 0, -100,  100, 64, 100,  param.AIR)
