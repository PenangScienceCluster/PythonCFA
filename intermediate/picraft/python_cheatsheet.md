Raspberry Pi + Minecraft Cheatsheet
Learn APIs
# The line written after the “#” symbol will be ignored. This is known as commenting out code.
# You only need to run the lines that are uncommented.
# From: http://www.stuffaboutcode.com/2013/04/minecraft-pi-edition-api-tutorial.html
## Initial calls to load Minecraft modules in Python
	import mcpi.minecraft as minecraft
	import mcpi.block as block
	import time
## Create a connection to Minecraft (Minecraft has to be running!)
	mc = minecraft.Minecraft.create()
## Send a chat message, with a 5 second delay
	mc.postToChat("Hello Minecraft World")
	time.sleep(5)
## Get player position
	playerPos = mc.player.getPos()
## Set player position
	mc.player.setPos(playerPos.x, playerPos.y + 50, playerPos.z)
	mc.postToChat("Dont look down")
	time.sleep(5)
## Trap!
	playerTilePos = mc.player.getTilePos()
	blockBelowPlayerType = mc.getBlock(playerTilePos.x, 	playerTilePos.y - 1, playerTilePos.z)
	mc.setBlock(playerTilePos.x + 1, playerTilePos.y + 1, 	playerTilePos.z, blockBelowPlayerType)
	mc.setBlock(playerTilePos.x, playerTilePos.y + 1, 	playerTilePos.z + 1, blockBelowPlayerType)
	mc.setBlock(playerTilePos.x - 1, playerTilePos.y + 1, 	playerTilePos.z, blockBelowPlayerType)
	mc.setBlock(playerTilePos.x, playerTilePos.y + 1, 	playerTilePos.z - 1, blockBelowPlayerType)
	mc.postToChat("Trapped you")
	time.sleep(5)
## Free!
	mc.setBlock(playerTilePos.x + 1, playerTilePos.y + 1, 	playerTilePos.z, block.AIR)
	mc.postToChat("Be free")
	time.sleep(5)
## Set a big diamond floor!
	mc.setBlocks(playerTilePos.x - 25, playerTilePos.y - 1, 	playerTilePos.z - 25, playerTilePos.x + 25, playerTilePos.y -	1, playerTilePos.z + 25, block.DIAMOND_BLOCK)
	mc.postToChat("Now thats a big diamond floor!")
Boom!
# From: https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi/7
# Note: These commands will not work as shown. You need to modify them to get them working!
# This is a little test to see how much you understand the commands from the previous section.
## Set a TNT block
	tnt = 46
	mc.setBlock(x, y, z, tnt)
## Set a TNT block that will EXPLODE!
	tnt = 46
	mc.setBlock(x, y, z, tnt, 1) 
## Create a big cube of TNT!
	tnt = 46
	mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, tnt, 1)
