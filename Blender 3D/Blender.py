import bpy
from math import radians

#create cube
bpy.ops.mesh.primitive_cube_add()

so = bpy.context.active_object

#move object
so.location[0] = 5

#[0] = X
#[1] = Y
#[2] = Z

#radians object
so.rotation_euler[0] = radians(45)

#create modifiers
so.modifiers.new("My Modifier", 'SUBSURF')

so.modifiers["My Modifier"].levels = 3

mod_subsurf = so.modifiers.new("My Modifier", 'SUBSURF')
mod_subsurf.levels = 5

bpy.ops.object.shade_smooth()