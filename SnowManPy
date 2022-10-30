import maya.cmds as cmds

size = 3

cmds.polySphere(sx = 20, sy = 20, r = (size))
cmds.move(0, size, 0)

cmds.polySphere(sx = 20, sy = 20, r = (size/1.5))
cmds.move(0, (((size * 2) + (size -1)) - (size * 2) / (8)), 0)

cmds.polySphere(sx = 20, sy = 20, r = (size/3))
cmds.move(0, (((size * 3) + (size -1)) - (size * 3) / (8)), 0)

cmds.polyCylinder(sx = 20, sy = 20, h = size, r = (size/3.5))
cmds.move(0, (size * 4), 0)

cmds.polyCylinder(sx = 20, sy = 20, h = (size/2.99), r = (size/1.1))
cmds.scale(.5, .30, .5)
cmds.move(0, ((size * 4) * 0.883), 0)

cmds.polySphere(sx = 20, sy = 20, r = (size/12))
cmds.move(((size / 3)* 0.4), (((size * 3) + (size - 1)) - (size * 3) / 8), ((size / 3) * 0.7))

cmds.polySphere(sx = 20, sy = 20, r = (size/12))
cmds.move(((-size / 3)* 0.4), (((size * 3) + (size - 1)) - (size * 3) / 8), ((size / 3) * 0.7))