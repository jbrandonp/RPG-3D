# scripts/blender/create_elara_blockout.py
# Lance ce script dans Blender : Scripting → Open → Run Script
# Crée le blockout d'Elara Voss avec le squelette de base

import bpy
import math

# === NETTOYAGE DE LA SCÈNE ===
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# === PROPORTIONS ELARA VOSS ===
# Style "Heroic" PS2 : tête = 1/6 de la hauteur totale
# Hauteur totale : 1.7m en unités Blender
TOTAL_HEIGHT = 1.7
HEAD_SIZE = TOTAL_HEIGHT / 6       # 0.283m
TORSO_HEIGHT = TOTAL_HEIGHT * 0.35 # 0.595m
LEG_HEIGHT = TOTAL_HEIGHT * 0.45   # 0.765m
SHOULDER_WIDTH = 0.45
HIP_WIDTH = 0.32

# === CRÉATION DU CORPS (BLOCKOUT) ===

# 1. Tête
bpy.ops.mesh.primitive_uv_sphere_add(
    segments=6, ring_count=6,
    radius=HEAD_SIZE/2,
    location=(0, 0, TOTAL_HEIGHT - HEAD_SIZE/2)
)
head = bpy.context.object
head.name = "elara_head"

# 2. Torse
bpy.ops.mesh.primitive_cube_add(
    size=1,
    location=(0, 0, TOTAL_HEIGHT - HEAD_SIZE - TORSO_HEIGHT/2)
)
torso = bpy.context.object
torso.name = "elara_torso"
torso.scale = (SHOULDER_WIDTH, 0.22, TORSO_HEIGHT)
bpy.ops.object.transform_apply(scale=True)

# 3. Bassin
bpy.ops.mesh.primitive_cube_add(
    size=1,
    location=(0, 0, LEG_HEIGHT + 0.1)
)
hip = bpy.context.object
hip.name = "elara_hip"
hip.scale = (HIP_WIDTH, 0.20, 0.22)
bpy.ops.object.transform_apply(scale=True)

# 4. Jambe gauche
bpy.ops.mesh.primitive_cylinder_add(
    vertices=6, radius=0.07,
    depth=LEG_HEIGHT * 0.55,
    location=(-HIP_WIDTH/2 + 0.07, 0, LEG_HEIGHT * 0.7)
)
leg_l = bpy.context.object
leg_l.name = "elara_leg_L"

# 5. Jambe droite
bpy.ops.mesh.primitive_cylinder_add(
    vertices=6, radius=0.07,
    depth=LEG_HEIGHT * 0.55,
    location=(HIP_WIDTH/2 - 0.07, 0, LEG_HEIGHT * 0.7)
)
leg_r = bpy.context.object
leg_r.name = "elara_leg_R"

# 6. Bras gauche
bpy.ops.mesh.primitive_cylinder_add(
    vertices=6, radius=0.055,
    depth=TORSO_HEIGHT * 0.85,
    location=(-SHOULDER_WIDTH/2 - 0.055, 0,
              TOTAL_HEIGHT - HEAD_SIZE - TORSO_HEIGHT * 0.3)
)
arm_l = bpy.context.object
arm_l.name = "elara_arm_L"
arm_l.rotation_euler = (0, math.radians(15), 0)
bpy.ops.object.transform_apply(rotation=True)

# 7. Bras droit
bpy.ops.mesh.primitive_cylinder_add(
    vertices=6, radius=0.055,
    depth=TORSO_HEIGHT * 0.85,
    location=(SHOULDER_WIDTH/2 + 0.055, 0,
              TOTAL_HEIGHT - HEAD_SIZE - TORSO_HEIGHT * 0.3)
)
arm_r = bpy.context.object
arm_r.name = "elara_arm_R"
arm_r.rotation_euler = (0, math.radians(-15), 0)
bpy.ops.object.transform_apply(rotation=True)

# === CRÉATION DU SQUELETTE (ARMATURE) ===
bpy.ops.object.armature_add(location=(0, 0, 0))
armature = bpy.context.object
armature.name = "elara_armature"
arm_data = armature.data
arm_data.name = "elara_rig"

bpy.ops.object.mode_set(mode='EDIT')
bones = arm_data.edit_bones

# Supprimer l'os par défaut
for bone in bones:
    bones.remove(bone)

# Os racine (Root) — obligatoire à (0,0,0)
root = bones.new("root")
root.head = (0, 0, 0)
root.tail = (0, 0, 0.1)

# Os pelvis
pelvis = bones.new("pelvis")
pelvis.head = (0, 0, LEG_HEIGHT)
pelvis.tail = (0, 0, LEG_HEIGHT + 0.15)
pelvis.parent = root

# Os colonne vertébrale
spine = bones.new("spine")
spine.head = (0, 0, LEG_HEIGHT + 0.15)
spine.tail = (0, 0, LEG_HEIGHT + TORSO_HEIGHT * 0.5)
spine.parent = pelvis

# Os poitrine
chest = bones.new("chest")
chest.head = (0, 0, LEG_HEIGHT + TORSO_HEIGHT * 0.5)
chest.tail = (0, 0, LEG_HEIGHT + TORSO_HEIGHT)
chest.parent = spine

# Os cou
neck = bones.new("neck")
neck.head = (0, 0, TOTAL_HEIGHT - HEAD_SIZE)
neck.tail = (0, 0, TOTAL_HEIGHT - HEAD_SIZE * 0.3)
neck.parent = chest

# Os tête
head_bone = bones.new("head")
head_bone.head = (0, 0, TOTAL_HEIGHT - HEAD_SIZE * 0.3)
head_bone.tail = (0, 0, TOTAL_HEIGHT + 0.05)
head_bone.parent = neck

# Os épaule gauche
shoulder_l = bones.new("shoulder_L")
shoulder_l.head = (-SHOULDER_WIDTH * 0.3, 0, TOTAL_HEIGHT - HEAD_SIZE - 0.05)
shoulder_l.tail = (-SHOULDER_WIDTH/2, 0, TOTAL_HEIGHT - HEAD_SIZE - 0.1)
shoulder_l.parent = chest

# Os bras gauche (upper arm)
upper_arm_l = bones.new("upper_arm_L")
upper_arm_l.head = (-SHOULDER_WIDTH/2, 0, TOTAL_HEIGHT - HEAD_SIZE - 0.1)
upper_arm_l.tail = (-SHOULDER_WIDTH/2 - 0.05, 0,
                     TOTAL_HEIGHT - HEAD_SIZE - TORSO_HEIGHT * 0.45)
upper_arm_l.parent = shoulder_l

# Os avant-bras gauche
forearm_l = bones.new("forearm_L")
forearm_l.head = upper_arm_l.tail.copy()
forearm_l.tail = (-SHOULDER_WIDTH/2 - 0.07, 0,
                   TOTAL_HEIGHT - HEAD_SIZE - TORSO_HEIGHT * 0.85)
forearm_l.parent = upper_arm_l

# Main gauche
hand_l = bones.new("hand_L")
hand_l.head = forearm_l.tail.copy()
hand_l.tail = (-SHOULDER_WIDTH/2 - 0.08, 0,
                TOTAL_HEIGHT - HEAD_SIZE - TORSO_HEIGHT * 1.0)
hand_l.parent = forearm_l

# Miroir côté droit (même structure, X inversé)
shoulder_r = bones.new("shoulder_R")
shoulder_r.head = (SHOULDER_WIDTH * 0.3, 0, TOTAL_HEIGHT - HEAD_SIZE - 0.05)
shoulder_r.tail = (SHOULDER_WIDTH/2, 0, TOTAL_HEIGHT - HEAD_SIZE - 0.1)
shoulder_r.parent = chest

upper_arm_r = bones.new("upper_arm_R")
upper_arm_r.head = (SHOULDER_WIDTH/2, 0, TOTAL_HEIGHT - HEAD_SIZE - 0.1)
upper_arm_r.tail = (SHOULDER_WIDTH/2 + 0.05, 0,
                     TOTAL_HEIGHT - HEAD_SIZE - TORSO_HEIGHT * 0.45)
upper_arm_r.parent = shoulder_r

forearm_r = bones.new("forearm_R")
forearm_r.head = upper_arm_r.tail.copy()
forearm_r.tail = (SHOULDER_WIDTH/2 + 0.07, 0,
                   TOTAL_HEIGHT - HEAD_SIZE - TORSO_HEIGHT * 0.85)
forearm_r.parent = upper_arm_r

hand_r = bones.new("hand_R")
hand_r.head = forearm_r.tail.copy()
hand_r.tail = (SHOULDER_WIDTH/2 + 0.08, 0,
                TOTAL_HEIGHT - HEAD_SIZE - TORSO_HEIGHT * 1.0)
hand_r.parent = forearm_r

# Cuisse gauche
thigh_l = bones.new("thigh_L")
thigh_l.head = (-HIP_WIDTH/2 + 0.07, 0, LEG_HEIGHT)
thigh_l.tail = (-HIP_WIDTH/2 + 0.05, 0, LEG_HEIGHT * 0.5)
thigh_l.parent = pelvis

# Tibia gauche
shin_l = bones.new("shin_L")
shin_l.head = thigh_l.tail.copy()
shin_l.tail = (-HIP_WIDTH/2 + 0.04, 0, LEG_HEIGHT * 0.1)
shin_l.parent = thigh_l

# Pied gauche
foot_l = bones.new("foot_L")
foot_l.head = shin_l.tail.copy()
foot_l.tail = (-HIP_WIDTH/2 + 0.04, -0.12, 0)
foot_l.parent = shin_l

# Cuisse droite
thigh_r = bones.new("thigh_R")
thigh_r.head = (HIP_WIDTH/2 - 0.07, 0, LEG_HEIGHT)
thigh_r.tail = (HIP_WIDTH/2 - 0.05, 0, LEG_HEIGHT * 0.5)
thigh_r.parent = pelvis

# Tibia droit
shin_r = bones.new("shin_R")
shin_r.head = thigh_r.tail.copy()
shin_r.tail = (HIP_WIDTH/2 - 0.04, 0, LEG_HEIGHT * 0.1)
shin_r.parent = thigh_r

# Pied droit
foot_r = bones.new("foot_R")
foot_r.head = shin_r.tail.copy()
foot_r.tail = (HIP_WIDTH/2 - 0.04, -0.12, 0)
foot_r.parent = shin_r

bpy.ops.object.mode_set(mode='OBJECT')

# === VÉRIFICATION FINALE ===
total_bones = len(arm_data.bones)
print(f"\n✅ ELARA VOSS BLOCKOUT CRÉÉ")
print(f"   Os total : {total_bones}/60 (limite PS2)")
print(f"   Hauteur  : {TOTAL_HEIGHT}m")
print(f"   Épaules  : {SHOULDER_WIDTH}m")
print(f"\n⚠️  PROCHAINE ÉTAPE : Retopologie manuelle")
print(f"   Objectif : < 4000 triangles final")
print(f"   Guide    : assets_sources/characters/elara_voss/ELARA_GUIDE.md")
