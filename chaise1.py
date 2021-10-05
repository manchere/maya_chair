import maya.cmds as cmds

def legs():
    for leg_num in range(2):
        if leg_num % 2 == 0:
            cmds.polyCylinder(n= 'leg0%s' % leg_num, sx=20, sy=10, h=4.5, r=.15)
            cmds.select('leg0%s.f[100:119]' % leg_num)
            #cmds.scale(1.857983, 1.857983, 1.857983)
            cmds.move(-1, 3 , 1, 'leg0%s' % leg_num)
            cmds.polyExtrudeFacet( 'leg0%s.f[0:19]' % leg_num, kft=True, ltz=.08)
            cmds.polyBevel( 'leg0%s.f[0:19]' % leg_num, offset=0.035 )
            cmds.select('leg0%s.f[160:179]' % leg_num)
            cmds.scale(0.37,1,1)
            cmds.polyTorus(n = 'knot%s' % leg_num, sr =0.4132, sx=20, sy=20, cuv=1, ch=1)
            cmds.scale(0.062, 0.062, 0.062, 'knot%s' % leg_num)
            cmds.rotate(0,0,90,'knot%s' % leg_num)
            cmds.move(-1.045, 5.13, 1.002,'knot%s' % leg_num)
            cmds.polyUnite('knot%s' % leg_num, 'leg0%s' % leg_num, n='n_leg0%s' % leg_num)
legs()

    
    