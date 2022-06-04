# Hello World for Minecraft Pi Edition
# mcpi, MCPI: Minecraft Pi
from mcpi.minecraft import Minecraft
import param_MCPI as param

mc = Minecraft.create(address='192.168.1.16', port=param.PORT_MC)
mc.postToChat('Hello Minecraft Pi Edition')
mc.setBlocks(-30, -1, -30,  30, -1, 30,  param.GRASS_BLOCK)
mc.setBlocks(-30, 0, -30,  30, 64, 30,  param.AIR)
