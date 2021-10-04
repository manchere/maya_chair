import maya.cmds as cmds

cmds.polyCube(name ='leg1')
cmds.scale(1, 5, 1, 'leg1')
cmds.move(-2, 3, 1, 'leg1')

cmds.polyCube(name ='leg2')
cmds.scale(1, 5, 1, 'leg2')
cmds.move(2, 3, 1, 'leg2')

cmds.polyCube(name ='leg3')
cmds.scale(1, 5, 1, 'leg3') 
cmds.move(0, 3, 5, 'leg3')

cmds.polyCylinder(name='table1')
cmds.scale(3.154, 0.556, 3.43, 'table1')
cmds.move(0, 5.137, 2.432, 'table1')

cmds.polyCube(name ='back')
cmds.scale(5.963, 6.334, 1, 'back')
cmds.move(0, 8.439,1,'back')
cmds.rotate(-10,0,0)

cmds.polyCube(name ='back2')
cmds.scale(4.552, 4.835, 0.763, 'back2')
cmds.move(0, 8.439,1.5,'back2')
cmds.rotate(-10,0,0)

#cmds.select(back2.f[0])


    
    