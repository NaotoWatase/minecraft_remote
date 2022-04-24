# Hello World for Minecraft Java Edition 1.16.5
# mcje, MCJE: Minecraft Java Edition
from mcje.minecraft import Minecraft
import param_MCJE as param


mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Hello Minecraft Java Edition 1.16.5')


data = [
  "#  # ### #   #    ##   #   #  ##  ###  #   ### ",
  "#  # #   #   #   #  #  # # # #  # #  # #   #  #",
  "#### ### #   #   #  #  # # # #  # ###  #   #  #",
  "#  # #   #   #   #  #  # # # #  # # #  #   #  #",
  "#  # ### ### ###  ##    # #   ##  #  # ### ### "
]

for y, line in enumerate(data):
  for x, c in enumerate(line):
    if c == "#":
      mc.setBlock(10, 20, 10, param.GOLD_BLOCK)