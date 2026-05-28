# scripts/blender/create_goblin_blockout.py
# Lance dans Blender : Scripting → Open → Run Script
# Crée le blockout du Gobelin avec squelette humanoïde simplifié

import bpy
import math

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# PROPORTIONS GOBELIN
# Style "Trappu PS2" : tête = 1/4 de la hauteur (plus grande que humain)
TOTAL_HEIGHT = 1.1
HEAD_SIZE    = TOTAL_HEIGHT / 4      # 0.275m — grosse tête
TORSO_HEIGHT = TOTAL_HEIGHT * 0.30   # 0.33m — torse court et large
LEG_HEIGHT   = TOTAL_HEIGHT * 0.40   # 0.44m — jambes courtes
SHOULDER_WIDTH = 0.42                # Épaules larges pour le style
HIP_WIDTH    = 0.30

# CORPS : même structure qu'Elara mais proportions différentes
# Tête (grosse — style cartoon PS2)
bpy.ops.mesh.primitive_uv_sphere_add(
    segments=6, ring_count=5,
    radius=HEAD_SIZE / 2,
    location=(0, 0, TOTAL_HEIGHT - HEAD_SIZE / 2)
)
bpy.context.object.name = "goblin_head"

# Oreilles pointues (cônes)
for side, x in [("L", -HEAD_SIZE * 0.55), ("R", HEAD_SIZE * 0.55)]:
    bpy.ops.mesh.primitive_cone_add(
        vertices=4, radius1=0.04, depth=0.12,
        location=(x, 0, TOTAL_HEIGHT - HEAD_SIZE * 0.15)
    )
    ear = bpy.context.object
    ear.name = f"goblin_ear_{side}"
    ear.rotation_euler = (0, math.radians(30 if side == "L" else -30), 0)
    bpy.ops.object.transform_apply(rotation=True)

# Torse (trapu et large)
bpy.ops.mesh.primitive_cube_add(
    size=1,
    location=(0, 0, LEG_HEIGHT + TORSO_HEIGHT / 2)
)
torso = bpy.context.object
torso.name = "goblin_torso"
torso.scale = (SHOULDER_WIDTH, 0.25, TORSO_HEIGHT)
bpy.ops.object.transform_apply(scale=True)

# Bassin
bpy.ops.mesh.primitive_cube_add(
    size=1, location=(0, 0, LEG_HEIGHT + 0.05)
)
hip = bpy.context.object
hip.name = "goblin_hip"
hip.scale = (HIP_WIDTH, 0.22, 0.18)
bpy.ops.object.transform_apply(scale=True)

# Jambes courtes et trapues
for side, x in [("L", -HIP_WIDTH/2 + 0.065), ("R", HIP_WIDTH/2 - 0.065)]:
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=6, radius=0.08,
        depth=LEG_HEIGHT * 0.50,
        location=(x, 0, LEG_HEIGHT * 0.65)
    )
    bpy.context.object.name = f"goblin_leg_{side}"

# Bras longs (caractéristique gobelin)
for side, x, rot in [("L", -SHOULDER_WIDTH/2 - 0.05, 12),
                      ("R",  SHOULDER_WIDTH/2 + 0.05, -12)]:
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=6, radius=0.05,
        depth=TORSO_HEIGHT * 1.1,  # Bras plus longs que le torse
        location=(x, 0, LEG_HEIGHT + TORSO_HEIGHT * 0.55)
    )
    arm = bpy.context.object
    arm.name = f"goblin_arm_{side}"
    arm.rotation_euler = (0, math.radians(rot), 0)
    bpy.ops.object.transform_apply(rotation=True)

# SQUELETTE (même structure qu'Elara, 25 os max)
bpy.ops.object.armature_add(location=(0, 0, 0))
armature = bpy.context.object
armature.name = "goblin_armature"
arm_data = armature.data
arm_data.name = "goblin_rig"

bpy.ops.object.mode_set(mode='EDIT')
bones = arm_data.edit_bones
for bone in list(bones):
    bones.remove(bone)

# Os principaux (structure identique à Elara, proportions goblins)
def add_bone(name, head, tail, parent_name=None):
    b = bones.new(name)
    b.head = head
    b.tail = tail
    if parent_name:
        b.parent = bones[parent_name]
    return b

add_bone("root",    (0,0,0),                    (0,0,0.08))
add_bone("pelvis",  (0,0,LEG_HEIGHT),            (0,0,LEG_HEIGHT+0.12),      "root")
add_bone("spine",   (0,0,LEG_HEIGHT+0.12),       (0,0,LEG_HEIGHT+TORSO_HEIGHT*0.5), "pelvis")
add_bone("chest",   (0,0,LEG_HEIGHT+TORSO_HEIGHT*0.5),
                    (0,0,LEG_HEIGHT+TORSO_HEIGHT),  "spine")
add_bone("neck",    (0,0,TOTAL_HEIGHT-HEAD_SIZE), (0,0,TOTAL_HEIGHT-HEAD_SIZE*0.4), "chest")
add_bone("head",    (0,0,TOTAL_HEIGHT-HEAD_SIZE*0.4), (0,0,TOTAL_HEIGHT+0.04), "neck")

# Bras gauche
add_bone("shoulder_L", (-SHOULDER_WIDTH*0.3, 0, TOTAL_HEIGHT-HEAD_SIZE-0.04),
                        (-SHOULDER_WIDTH/2,   0, TOTAL_HEIGHT-HEAD_SIZE-0.09), "chest")
add_bone("upper_arm_L", (-SHOULDER_WIDTH/2, 0, TOTAL_HEIGHT-HEAD_SIZE-0.09),
                         (-SHOULDER_WIDTH/2-0.04, 0, LEG_HEIGHT+TORSO_HEIGHT*0.55), "shoulder_L")
add_bone("forearm_L", (-SHOULDER_WIDTH/2-0.04, 0, LEG_HEIGHT+TORSO_HEIGHT*0.55),
                       (-SHOULDER_WIDTH/2-0.06, 0, LEG_HEIGHT+TORSO_HEIGHT*0.1),  "upper_arm_L")
add_bone("hand_L",    (-SHOULDER_WIDTH/2-0.06, 0, LEG_HEIGHT+TORSO_HEIGHT*0.1),
                       (-SHOULDER_WIDTH/2-0.07, 0, LEG_HEIGHT-0.04),              "forearm_L")

# Bras droit (miroir)
add_bone("shoulder_R", (SHOULDER_WIDTH*0.3, 0, TOTAL_HEIGHT-HEAD_SIZE-0.04),
                        (SHOULDER_WIDTH/2,   0, TOTAL_HEIGHT-HEAD_SIZE-0.09), "chest")
add_bone("upper_arm_R", (SHOULDER_WIDTH/2, 0, TOTAL_HEIGHT-HEAD_SIZE-0.09),
                         (SHOULDER_WIDTH/2+0.04, 0, LEG_HEIGHT+TORSO_HEIGHT*0.55), "shoulder_R")
add_bone("forearm_R", (SHOULDER_WIDTH/2+0.04, 0, LEG_HEIGHT+TORSO_HEIGHT*0.55),
                       (SHOULDER_WIDTH/2+0.06, 0, LEG_HEIGHT+TORSO_HEIGHT*0.1),  "upper_arm_R")
add_bone("hand_R",    (SHOULDER_WIDTH/2+0.06, 0, LEG_HEIGHT+TORSO_HEIGHT*0.1),
                       (SHOULDER_WIDTH/2+0.07, 0, LEG_HEIGHT-0.04),              "forearm_R")

# Jambes
add_bone("thigh_L", (-HIP_WIDTH/2+0.065, 0, LEG_HEIGHT),
                     (-HIP_WIDTH/2+0.05,  0, LEG_HEIGHT*0.5), "pelvis")
add_bone("shin_L",  (-HIP_WIDTH/2+0.05,  0, LEG_HEIGHT*0.5),
                     (-HIP_WIDTH/2+0.04,  0, LEG_HEIGHT*0.08), "thigh_L")
add_bone("foot_L",  (-HIP_WIDTH/2+0.04,  0, LEG_HEIGHT*0.08),
                     (-HIP_WIDTH/2+0.04,  -0.10, 0),           "shin_L")

add_bone("thigh_R", (HIP_WIDTH/2-0.065, 0, LEG_HEIGHT),
                     (HIP_WIDTH/2-0.05,  0, LEG_HEIGHT*0.5), "pelvis")
add_bone("shin_R",  (HIP_WIDTH/2-0.05,  0, LEG_HEIGHT*0.5),
                     (HIP_WIDTH/2-0.04,  0, LEG_HEIGHT*0.08), "thigh_R")
add_bone("foot_R",  (HIP_WIDTH/2-0.04,  0, LEG_HEIGHT*0.08),
                     (HIP_WIDTH/2-0.04,  -0.10, 0),           "shin_R")

bpy.ops.object.mode_set(mode='OBJECT')

total_bones = len(arm_data.bones)
print(f"\n✅ GOBELIN BLOCKOUT CRÉÉ")
print(f"   Os total    : {total_bones}/30 (limite ennemis standards)")
print(f"   Hauteur     : {TOTAL_HEIGHT}m")
print(f"   Tête        : {HEAD_SIZE:.3f}m (1/4 du corps — style cartoon)")
print(f"\n⚠️  PROCHAINE ÉTAPE : Retopologie manuelle")
print(f"   Objectif    : < 1000 triangles final")
print(f"   Guide       : assets_sources/characters/goblin/GOBLIN_GUIDE.md")
