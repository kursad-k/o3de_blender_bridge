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
"""! @brief This is the entry point for the DCCsi Launcher. Come up with a better description """

##
# @file main.py
#
# @brief The Blender O3DE Scene exporter is a convenience tool for one click
# exporter from Blender to O3DE.
#
# @section This DCCsi tool is non-destructive to your scene, as it will export
# selected copies of your mesh and textures, re-path texture links to your mesh
# during file export. You can export selected static meshes or rigged animated
# meshes within the capabilities of the .FBX format and O3DE actor entity.
#
# You have options to export textures with the mesh, or with the mesh within
# a sub folder "/textures". This will work for Blender Scenes with or without
# packed textures.
#
# Hardware and Software Requirements:
#
# Support for Blender 4.+ Windows 10/11 64-bit version
# O3DE Stable 23.10 Release Windows 10/11 64-bit version
#
# @section Launcher Notes
# - Comments are Doxygen compatible

bl_info = {
    "name": "O3DE_DCCSI_BLENDER_SCENE_EXPORTER",
    "author": "kursad-k, shawstar@amazon(original maintainer)",
    "version": (1, 5, 1),
    "blender": (4, 00, 0),
    "location": "",
    "description": "Export Scene Assets to O3DE",
    "warning": "",
    "doc_url": "",
    "category": "Import-Export",
}  # This is needed for Blender Plugin


import sys
import importlib

from re import A
from typing import Any
import bpy
from bpy.props import EnumProperty, PointerProperty
import sys
from pathlib import Path
# Needed to import custom scripts in Blender Python


from . import o3de_utils
from . import ui
from . import constants


if locals().get('loaded'):
    loaded = False
    from importlib import reload
    from sys import modules

    modules[__name__] = reload(modules[__name__])
    for name, module in modules.items():
        if name.startswith(f"{__package__}."):
            globals()[name] = reload(module)
    del reload, modules



classes = (
    ui.O3deTools,
    ui.MessageBox,
    ui.MessageBoxConfirm,
    ui.ReportCardButton,
    ui.WikiButton,
    ui.CustomProjectPath,
    ui.AddColliderMesh,
    ui.AddLODMesh,
    ui.ProjectsListDropDown,
    ui.SceneExporterFileMenu,
    ui.ExportOptionsListDropDown,
    ui.AnimationOptionsListDropDown,
    ui.O3DE_OP_Export_Selected,
    ui.O3DE_OP_Export_Collection,
)


def register():
    """! 
    This is the function that will register Classes and Global Vars for this plugin
    """
    # bpy.utils.register_class(ui.O3deTools)
    # bpy.utils.register_class(ui.MessageBox)
    # bpy.utils.register_class(ui.MessageBoxConfirm)
    # bpy.utils.register_class(ui.ReportCard)
    # # bpy.utils.register_class(ui.ReportCardButton)
    # bpy.utils.register_class(ui.WikiButton)
    # bpy.utils.register_class(ui.CustomProjectPath)
    # bpy.utils.register_class(ui.AddColliderMesh)
    # bpy.utils.register_class(ui.AddLODMesh)
    # bpy.utils.register_class(ui.ProjectsListDropDown)
    # bpy.utils.register_class(ui.SceneExporterFileMenu)
    # bpy.utils.register_class(ui.ExportOptionsListDropDown)
    # bpy.utils.register_class(ui.AnimationOptionsListDropDown)
    
    ## Refactoring starts here
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    
    ui.register_props()
    
    bpy.types.TOPBAR_MT_file_export.append(ui.file_export_menu_add)  # Blender Specific Class and Naming Convention. 
    
def unregister():
    """! This is the function that will unregister Classes and Global Vars for this plugin
    """
    
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    
    ui.delete_props()
    # bpy.utils.unregister_class(ui.O3deTools)
    # bpy.utils.unregister_class(ui.MessageBox)
    # bpy.utils.unregister_class(ui.MessageBoxConfirm)
    # bpy.utils.unregister_class(ui.ReportCard)
    # bpy.utils.unregister_class(ui.ReportCardButton)
    # bpy.utils.unregister_class(ui.WikiButton)
    # bpy.utils.unregister_class(ui.CustomProjectPath)
    # bpy.utils.unregister_class(ui.AddColliderMesh)
    # bpy.utils.unregister_class(ui.AddLODMesh)
    # bpy.utils.unregister_class(ui.ProjectsListDropDown)
    # bpy.utils.unregister_class(ui.SceneExporterFileMenu)
    # bpy.utils.unregister_class(ui.ExportOptionsListDropDown)
    # bpy.utils.unregister_class(ui.AnimationOptionsListDropDown)
    
    bpy.types.TOPBAR_MT_file_export.remove(ui.file_export_menu_add)  # Blender Specific Class and Naming Convention. 

if __name__ == "__main__":
    register()

loaded = True
