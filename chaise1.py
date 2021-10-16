import maya.cmds as cmds

cmds.file(new=True, force=True)

# definition d'un pied de la chaise
def legs(x, y, z, rotateX, rotateY, rotateZ, leg_name):
    cmds.polyCylinder(n='leg%s' % leg_name, sx=20, sy=10, h=4.5, r=.15)
    cmds.select('leg%s.f[100:119]' % leg_name)
    cmds.move(0, 3, 0, 'leg%s' % leg_name)
    cmds.polyExtrudeFacet( 'leg%s.f[0:19]' % leg_name, kft=True, ltz=.08)
    cmds.polyBevel('leg%s.f[0:19]' % leg_name, offset=0.035)
    cmds.select('leg%s.f[160:179]' % leg_name)
    cmds.scale(0.37,1,1)
    cmds.polyTorus(n = 'knot%s' % leg_name, sr=0.4132, sx=20, sy=20, cuv=1, ch=1)
    cmds.scale(0.162, 0.162, 0.162, 'knot%s' % leg_name)
    cmds.rotate(0,0,90,'knot%s' % leg_name)
    cmds.move(0, 5.13, 0,'knot%s' % leg_name)
    cmds.polyUnite('knot%s' % leg_name, 'leg%s' % leg_name, n='n_leg%s' % leg_name)
    cmds.move(x, y, z)
    cmds.rotate(rotateX, rotateY, rotateZ)

# definition du siege de la chaise
def seat(x, y, z, seat, rotation):
    cmds.polySphere(n = 'sphere%s' % seat, sx=40, sy=15, r=0.95)
    cmds.scale(1.451, 0.214, 1.451, 'sphere%s' % seat)
    cmds.polyTorus(n = 'circlemetal%s' % seat, sr=0.032, sx=30, sy=20, r=0.45, ch=1)
    cmds.scale(3.221, 3.221, 3.221, 'circlemetal%s' % seat)
    cmds.polyUnite('sphere%s' % seat, 'circlemetal%s' % seat, n='full%s' % seat)
    cmds.move(x, y, z)
    cmds.rotate(rotation, 0, 0)

# definition d'un barreau
def barreau(x, y, z, scaleY, name, rotateX = 0, rotateY = 0, rotateZ = 90):
    cmds.polyCylinder(n= name)
    cmds.move(x,y,z)
    cmds.scale(0.142, scaleY, 0.142)
    cmds.rotate(rotateX, rotateY, rotateZ)

def supprimer_histoire():
    cmds.select(all = True)
    cmds.delete(constructionHistory = True)

def ajuster_pivot():
    cmds.move(0, 0, 0,  '.scalePivot', '.rotatePivot', absolute = True)

def etirer(name, longueur, hauteur):
    cmds.select(name)
    cmds.scale(longueur, hauteur, xy = True)


# Creation des pieds de la chaise
legs(-0.25, -0.514, 3.681, -150.546, -0.155, 179.288, 'arriere_droit')
legs(1.843, -0.514, 3.681, -29.455, 0.522, -0.919, 'arriere_gauche')
legs(-0.004, -0.514, 0.491, 149.976, -9.602, 184.291, 'devant_droit')
legs(1.503, -0.514, 0.491, 149.976, -9.602, 184.291, 'devant_gauche')
seat(0.871, 4.142, 1.707, 'siege', 0) # siege de la chaise
seat(0.871, 6.304, 3.155,'dossier',-84.776) # dossier de la chaise
barreau(0.826, 1.102, 2.771, 1.05,'b_arriere') # barreau arriere
barreau(0.826, 1.102, 1.415, 0.76, 'b_devant') # barreau de devant
barreau(0.826, 3.968, 1.161, 1.05, 'sous_siege') # barreau sous le siege
barreau(0.224, 4.846, 3.136, 0.81, 'b_droit', 5.338, -0.146, 3.999) # barreau droit du dossier
barreau(1.436, 4.846, 3.136, 0.81, 'b_gauche',5.338, -0.146, -3.999) # barreau gauche du dossier

#supprimer l'histoire
supprimer_histoire()

# grouper les parties de la chaise
cmds.group('n_legarriere_droit', 'n_legarriere_gauche', 'b_arriere',  'sous_siege', n = 'front_legs')
cmds.group('n_legdevant_droit', 'n_legdevant_gauche', 'b_devant',n = 'back_legs')
cmds.group('b_droit', 'b_gauche', 'fulldossier',n = 'back')
cmds.group('back_legs', 'front_legs', n = 'full_legs')
cmds.group('full_legs', 'back','fullsiege', n = 'chair')
cmds.move(0, 0, 0, 'chair')
ajuster_pivot()

etirer('full_legs', 1, 5)