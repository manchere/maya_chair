import maya.cmds as cmds
import math
# On ne résout pas un grand problème avec une grosse solution, mais par une armée de petites solutions

long_p = 4.5
haute = 10
LENGTH_FLOOR = 2.478

cmds.file(new=True, force=True)

# definition d'un pied de la chaise
def legs(x, y, z, rotateX, rotateY, rotateZ, leg_name):
    cmds.polyCylinder(n='leg%s' % leg_name, sx=20, sy=10, h=long_p, r=.15)
    cmds.select('leg%s.f[100:119]' % leg_name)
    cmds.polyExtrudeFacet( 'leg%s.f[0:19]' % leg_name, kft=True, ltz=.08)
    cmds.polyBevel('leg%s.f[0:19]' % leg_name, offset=0.035)
    cmds.select('leg%s.f[160:179]' % leg_name)
    cmds.scale(0.37,1,1)
    cmds.polyUnite(chair_ring(leg_name), 'leg%s' % leg_name, n='n_leg%s' % leg_name)
    leg_position(x, y, z, rotateX, rotateY, rotateZ)

# positionement d'un pied
def leg_position(x, y, z, rotateX, rotateY, rotateZ):
    cmds.move(x, y, z)
    cmds.rotate(rotateX, rotateY, rotateZ)

# definition d'un anneau pour un pied
def chair_ring(leg_name):
    cmds.polyTorus(n = 'knot%s' % leg_name, sr=0.4132, sx=20, sy=20, ch=1)
    cmds.scale(0.162, 0.162, 0.162, 'knot%s' % leg_name)
    cmds.rotate(0,0,90,'knot%s' % leg_name)
    cmds.move(0, 2.138, 0,'knot%s' % leg_name)

    return 'knot %s' % leg_name

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

# supprimer l'historique
def supprimer_histo():
    cmds.select(all = True)
    cmds.delete(constructionHistory = True)

# Creation des pieds de la chaise
legs(-1.039, 0, 0, -30, 0, 0, 'arriere_droit')
legs(1.039, 0, 0, -30, 0, 0, 'arriere_gauche')
legs(0.75, 0, -0.43, 30, 0, 0, 'devant_droit')
legs(-0.75, 0, -0.43, 30, 0, 0, 'devant_gauche')

seat(0, 2.075, -0.38, 'siege', 0) # siege de la chaise
seat(0, 4.15, 1,'dossier',-84.776) # dossier de la chaise
barreau(0, -0.92, 0.536, 1.05,'b_arriere') # barreau arriere
barreau(0, -0.92, -0.967, 0.76, 'b_devant') # barreau de devant
barreau(0, 1.851, 0.631, 0.7, 'sous_siege') # barreau sous le siege
barreau(-0.6, 2.5, 1, 0.81, 'b_droit', 5, 0, 4) # barreau droit du dossier
barreau(0.6, 2.5, 1, 0.81, 'b_gauche', 5, 0, -4)  # barreau gauche du dossier

# #supprimer l'histoire
supprimer_histo()

# grouper les parties de la chaise

# groupe pied arriere de la chaise
cmds.group('n_legarriere_droit', 'n_legarriere_gauche', 'b_arriere',  'sous_siege', n = 'front_legs')

# groupe pied devant de la chaise
cmds.group('n_legdevant_droit', 'n_legdevant_gauche', 'b_devant',n = 'back_legs')

# groupe dossier/siege de la chaise
cmds.group('b_droit', 'b_gauche', 'fulldossier', 'fullsiege', n = 'back')

# groupe tous les pieds de la chaise
cmds.group('back_legs', 'front_legs', n = 'full_legs')

# groupe toute la chaise
cmds.group('full_legs', 'back', n = 'chair')

def get_height(longueur_pied, angle_prime): # longueur_pieds equivalent a l'hypotenuse
    return longueur_pied * math.cos(math.radians(angle_prime))

height = 3
width = 1
cmds.scale(width, height, 1, 'full_legs')
cmds.scale(width, 1, 1, 'back')
cmds.move(0, get_height(height * long_p, 30) * 0.5, 0, 'full_legs')
cmds.move(0, get_height(height * long_p, 30) * 0.5 + get_height(long_p * height, 30), 0, 'back')
