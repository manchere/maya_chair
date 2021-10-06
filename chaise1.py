import maya.cmds as cmds

def legs(x, y, z, rotateX, rotateY, rotateZ, leg_name):
    cmds.polyCylinder(n= 'leg0%s' % leg_name, sx=20, sy=10, h=4.5, r=.15)
    cmds.select('leg0%s.f[100:119]' % leg_name)
    cmds.move(0, 3 , 0, 'leg0%s' % leg_name)
    cmds.polyExtrudeFacet( 'leg0%s.f[0:19]' % leg_name, kft=True, ltz=.08)
    cmds.polyBevel('leg0%s.f[0:19]' % leg_name, offset=0.035)
    cmds.select('leg0%s.f[160:179]' % leg_name)
    cmds.scale(0.37,1,1)
    cmds.polyTorus(n = 'knot%s' % leg_name, sr=0.4132, sx=20, sy=20, cuv=1, ch=1)
    cmds.scale(0.162, 0.162, 0.162, 'knot%s' % leg_name)
    cmds.rotate(0,0,90,'knot%s' % leg_name)
    cmds.move(0, 5.13, 0,'knot%s' % leg_name)
    cmds.polyUnite('knot%s' % leg_name, 'leg0%s' % leg_name, n='n_leg0%s' % leg_name)
    cmds.move(x, y, z,'n_leg0%s' % leg_name)
    cmds.rotate(rotateX, rotateY, rotateZ)

def seat(x, y, z, seat, rotation):
    cmds.polySphere(n = 'sphere%s' % seat, sx=40, sy=15, r=0.95)
    cmds.scale(1.451, 0.214, 1.451, 'sphere%s' % seat)
    cmds.polyTorus(n = 'circlemetal%s' % seat, sr=0.032, sx=30, sy=20, r=0.45, ch=1)
    cmds.scale(3.221, 3.221, 3.221, 'circlemetal%s' % seat)
    cmds.polyUnite('sphere%s' % seat, 'circlemetal%s' % seat, n='full%s' % seat)
    cmds.move(x, y, z)
    cmds.rotate(rotation, 0, 0)

def barreau(x, y, z, scaleY, rotateX = 0, rotateY = 0, rotateZ = 90):   
    cmds.polyCylinder()
    cmds.move(x,y,z)
    cmds.scale(0.142, scaleY, 0.142)
    cmds.rotate(rotateX, rotateY, rotateZ)

legs(-0.25, -0.514, 3.681, -150.546, -0.155, 179.288, 'arriere_droit')
legs(1.843, -0.514, 3.681, -29.455, 0.522, -0.919, 'arriere_gauche')
legs(-0.004, -0.514, 0.491, 149.976, -9.602, 184.291, 'devant_droit')
legs(1.503, -0.514, 0.491, 149.976, -9.602, 184.291, 'devant_gauche')
seat(0.871, 4.142, 1.707, 'siege', 0)
seat(0.871, 6.304, 3.155,'dossier',-84.776)

barreau(0.826, 1.102, 2.771, 1.05) # barreau arriere
barreau(0.826, 1.102, 1.415, 0.76) # barreau de devant
barreau(0.826, 3.968, 1.161, 1.05) # barreau sous le siege
barreau(0.224, 4.846, 3.136, 0.81, 5.338, -0.146, 3.999)
barreau(1.436, 4.846, 3.136, 0.81, 5.338, -0.146, -3.999)