#\ -*- coding: utf-8 -*-
import math
import maya.cmds as cmds

class Chair:
    def __init__(self, long_h):
        self.Window = 'Chair'
        self.Height = long_h

        if cmds.window(self.Window, exists=True):
            cmds.delete(self.Window, window=True)

    # definition d'un pied de la chaise
    def legs(self, x, y, z, rotateX, rotateY, rotateZ, leg_name):
        cmds.polyCylinder(n='leg%s' % leg_name, sx=20, sy=10, h=self.Height, r=.15)
        cmds.polyExtrudeFacet( 'leg%s.f[0:19]' % leg_name, kft=True, ltz=.08)
        cmds.polyBevel('leg%s.f[0:19]' % leg_name, offset=0.035)
        cmds.select('leg%s.f[160:179]' % leg_name)
        cmds.scale(0.37,1,1)
        cmds.polyUnite(self.chair_ring(leg_name), 'leg%s' % leg_name, n='n_leg%s' % leg_name)
        self.leg_position(x, y, z, rotateX, rotateY, rotateZ)

    # positionement d'un pied
    def leg_position(self, x, y, z, rotateX, rotateY, rotateZ):
        cmds.move(x, y, z)
        cmds.rotate(rotateX, rotateY, rotateZ)

    # definition d'un anneau pour un pied
    def chair_ring(self, leg_name):
        cmds.polyTorus(n = 'knot%s' % leg_name, sr=0.4132, sx=20, sy=20, ch=1)
        cmds.scale(0.162, 0.162, 0.162, 'knot%s' % leg_name)
        cmds.rotate(0,0,90,'knot%s' % leg_name)
        cmds.move(0, 2.138, 0,'knot%s' % leg_name)

        return 'knot %s' % leg_name

    # definition du siege de la chaise
    def seat(self, x, y, z, sname, rotation):
        cmds.polySphere(n = 'sphere%s' % sname, sx=40, sy=15, r=0.95)
        cmds.scale(1.451, 0.214, 1.451, 'sphere%s' % sname)
        cmds.polyTorus(n = 'circlemetal%s' % sname, sr=0.032, sx=30, sy=20, r=0.45, ch=1)
        cmds.scale(3.221, 3.221, 3.221, 'circlemetal%s' % sname)
        cmds.polyUnite('sphere%s' % sname, 'circlemetal%s' % sname, n='full%s' % sname)
        cmds.move(x, y, z)
        cmds.rotate(rotation, 0, 0)

    # definition d'un barreau
    def barreau(self, x, y, z, scaleY, name, rotateX = 0, rotateY = 0, rotateZ = 90):
        cmds.polyCylinder(n= name)
        cmds.move(x,y,z)
        cmds.scale(0.142, scaleY, 0.142)
        cmds.rotate(rotateX, rotateY, rotateZ)

    # supprimer l'historique
    def supprimer_histo(self):
        cmds.select(all = True)
        cmds.delete(constructionHistory = True)


    def get_height(self, longueur_pied, angle_prime): # longueur_pieds equivalent a l'hypotenuse
        return longueur_pied * math.cos(math.radians(angle_prime))

# -------------------------------------------------------------------------------------------

def create_btn():
    cmds.button(label='creer', command='btn_create_chair()')

def suppr_btn():
    cmds.button(label='supprimer', command="cmds.delete()" )
   
def slider(sld_name, lbl_name):
    return cmds.floatSliderGrp(sld_name, label=lbl_name, field = True, minValue =1.0, maxValue =10.0, value = 1)

def get_slider(sld_name):
    return cmds.floatSliderGrp(sld_name, query=True, value=True)

def option_menu():
    cmds.optionMenu( label='Colors', changeCommand='' )
    cmds.menuItem( label='Yellow' )
    cmds.menuItem( label='Purple' )
    cmds.menuItem( label='Orange' )

# def get_opt_menu():
#     return 

def toggle_long_pied(value):
    cmds.floatSliderGrp('long', edit=True, enable=value)

def pos_legs_vert():
    if get_check_box():
        return [-1.295, 0.54]
    else:
        return [-0.43, 0]

def create_shader(name, node_type="lambert"):
    mtl = cmds.shadingNode(node_type, name=name, asShader=True)
    sg = cmds.sets(name="%sSG" % name, empty=True, renderable=True, noSurfaceShader=True)
    cmds.connectAttr("%s.outColor" % mtl, "%s.surfaceShader" % sg)
    return mtl, sg

def set_color(colors):
    shader_color = colors
    meshes = cmds.ls(selection=True, dag=True, type="mesh", noIntermediate=True)
    material, sgrp = create_shader("siege_MTL", 'blinn')
    cmds.setAttr(material + ".color", shader_color[0], shader_color[1], shader_color[2], type="double3")
    cmds.sets(meshes, forceElement=sgrp)

def is_vertical(val):
    return 0 if val else 30

# def is_checked():
#     if cmds.checkBox()

def get_check_box():
    return cmds.checkBox('verti_check', q=True, v=True)

def btn_create_chair():
    chair = Chair(get_slider('long'))

    chair.legs(-1.039, 0, pos_legs_vert()[1], -(is_vertical(get_check_box())), 0, 0, 'arriere_droit')#neg
    chair.legs(1.039, 0, pos_legs_vert()[1], -(is_vertical(get_check_box())), 0, 0, 'arriere_gauche')
    chair.legs(0.75, 0, pos_legs_vert()[0], is_vertical(get_check_box()), 0, 0, 'devant_droit')#pos
    chair.legs(-0.75, 0, pos_legs_vert()[0], is_vertical(get_check_box()), 0, 0, 'devant_gauche')
    chair.seat(0, 2.075, -0.38, 'siege', 0) # siege de la chaise
    chair.seat(0, 4.15, 1,'dossier',-84.776) # dossier de la chaise
    chair.barreau(0, -0.92,  pos_legs_vert()[1], 1.05,'b_arriere') # barreau arriere 0.536
    chair.barreau(0, -0.92, pos_legs_vert()[0], 0.76, 'b_devant') # barreau de devant -0.967
    chair.barreau(0, 1.851, 0.631, 0.7, 'sous_siege') # barreau sous le siege
    chair.barreau(-0.6, 2.5, 1, 0.81, 'b_droit', 5, 0, 4) # barreau droit du dossier
    chair.barreau(0.6, 2.5, 1, 0.81, 'b_gauche', 5, 0, -4)  # barreau gauche du dossier
    chair.supprimer_histo()
    set_color([0, 23, 2])

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

    # cmds.move('chair', chair.Height/2, -ass/2.5, pied1)
    # cmds.move(Height/2.5, arr/2, ass/2.5, pied2)
    # cmds.move(-Height/2.5, hPiedAvant/2, -ass/2.5, pied3)
    # cmds.move(-Height/2.5, arr/2, ass/2.5, pied4)
    
    # cmds.move(Height/2.5, arr/3, 0, EntrP1)
    # cmds.move(-Height/2.5, arr/3, 0, EntrP2)
    # cmds.move(0, arr/3, ass/2.5, EntrP3)
    # cmds.move(0, arr/3, -ass/2.5, EntrP4)
    
    # cmds.move(0, arr, 0, assise)
    
    # cmds.move(Height/2.5, hPiedAvant, 0, Acc1)
    # cmds.move(-Height/2.5, hPiedAvant, 0, Acc2)
    
    # u = (hDossier/2) * math.sin(math.radians(rxD))
    # cmds.move( 0, arr + hDossier/2, (ass/2.0) + u/2, Dossier)
    
# cmds.move(0, chair.Height + hAssise/2, 0,)

def show_ui():
    my_win = cmds.window(title="Chaise Configuration", widthHeight=(300, 200))
    cmds.columnLayout(adjustableColumn=True)
    suppr_btn()
    slider('large','largeur siege')
    slider('long','longueur pied')
    cmds.checkBox('verti_check', label ='Pied Vertical', changeCommand=toggle_long_pied, value=True)
    option_menu()
    cmds.separator(height = 20)
    create_btn()

    cmds.showWindow(my_win)

show_ui()
