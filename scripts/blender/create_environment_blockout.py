# scripts/blender/create_environment_blockout.py
# Lance dans Blender : Scripting → Open → Run Script
# Génère les props Velnor Slums + plan Atlas prêt à peindre

import bpy
import math

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# === MATÉRIAU ATLAS PARTAGÉ (1 seul pour TOUS les props) ===
# Principe : chaque prop utilise une zone différente du même atlas 2048x2048
mat = bpy.data.materials.new(name="velnor_atlas")
mat.use_nodes = True
nodes = mat.node_tree.nodes
links = mat.node_tree.links
nodes.clear()

# Nœud texture (sera lié à l'atlas 2048x2048 peint dans Krita)
tex_node = nodes.new('ShaderNodeTexImage')
tex_node.interpolation = 'Closest'   # Nearest-neighbor = style PS2 pixélisé
tex_node.location = (-300, 0)

# Nœud émission (Unlit = pas de PBR, pas de lumière calculée)
emit_node = nodes.new('ShaderNodeEmission')
emit_node.location = (0, 0)

output_node = nodes.new('ShaderNodeOutputMaterial')
output_node.location = (300, 0)

links.new(tex_node.outputs['Color'], emit_node.inputs['Color'])
links.new(emit_node.outputs['Emission'], output_node.inputs['Surface'])

def assign_atlas(obj):
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)

# === PROP 1 : MUR EN PIERRE (stone_wall) ===
# Zone Atlas : UV range X[0.0-0.25], Y[0.75-1.0]
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 1.0))
wall = bpy.context.object
wall.name = "prop_stone_wall"
wall.scale = (2.0, 0.3, 2.0)
bpy.ops.object.transform_apply(scale=True)
assign_atlas(wall)
# Tag de zone atlas dans custom property
wall["atlas_zone"] = "TL"   # Top-Left du atlas

# === PROP 2 : TONNEAU (barrel) ===
# Zone Atlas : UV range X[0.25-0.5], Y[0.75-1.0]
bpy.ops.mesh.primitive_cylinder_add(
    vertices=8, radius=0.22, depth=0.45,
    location=(3, 0, 0.225)
)
barrel = bpy.context.object
barrel.name = "prop_barrel"
assign_atlas(barrel)
barrel["atlas_zone"] = "TR"  # Top-Right

# Couvercle du tonneau
bpy.ops.mesh.primitive_cylinder_add(
    vertices=8, radius=0.24, depth=0.04,
    location=(3, 0, 0.47)
)
lid = bpy.context.object
lid.name = "prop_barrel_lid"
assign_atlas(lid)
lid["atlas_zone"] = "TR"

# === PROP 3 : CAISSE EN BOIS (crate) ===
# Zone Atlas : UV range X[0.5-0.75], Y[0.75-1.0]
bpy.ops.mesh.primitive_cube_add(size=0.6, location=(6, 0, 0.3))
crate = bpy.context.object
crate.name = "prop_crate"
assign_atlas(crate)
crate["atlas_zone"] = "BL"  # Bottom-Left

# === PROP 4 : PIERRE TOMBALE (gravestone) ===
# Zone Atlas : UV range X[0.75-1.0], Y[0.75-1.0]
bpy.ops.mesh.primitive_cube_add(size=1, location=(9, 0, 0.5))
grave = bpy.context.object
grave.name = "prop_gravestone"
grave.scale = (0.3, 0.12, 0.9)
bpy.ops.object.transform_apply(scale=True)
assign_atlas(grave)
grave["atlas_zone"] = "BR"  # Bottom-Right

# Arrondi du haut (demi-cylindre)
bpy.ops.mesh.primitive_cylinder_add(
    vertices=8, radius=0.15, depth=0.12,
    location=(9, 0, 0.95)
)
grave_top = bpy.context.object
grave_top.name = "prop_gravestone_top"
# Couper en deux (demi-cylindre) manuellement en Blender ensuite
assign_atlas(grave_top)
grave_top["atlas_zone"] = "BR"

# === PROP 5 : PAVÉ DE SOL (floor_tile) ===
# Tuile 1m × 1m, empilable par instanciation dans Bevy
bpy.ops.mesh.primitive_plane_add(size=1.0, location=(0, 5, 0))
tile = bpy.context.object
tile.name = "prop_floor_tile"
assign_atlas(tile)
tile["atlas_zone"] = "BOTTOM_STRIP"  # Bande basse de l'atlas

# === PROP 6 : LAMPADAIRE ROUILLÉ (lantern_post) ===
# Iconique dans les slums — lumière ambiante visuelle (faux light map sur texture)
bpy.ops.mesh.primitive_cylinder_add(
    vertices=6, radius=0.04, depth=2.2,
    location=(3, 5, 1.1)
)
post = bpy.context.object
post.name = "prop_lantern_post"
assign_atlas(post)
post["atlas_zone"] = "CENTER"

# Lanterne (cube hexagonal simplifié)
bpy.ops.mesh.primitive_cube_add(size=0.25, location=(3, 5, 2.35))
lantern = bpy.context.object
lantern.name = "prop_lantern_head"
assign_atlas(lantern)
lantern["atlas_zone"] = "CENTER"

# === PLAN DE SOL POUR MISE EN SCÈNE ===
bpy.ops.mesh.primitive_plane_add(size=15.0, location=(4.5, 2.5, 0))
ground = bpy.context.object
ground.name = "scene_ground_preview"
assign_atlas(ground)

# === GUIDE ZONES ATLAS (objet texte informatif) ===
# Ce texte rappelle quelle zone de l'atlas 2048x2048 est réservée à quel prop
bpy.ops.object.text_add(location=(-2, -4, 0))
text_obj = bpy.context.object
text_obj.name = "ATLAS_GUIDE_TEXT"
text_obj.data.body = (
    "ATLAS 2048x2048 — ZONES RÉSERVÉES\n"
    "TL  [0.00-0.25 / 0.75-1.00] → stone_wall\n"
    "TR  [0.25-0.50 / 0.75-1.00] → barrel\n"
    "BL  [0.50-0.75 / 0.75-1.00] → crate\n"
    "BR  [0.75-1.00 / 0.75-1.00] → gravestone\n"
    "BOT [0.00-1.00 / 0.00-0.25] → floor_tile\n"
    "CTR [0.25-0.75 / 0.25-0.75] → lantern_post\n"
    "  → Ouvrir dans Krita : assets_sources/environment/velnor_atlas.kra"
)
text_obj.data.size = 0.18

total_props = 7
print(f"\n✅ VELNOR SLUMS BLOCKOUT CRÉÉ")
print(f"   Props générés   : {total_props}")
print(f"   Matériau unique : 'velnor_atlas' (Unlit Emission + Nearest-Neighbor)")
print(f"   Draw calls      : 1 seul pour tous les props (atlas partagé)")
print(f"\n📐 ZONES ATLAS ASSIGNÉES (à peindre dans Krita) :")
print(f"   TL → stone_wall  | TR → barrel")
print(f"   BL → crate       | BR → gravestone")
print(f"   BOT → floor_tile | CTR → lantern_post")
print(f"\n⚠️  PROCHAINE ÉTAPE : UV Unwrap de chaque prop")
print(f"   Guide : assets_sources/environment/ATLAS_GUIDE.md")
print(f"   Atlas : assets_sources/environment/velnor_atlas.kra")
