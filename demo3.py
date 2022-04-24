# Hello World for Minecraft Java Edition 1.16.5
# mcje, MCJE: Minecraft Java Edition
from mcje.minecraft import Minecraft
import param_MCJE as param


mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Hello Minecraft Java Edition 1.16.5')

mc.setBlock(1, 2, 2, param.GOLD_BLOCK)