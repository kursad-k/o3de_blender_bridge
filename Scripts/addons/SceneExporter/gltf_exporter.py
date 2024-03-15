# coding:utf-8
#!/usr/bin/python
#
# Copyright (c) Contributors to the Open 3D Engine Project.
# For complete copyright and license terms please see the LICENSE at the root of this distribution.
#
# SPDX-License-Identifier: Apache-2.0 OR MIT
#
#
# -------------------------------------------------------------------------
from pathlib import Path
from . import utils
from . import o3de_utils
from . import constants
import bpy

def _gltf_export_(file=None,gscale=1.0,custom=None, context=bpy.context):
    
    for i in range(5):
        print("EXPORTING GLTF")
        
def gltf_export(file=None,gscale=1.0,custom=None, context=bpy.context):
    """!
        filepath='', check_existing=True, export_import_convert_lighting_mode='SPEC', 
        gltf_export_id='', export_format='GLB', ui_tab='GENERAL', export_copyright='', 
        export_image_format='AUTO', export_image_add_webp=False, export_image_webp_fallback=False, 
        export_texture_dir='', export_jpeg_quality=75, export_image_quality=75, 
        export_keep_originals=False, export_texcoords=True, export_normals=True, 
        export_draco_mesh_compression_enable=False, export_draco_mesh_compression_level=6, 
        export_draco_position_quantization=14, export_draco_normal_quantization=10, 
        export_draco_texcoord_quantization=12, export_draco_color_quantization=10, 
        export_draco_generic_quantization=12, export_tangents=False, export_materials='EXPORT', 
        export_colors=True, export_attributes=False, use_mesh_edges=False, use_mesh_vertices=False, 
        export_cameras=False, use_selection=False, use_visible=False, use_renderable=False, 
        use_active_collection_with_nested=True, use_active_collection=False, use_active_scene=False, 
        export_extras=False, export_yup=True, export_apply=False, export_animations=True, export_frame_range=False, 
        export_frame_step=1, export_force_sampling=True, export_animation_mode='ACTIONS', 
        export_nla_strips_merged_animation_name='Animation', export_def_bones=False, export_hierarchy_flatten_bones=False, 
        export_optimize_animation_size=True, export_optimize_animation_keep_anim_armature=True, 
        export_optimize_animation_keep_anim_object=False, export_negative_frame='SLIDE', 
        export_anim_slide_to_zero=False, export_bake_animation=False, export_anim_single_armature=True, 
        export_reset_pose_bones=True, export_current_frame=False, 
        export_rest_position_armature=True, export_anim_scene_split_object=True, export_skins=True, export_influence_nb=4, 
        export_all_influences=False, export_morph=True, export_morph_normal=True, export_morph_tangent=False, 
        export_morph_animation=True, export_morph_reset_sk_data=True, export_lights=False, export_try_sparse_sk=True, 
        export_try_omit_sparse_sk=False, export_gpu_instances=False, export_nla_strips=True, export_original_specular=False, 
        will_save_settings=False, filter_glob='*.glb'
    """
    C=context
    
    if file and custom:
        self.customExport(exporter="bpy.ops.export_scene.gltf",
                        file=file,global_scale=gscale, custom=custom,
                        exporterdefaults="use_selection=True")
        
    elif file:
        f_start=C.scene.frame_start
        f_end=C.scene.frame_end
        c_frame=C.scene.frame_current

        #TODO: Renable frame range export later
        # We set the frame range to current frame so only current frame is exported
        C.scene.frame_start=c_frame
        C.scene.frame_end=c_frame

        bpy.ops.export_scene.gltf(filepath=file, export_format='GLTF_SEPARATE', use_renderable=True, use_active_scene=True, use_selection=True, 
                                    use_visible=True, export_apply=True, export_yup=False, export_bake_animation=True, export_image_format='AUTO')
        #export_selected=True (I got a warning here)

        #Restore frames
        C.scene.frame_start=f_start
        C.scene.frame_end=f_end

        return True
    else:
        print("No file path exists for the FBX export")
        return False