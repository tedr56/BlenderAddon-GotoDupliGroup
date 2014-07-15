import bpy

bl_info = {
    "name": "GotoDupliGroup",
    "author": "Ted VjBros",
    "version": (0, 1, 1),
    "blender": (2, 69, 0),
    "location": "Properties > Object > Duplication",
    "description": "Quick Shortcut to the Duplicated Group",
    "category": "Object",
    "wiki_url": "https://github.com/tedr56/BlenderAddon-GotoDupliGroup",
    "tracker_url": "https://github.com/tedr56/BlenderAddon-GotoDupliGroup/issues"
    }
    

class GotoDupliGroup(bpy.types.Operator):
    bl_idname = "dupligroup.goto"
    bl_label = "Goto DupliGroup"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        if context.active_object:
            return context.active_object.dupli_group is not None and context.active_object.dupli_type == 'GROUP'
        return False
        
    def execute(self, context):
        Dupligroup = context.active_object.dupli_group
        duplicates = Dupligroup.objects.items()
        if len(duplicates):
            layers = [False for i in range(20)]
            for object in duplicates:
                print(object)
                ObjectLayers = object[1].layers
                for i in range(20):
                    if ObjectLayers[i]:
                        layers[i] = True
            bpy.ops.object.select_all(action='DESELECT')
            context.scene.layers = layers
            for object in Dupligroup.objects:
            	bpy.ops.object.select_pattern(pattern=object.name, case_sensitive=False, extend=True)
            context.scene.objects.active = duplicates[0][1]
            return {'FINISHED'}
        return {'CANCELED'}

def menu_func(self, context):
    if context.active_object.dupli_type == 'GROUP':
    	self.layout.operator(GotoDupliGroup.bl_idname, icon='MESH_CUBE')

def register():
    bpy.utils.register_class(GotoDupliGroup)
    bpy.types.OBJECT_PT_duplication.append(menu_func)

def unregister():
    bpy.utils.unregister_class(GotoDupliGroup)
    bpy.types.OBJECT_PT_duplication.remove(menu_func)


if __name__ == "__main__":
    register()   