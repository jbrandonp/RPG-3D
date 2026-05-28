# scripts/blender/create_wolf_blockout.py
# Squelette quadrupède : structure TOTALEMENT différente d'un humanoïde

import bpy
import math

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# PROPORTIONS LOUP CORROMPU
BODY_LENGTH  = 1.2    # Longueur du corps
BODY_HEIGHT  = 0.45   # Hauteur du dos au sol
BODY_WIDTH   = 0.30   # Largeur du torse
LEG_LENGTH   = 0.50   # Longueur des pattes
HEAD_SIZE    = 0.28   # Tête allongée (museau de loup)

# CORPS (allongé horizontal — axe Z = longueur du corps)
bpy.ops.mesh.primitive_cube_add(
    size=1, location=(0, 0, BODY_HEIGHT + 0.1)
)
body = bpy.context.object
body.name = "wolf_body"
body.scale = (BODY_WIDTH, BODY_LENGTH * 0.6, BODY_HEIGHT * 0.5)
bpy.ops.object.transform_apply(scale=True)

# Cou incliné vers l'avant
bpy.ops.mesh.primitive_cylinder_add(
    vertices=6, radius=0.10, depth=0.30,
    location=(0, BODY_LENGTH * 0.35, BODY_HEIGHT + 0.25)
)
neck = bpy.context.object
neck.name = "wolf_neck"
neck.rotation_euler = (math.radians(40), 0, 0)
bpy.ops.object.transform_apply(rotation=True)

# Tête (museau allongé)
bpy.ops.mesh.primitive_cube_add(
    size=1, location=(0, BODY_LENGTH * 0.5, BODY_HEIGHT + 0.38)
)
head = bpy.context.object
head.name = "wolf_head"
head.scale = (HEAD_SIZE * 0.8, HEAD_SIZE * 1.2, HEAD_SIZE * 0.7)
bpy.ops.object.transform_apply(scale=True)

# Queue
bpy.ops.mesh.primitive_cylinder_add(
    vertices=4, radius=0.05, depth=0.40,
    location=(0, -BODY_LENGTH * 0.45, BODY_HEIGHT + 0.20)
)
tail = bpy.context.object
tail.name = "wolf_tail"
tail.rotation_euler = (math.radians(-40), 0, 0)
bpy.ops.object.transform_apply(rotation=True)

# 4 PATTES (positionnées aux coins du corps)
paw_positions = [
    ("FL", -BODY_WIDTH * 0.45,  BODY_LENGTH * 0.3),  # Front Left
    ("FR",  BODY_WIDTH * 0.45,  BODY_LENGTH * 0.3),  # Front Right
    ("BL", -BODY_WIDTH * 0.45, -BODY_LENGTH * 0.3),  # Back Left
    ("BR",  BODY_WIDTH * 0.45, -BODY_LENGTH * 0.3),  # Back Right
]
for name, x, y in paw_positions:
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=6, radius=0.065,
        depth=LEG_LENGTH * 0.9,
        location=(x, y, BODY_HEIGHT * 0.3)
    )
    bpy.context.object.name = f"wolf_leg_{name}"

# SQUELETTE QUADRUPÈDE
bpy.ops.object.armature_add(location=(0, 0, 0))
armature = bpy.context.object
armature.name = "wolf_armature"
arm_data = armature.data

bpy.ops.object.mode_set(mode='EDIT')
bones = arm_data.edit_bones
for bone in list(bones):
    bones.remove(bone)

def add_bone(name, head, tail, parent_name=None):
    b = bones.new(name)
    b.head = head
    b.tail = tail
    if parent_name:
        b.parent = bones[parent_name]
    return b

# Colonne vertébrale horizontale
add_bone("root",     (0,0,0),                              (0,0,0.05))
add_bone("spine_01", (0, -BODY_LENGTH*0.3, BODY_HEIGHT),   (0, 0,              BODY_HEIGHT+0.05), "root")
add_bone("spine_02", (0, 0,  BODY_HEIGHT+0.05),            (0, BODY_LENGTH*0.3, BODY_HEIGHT),     "spine_01")
add_bone("chest",    (0, BODY_LENGTH*0.3,  BODY_HEIGHT),   (0, BODY_LENGTH*0.4, BODY_HEIGHT+0.1),"spine_02")
add_bone("neck",     (0, BODY_LENGTH*0.4,  BODY_HEIGHT+0.1),(0, BODY_LENGTH*0.5, BODY_HEIGHT+0.3),"chest")
add_bone("head",     (0, BODY_LENGTH*0.5,  BODY_HEIGHT+0.3),(0, BODY_LENGTH*0.65,BODY_HEIGHT+0.35),"neck")
add_bone("jaw",      (0, BODY_LENGTH*0.52, BODY_HEIGHT+0.28),(0,BODY_LENGTH*0.65,BODY_HEIGHT+0.22),"head")

# Queue
add_bone("tail_01",  (0, -BODY_LENGTH*0.35, BODY_HEIGHT),   (0,-BODY_LENGTH*0.5, BODY_HEIGHT+0.1), "spine_01")
add_bone("tail_02",  (0, -BODY_LENGTH*0.5,  BODY_HEIGHT+0.1),(0,-BODY_LENGTH*0.6, BODY_HEIGHT+0.2),"tail_01")

# Pattes avant gauche
add_bone("upper_leg_FL", (-BODY_WIDTH*0.45, BODY_LENGTH*0.3,  BODY_HEIGHT),
                          (-BODY_WIDTH*0.45, BODY_LENGTH*0.28, BODY_HEIGHT*0.5), "chest")
add_bone("lower_leg_FL", (-BODY_WIDTH*0.45, BODY_LENGTH*0.28, BODY_HEIGHT*0.5),
                          (-BODY_WIDTH*0.45, BODY_LENGTH*0.30, 0.05),            "upper_leg_FL")
add_bone("paw_FL",       (-BODY_WIDTH*0.45, BODY_LENGTH*0.30, 0.05),
                          (-BODY_WIDTH*0.45, BODY_LENGTH*0.38, 0),               "lower_leg_FL")

# Patte avant droite (miroir X)
add_bone("upper_leg_FR", (BODY_WIDTH*0.45, BODY_LENGTH*0.3,  BODY_HEIGHT),
                          (BODY_WIDTH*0.45, BODY_LENGTH*0.28, BODY_HEIGHT*0.5), "chest")
add_bone("lower_leg_FR", (BODY_WIDTH*0.45, BODY_LENGTH*0.28, BODY_HEIGHT*0.5),
                          (BODY_WIDTH*0.45, BODY_LENGTH*0.30, 0.05),            "upper_leg_FR")
add_bone("paw_FR",       (BODY_WIDTH*0.45, BODY_LENGTH*0.30, 0.05),
                          (BODY_WIDTH*0.45, BODY_LENGTH*0.38, 0),               "lower_leg_FR")

# Pattes arrière gauche (genou inversé — caractéristique quadrupède)
add_bone("upper_leg_BL", (-BODY_WIDTH*0.45, -BODY_LENGTH*0.3,  BODY_HEIGHT),
                          (-BODY_WIDTH*0.45, -BODY_LENGTH*0.35, BODY_HEIGHT*0.5), "spine_01")
add_bone("lower_leg_BL", (-BODY_WIDTH*0.45, -BODY_LENGTH*0.35, BODY_HEIGHT*0.5),
                          (-BODY_WIDTH*0.45, -BODY_LENGTH*0.28, 0.05),            "upper_leg_BL")
add_bone("paw_BL",       (-BODY_WIDTH*0.45, -BODY_LENGTH*0.28, 0.05),
                          (-BODY_WIDTH*0.45, -BODY_LENGTH*0.38, 0),               "lower_leg_BL")

# Patte arrière droite (miroir X)
add_bone("upper_leg_BR", (BODY_WIDTH*0.45, -BODY_LENGTH*0.3,  BODY_HEIGHT),
                          (BODY_WIDTH*0.45, -BODY_LENGTH*0.35, BODY_HEIGHT*0.5), "spine_01")
add_bone("lower_leg_BR", (BODY_WIDTH*0.45, -BODY_LENGTH*0.35, BODY_HEIGHT*0.5),
                          (BODY_WIDTH*0.45, -BODY_LENGTH*0.28, 0.05),            "upper_leg_BR")
add_bone("paw_BR",       (BODY_WIDTH*0.45, -BODY_LENGTH*0.28, 0.05),
                          (BODY_WIDTH*0.45, -BODY_LENGTH*0.38, 0),               "lower_leg_BR")

bpy.ops.object.mode_set(mode='OBJECT')

total_bones = len(arm_data.bones)
print(f"\n✅ LOUP CORROMPU BLOCKOUT CRÉÉ")
print(f"   Os total    : {total_bones}/25 (limite mobs quadrupèdes)")
print(f"   Corps       : {BODY_LENGTH}m × {BODY_HEIGHT}m")
print(f"   ⚠️  Genoux arrière INVERSÉS (normal pour quadrupède)")
print(f"\n⚠️  PROCHAINE ÉTAPE : Retopologie manuelle")
print(f"   Objectif    : < 1500 triangles final")
print(f"   Guide       : assets_sources/characters/wolf_corrupted/WOLF_GUIDE.md")
