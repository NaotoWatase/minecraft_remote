# Hello World for Minecraft Pi Edition
# mcpi, MCPI: Minecraft Pi
from mcpi.minecraft import Minecraft
import param_MCPI as param
from time import sleep

mc = Minecraft.create(address='itkids001.local', port=param.PORT_MC)
mc.postToChat('Hello Minecraft Pi Edition')   

NORMAL = 1000


def sky_island(island_x, island_y, island_z, block_type):
    X, Z = set_position(island_x, island_y, island_z)
    y = set_height(island_x, island_z, X, Z)
    for i in range(island_y):
        z=Z
        for i in range(island_z):
            x=X
            for i in range(island_x):
                blockObj = mc.getBlock(x,y,z)
                #mc.setBlock(x,y,z, param.AIR)
                blockObj = block_change(blockObj, block_type)                
                mc.setBlock(x,y+30,z, blockObj)

                x = x + 1 
            z = z + 1
        y = y + 1


def set_position(island_x, island_y, island_z):
    X, a, Z = mc.player.getPos()
    X = X-(island_x / 2)
    Z = Z-(island_y / 2)
    return X, Z


def set_height(range_x, range_z, X, Z):
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

    y=max_height-12
    return y

def block_change(blockObj, change_block_id):
    if change_block_id == normal:
        pass
    elif blockObj == 8 or blockObj == 9:
        print("yougan")
        blockObj = 11
    elif blockObj == 0:
        pass
    else:
        blockObj = change_block_id
    return blockObj



sky_island(island_x = 10, island_y = 14, island_z = 10, block_type = param.GOLD_BLOCK)

