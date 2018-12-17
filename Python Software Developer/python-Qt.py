import os
from random import randint
import numpy as np
xsi = Application

# This Xsi Project's folder path
project_path    = xsi.ActiveProject.Path

def Randomize_Position(obj):
    # Get random numbers between -10 and 10 and set as position
    obj.Kinematics.Local.posx.Value    = randint(-10,10)
    obj.Kinematics.Local.posy.Value    = randint(-10,10)
    obj.Kinematics.Local.posz.Value    = randint(-10,10)

# Create Cube called "Cube_Character"
cube_obj    = xsi.CreatePrim("Cube", "MeshSurface", "Cube_Character")
Randomize_Position(cube_obj)
model_path    = os.path.join(project_path, "Models", "Cube_Character.emdl")
xsi.ExportModel(cube_obj, model_path)

# Create Sphere called "Sphere_Character"
sphere_obj    = xsi.CreatePrim("Sphere", "MeshSurface", "Sphere_Character")
Randomize_Position(sphere_obj)
model_path    = os.path.join(project_path, "Models", "Sphere_Character.emdl")
xsi.ExportModel(sphere_obj, model_path)

# Create Spot Light called "Spot_Light"
spot_obj    = xsi.GetPrimLight("Spot.Preset", "Spot_Light")
Randomize_Position(spot_obj)
model_path    = os.path.join(project_path, "Models", "Spot_Light.emdl")
xsi.ExportModel(spot_obj, model_path)

# Create a Camera called "Main_Camera"
cam_obj        = xsi.GetPrimCamera("Camera", "Main_Camera")
cam_obj.Kinematics.Local.posz.Value = 50
model_path    = os.path.join(project_path, "Models", "Main_Camera.emdl")
xsi.ExportModel(cam_obj, model_path)

# Create a Cylinder called "Cylinder_Prop"
cyl_obj        = xsi.CreatePrim("Cylinder", "MeshSurface", "Cylinder_Prop")
Randomize_Position(cyl_obj)
model_path    = os.path.join(project_path, "Models", "Cylinder_Prop.emdl")
xsi.ExportModel(cyl_obj, model_path)