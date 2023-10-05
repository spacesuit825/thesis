import bpy
import math
import sys
import csv

X = 0.08 * 1000
Y = 0.08 * 1000
offset = 0.04

bpy.context.scene.unit_settings.system = 'METRIC'
bpy.context.scene.unit_settings.length_unit = 'METERS'
bpy.context.scene.unit_settings.scale_length = 1.0

for o in bpy.context.scene.objects:
    if o.type == 'MESH':
        o.select_set(True)
    else:
        o.select_set(False)

part_data = []
with open('C:/Users/lachl/Documents/thesis/process_rocky/part3_data.csv', 'r') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        part_data.append(row)

for i in range(len(part_data)):
    if part_data[i] == []:
        continue
    
    bpy.ops.import_mesh.stl(filepath='C:/Users/lachl/Documents/thesis/particle_shape/test_4.stl')

    part = bpy.context.active_object
    part.location = (part_data[i][0] * 1000, part_data[i][1] * 1000, part_data[i][2] * 1000)
    
    part.rotation_mode = 'AXIS_ANGLE'
    part.rotation_axis_angle[0] = part_data[i][3]
    part.rotation_axis_angle[1] = part_data[i][4]
    part.rotation_axis_angle[2] = part_data[i][5]
    part.rotation_axis_angle[3] = part_data[i][6]
    
    scale = 1000
    part.scale[0] = scale
    part.scale[1] = scale
    part.scale[2] = scale
    
    

for o in bpy.context.scene.objects:
    if o.type == 'MESH':
        o.select_set(True)
    else:
        o.select_set(False)

bpy.ops.object.duplicate(linked=False)
bpy.ops.transform.translate(value=(X,0,0))

for o in bpy.context.scene.objects:
    if o.type == 'MESH':
        o.select_set(True)
    else:
        o.select_set(False)

bpy.ops.object.duplicate(linked=False)
bpy.ops.transform.translate(value=(0,0,Y))

for o in bpy.context.scene.objects:
    if o.type == 'MESH':
        o.select_set(True)
    else:
        o.select_set(False)

bpy.ops.object.join()
grains = bpy.context.object

#bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(X/2, 0, Y/2))
#block = bpy.context.object
#block.name = 'block'
#block.scale[0] = X - 2*offset
#block.scale[1] = 500
#block.scale[2] = Y - 2*offset

#bool = grains.modifiers.new(type='BOOLEAN', name="bool 1")
#bool.object = block
#bool.operation = 'INTERSECT'
#bool.solver = 'FAST'

#bpy.ops.object.select_all(action='DESELECT')
#bpy.context.view_layer.objects.active = grains

#bpy.ops.object.modifier_apply(modifier="bool 1")

#bpy.ops.object.select_all(action='DESELECT')
#bpy.data.objects['block'].select_set(True)
#bpy.ops.object.delete()

#bpy.ops.object.editmode_toggle()
#bpy.ops.mesh.delete_loose()
#bpy.ops.export_mesh.stl(filepath='C:/Users/lachl/Documents/thesis/particle_shape/mesh.stl')