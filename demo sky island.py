# Hello World for Minecraft Pi Edition
# mcpi, MCPI: Minecraft Pi
from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
import time


mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Hello Minecraft Pi Edition')   

NORMAL = 1000

ISLAND_X = 15
ISLAND_Y = 15
ISLAND_Z = 15

set_color = [
    (35,0),
    (35,1),
    (35,2),
    (35,3),
    (35,4),
    (35,5),
    (35,6),
    (35,7),
    (35,8),
    (35,9),
    (35,10),
    (35,11),
    (35,12),
    (35,13),
    (35,14),
    (35,15),
    (35,0),
    (35,1),
    (35,2),
    (35,3),
    (35,4),
    (35,5),
    (35,6),
    (35,7),
    (35,8),
    (35,9),
    (35,10),
    (35,11),
    (35,12),
    (35,13),
    (35,14),
    (35,15),
    (35,0),
    (35,1),
    (35,2),
    (35,3),
    (35,4),
    (35,5),
    (35,6),
    (35,7),
    (35,8),
    (35,9),
    (35,10)
]

"""
set_color = [
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK,
    param.GOLD_BLOCK
]
"""


def sky_island(island_x, island_y, island_z, block_type):
    count_y = 0
    X, Z = set_position(island_x, island_y, island_z)
    y = set_height(island_x, island_y, island_z, X, Z)
    for i in range(island_y):
        z=Z
        for i in range(island_z):
            x=X
            for i in range(island_x):
                blockObj = mc.getBlock(x,y,z)
                #mc.setBlock(x,y,z, param.AIR)
                blockObj = block_change(blockObj, block_type, count_y)               
                mc.setBlock(x,y+island_y*1.5,z, blockObj)

                x = x + 1 
            z = z + 1
        y = y + 1
        count_y += 1
    mc.player.setPos(X, 200, Z)
    mc.postToChat('こ...これが..空島..?') 


def set_position(island_x, island_y, island_z):
    X, a, Z = mc.player.getPos()
    X = X-(island_x / 2)
    Z = Z-(island_y / 2)
    return X, Z


def set_height(range_x, range_y, range_z, X, Z):
    z=Z
    height = []
    for i in range(range_z):
        x=X
        for i in range(range_x):
            parts_height = mc.getHeight(x,z)
            height = height + [parts_height]
            x = x + 1 
        z = z + 1

    max_height = max(height)
    print(max_height)

    y=max_height-range_y
    return y

def block_change(blockObj, change_block_id, count_y):
    if change_block_id == NORMAL:
        pass
    elif blockObj == 8 or blockObj == 9:
        print("yougan")
        blockObj = 11
    elif blockObj == 0:
        pass
    else:
        blockObj = set_color[count_y]
    return blockObj

    




sky_island(island_x = ISLAND_X, island_y = ISLAND_Y, island_z = ISLAND_Z, block_type = (35,2))