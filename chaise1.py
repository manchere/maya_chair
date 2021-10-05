import maya.cmds as cmds

def legs(x, y, z, rotateX, rotateY, rotateZ, leg_num):
    cmds.polyCylinder(n= 'leg0%s' % leg_num, sx=20, sy=10, h=4.5, r=.15)
    cmds.select('leg0%s.f[100:119]' % leg_num)
    cmds.move(0, 3 , 0, 'leg0%s' % leg_num)
    cmds.polyExtrudeFacet( 'leg0%s.f[0:19]' % leg_num, kft=True, ltz=.08)
    cmds.polyBevel( 'leg0%s.f[0:19]' % leg_num, offset=0.035 )
    cmds.select('leg0%s.f[160:179]' % leg_num)
    cmds.scale(0.37,1,1)
    cmds.polyTorus(n = 'knot%s' % leg_num, sr =0.4132, sx=20, sy=20, cuv=1, ch=1)
    cmds.scale(0.062, 0.062, 0.062, 'knot%s' % leg_num)
    cmds.rotate(0,0,90,'knot%s' % leg_num)
    cmds.move(0, 5.13, 0,'knot%s' % leg_num)
    cmds.polyUnite('knot%s' % leg_num, 'leg0%s' % leg_num, n='n_leg0%s' % leg_num)
    cmds.nonLinear(n = 'bend_leg0%s' % leg_num, type='bend', curvature=-10 )
            
    cmds.rotate(0,74,0,'bend_leg0%s' % leg_num)
    cmds.select('n_leg0%s' % leg_num)

        # movement et rotation du pied
        
    cmds.move(x, y, z,'n_leg0%s' % leg_num)
    cmds.rotate(rotateX,rotateY, rotateZ)

def seat(x, y, z, seat, rotation = 90):
    cmds.polySphere(n = seat, sx=40, sy=15, r=.15)
    cmds.scale(1.451, 0.214, 1.451, 'seat')
    cmds.polyTorus(n = 'circlemetal', sr =0.032, sx=30, sy=20, r= 0.45, ch=1)
    cmds.scale(3.221, 3.221, 3.221, 'circlemetal')
    cmds.polyUnite(seat, 'circlemetal', n='full%s' % seat)
    cmds.move(x, y, z)
    
legs(-0.25, -0.514, 3.934, -150.546, -0.155, 179.288, 'arriere_droit')
legs(1.843, -0.514, 3.934, -29.455, 0.522, -0.919, 'arriere_gauche')
legs(-0.281, -0.514, -2.121, 149.976, -9.602, 184.291, 'devant_droit')
legs(1.843, -0.514, 3.934, -29.455, 0.522, -0.919, 'devant_gauche')
seat(0.871, 4.142, 0.823)
    
