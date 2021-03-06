# #####
# This file is part of the RobotDesigner of the Neurorobotics subproject (SP10)
# in the Human Brain Project (HBP).
# It has been forked from the RobotEditor (https://gitlab.com/h2t/roboteditor)
# developed at the Karlsruhe Institute of Technology in the
# High Performance Humanoid Technologies Laboratory (H2T).
# #####

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# #####
#
# Copyright (c) 2015, Karlsruhe Institute of Technology (KIT)
# Copyright (c) 2016, FZI Forschungszentrum Informatik
#
# Changes:
#
#   2015-01-16: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#   2017-06:    Benedikt Feldotto (TUM): Model Meta Data
#   2017-07:    Benedikt Feldotto (TUM): Full Inertia Support
#   2017-09:    Benedikt Feldotto (TUM), Muscle Support

#
# ######

# Blender imports
from glob import glob

import bpy
from bpy.props import FloatProperty, StringProperty, \
    EnumProperty, FloatVectorProperty, PointerProperty, IntProperty, CollectionProperty

# RobotDesigner imports
from ..core import PluginManager
from ..properties.globals import global_properties


# from .globals import global_properties

@PluginManager.register_property_group()
class RDDynamics(bpy.types.PropertyGroup):
    '''
    Property group that contains dynamics values
    '''
    # from mathutils import Vector
    # def updateCoM(self, context):
    #    frame = bpy.data.objects[bpy.context.scene.RobotDesigner.physicsFrameName]
    #    position = Vector((frame.RobotDesigner.dynamics.CoM[0],frame.RobotDesigner.dynamics.CoM[1],
    # frame.RobotDesigner.dynamics.CoM[2]))
    #    frame.location = position

    mass = FloatProperty(name="Mass (kg)", precision=4, step=0.1, default=1.0)

    # new inertia tensor
    inertiaXX = FloatProperty(name="", precision=4, step=0.1, default=1.0)
    inertiaXY = FloatProperty(name="", precision=4, step=0.1, default=0.0)
    inertiaXZ = FloatProperty(name="", precision=4, step=0.1, default=0.0)
    inertiaYY = FloatProperty(name="", precision=4, step=0.1, default=1.0)
    inertiaYZ = FloatProperty(name="", precision=4, step=0.1, default=0.0)
    inertiaZZ = FloatProperty(name="", precision=4, step=0.1, default=1.0)

@PluginManager.register_property_group()
class RDSensorNoise(bpy.types.PropertyGroup):
    type = EnumProperty(items=[('gaussian', 'Gaussian', 'Gaussian')])
    mean = FloatProperty(name="mean", default=0)
    stddev = FloatProperty(name="stddev", default=0)

@PluginManager.register_property_group()
class RDCamera(bpy.types.PropertyGroup):
    width = IntProperty(default=320, min=1)
    height = IntProperty(default=240, min=1)
    format = EnumProperty(items=[('L8', 'L8', 'L8'),
                                 ('R8G8B8', 'R8G8B8', 'R8G8B8'),
                                 ('B8G8R8', 'B8G8R8', 'B8G8R8'),
                                 ('BAYER_RGGB8', 'BAYER_RGGB8', 'BAYER_RGGB8'),
                                 ('BAYER_BGGR8', 'BAYER_BGGR8', 'BAYER_BGGR8'),
                                 ('BAYER_GBRG8', 'BAYER_GBRG8', 'BAYER_GBRG8'),
                                 ('BAYER_GRBG8', 'BAYER_GRBG8', 'BAYER_GRBG8')
                                 ])

    noise = PointerProperty(type=RDSensorNoise)


@PluginManager.register_property_group()
class RDContactSensor(bpy.types.PropertyGroup):
    collision = StringProperty(name="collision", default="__default__")
    topic = StringProperty(name="topic", default="__default_topic__")


@PluginManager.register_property_group()
class RDForceTorqueSensor(bpy.types.PropertyGroup):
    frame = StringProperty(name="frame", default="child")
    measure_direction = StringProperty(name="measure_direction", default="child_to_parent")


@PluginManager.register_property_group()
class RDDepthCameraSensor(bpy.types.PropertyGroup):
    output = StringProperty(name="output", default="depths")


@PluginManager.register_property_group()
class RDAltimeterSensor(bpy.types.PropertyGroup):
    vptype = StringProperty(name="type", default="none")
    vpmean = FloatProperty(name="mean", default=0)
    vpstddev = FloatProperty(name="stddev", default=0)
    vpbias_mean = FloatProperty(name="stddev", default=0)
    vpbias_stddev = FloatProperty(name="bias_stddev", default=0)
    vpprecision = FloatProperty(name="precision", default=0)
    vvtype = StringProperty(name="type", default="none")
    vvmean = FloatProperty(name="mean", default=0)
    vvstddev = FloatProperty(name="stddev", default=0)
    vvbias_mean = FloatProperty(name="stddev", default=0)
    vvbias_stddev = FloatProperty(name="bias_stddev", default=0)
    vvprecision = FloatProperty(name="precision", default=0)


@PluginManager.register_property_group()
class RDIMUSensor(bpy.types.PropertyGroup):
    localization = StringProperty(name="localization", default="CUSTOM")
    custom_rpy = FloatVectorProperty(name="custom_rpy", precision=4, default=[0.0, 0.0, 0.0])
    grav_dir_x = FloatVectorProperty(name="grav_dir_x", precision=4, default=[1.0, 0.0, 0.0])
    parent_frame = StringProperty(name="parent_frame", default="Name of parent frame")
    topic = StringProperty(name="topic", default="__default_topic__")
    vvtype = StringProperty(name="type", default="none")
    avxmean = FloatProperty(name="mean", default=0)
    avxstddev = FloatProperty(name="stddev", default=0)
    avxbias_mean = FloatProperty(name="stddev", default=0)
    avxbias_stddev = FloatProperty(name="bias_stddev", default=0)
    avxprecision = FloatProperty(name="precision", default=0)
    avymean = FloatProperty(name="mean", default=0)
    avystddev = FloatProperty(name="stddev", default=0)
    avybias_mean = FloatProperty(name="stddev", default=0)
    avybias_stddev = FloatProperty(name="bias_stddev", default=0)
    avyprecision = FloatProperty(name="precision", default=0)
    avzmean = FloatProperty(name="mean", default=0)
    avzstddev = FloatProperty(name="stddev", default=0)
    avzbias_mean = FloatProperty(name="stddev", default=0)
    avzbias_stddev = FloatProperty(name="bias_stddev", default=0)
    avzprecision = FloatProperty(name="precision", default=0)
    laxmean = FloatProperty(name="mean", default=0)
    laxstddev = FloatProperty(name="stddev", default=0)
    laxbias_mean = FloatProperty(name="stddev", default=0)
    laxbias_stddev = FloatProperty(name="bias_stddev", default=0)
    laxprecision = FloatProperty(name="precision", default=0)
    laymean = FloatProperty(name="mean", default=0)
    laystddev = FloatProperty(name="stddev", default=0)
    laybias_mean = FloatProperty(name="stddev", default=0)
    laybias_stddev = FloatProperty(name="bias_stddev", default=0)
    layprecision = FloatProperty(name="precision", default=0)
    lazmean = FloatProperty(name="mean", default=0)
    lazstddev = FloatProperty(name="stddev", default=0)
    lazbias_mean = FloatProperty(name="stddev", default=0)
    lazbias_stddev = FloatProperty(name="bias_stddev", default=0)
    lazprecision = FloatProperty(name="precision", default=0)


@PluginManager.register_property_group()
class RDLaserSensor(bpy.types.PropertyGroup):
    horizontal_samples = IntProperty(name="horizontal samples", default=320, min=1)
    vertical_samples = IntProperty(name="vertical samples", default=240, min=1)
    resolution = EnumProperty(items=[('8-Bit', '8-Bit', '8-Bit'),
                                     ('16-Bit', '16-Bit', '16-Bit')
                                     ])


class SceneSettingItem(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(name="Test Prop", default="Unknown")
    value = bpy.props.IntProperty(name="Test Prop", default=22)


class RDMusclePoints(bpy.types.PropertyGroup):
    '''
    Property group that contains muscle attachment point specifications
    '''
    # x = FloatProperty(name="X", precision=4, step=0.1, default=1.0)
    # y = FloatProperty(name="Y", precision=4, step=0.1, default=1.0)
    # z = FloatProperty(name="Z", precision=4, step=0.1, default=1.0)

    coordFrame = StringProperty(default="Select Segment")


@PluginManager.register_property_group()
class RDMuscle(bpy.types.PropertyGroup):
    '''
    Property group that contains muscle values
    '''

    def muscle_type_update(self, context):
        active_muscle = global_properties.active_muscle.get(bpy.context.scene)

        # if bpy.data.objects[active_muscle].RobotDesigner.muscles.muscleType == 'MYOROBOTICS':
        #    color = (1.0,0.0,0.0)
        if bpy.data.objects[active_muscle].RobotDesigner.muscles.muscleType == 'MILLARD_EQUIL':
            color = (0.8, 0.3, 0.0)
        elif bpy.data.objects[active_muscle].RobotDesigner.muscles.muscleType == 'MILLARD_ACCEL':
            color = (0.3, 0.8, 0.0)
        elif bpy.data.objects[active_muscle].RobotDesigner.muscles.muscleType == 'THELEN':
            color = (1.0, 0.0, 0.0)
        elif bpy.data.objects[active_muscle].RobotDesigner.muscles.muscleType == 'RIGID_TENDON':
            color = (0.0, 0.0, 1.0)

        bpy.data.objects[active_muscle].data.materials[active_muscle + '_vis'].diffuse_color = color

    muscleType = EnumProperty(
        items=[  # ('MYOROBOTICS', 'Myorobotics', 'Myorobotics Muscle'),
            ('MILLARD_EQUIL', 'Millard Equilibrium 2012', 'Millard Equilibrium 2012 Muscle'),
            ('MILLARD_ACCEL', 'Millard Acceleration 2012', 'Millard Acceleration 2012 Muscle'),
            ('THELEN', 'Thelen 2003', 'Thelen 2003 Muscle'),
            ('RIGID_TENDON', 'Rigid Tendon', 'Rigid Tendon Muscle')],
        name="Muscle Type:", update=muscle_type_update
    )

    robotName = StringProperty(name="RobotName")
    length = FloatProperty(name="muscle length", default=0.0, precision=2)
    max_isometric_force = FloatProperty(name="Max isometric Force", default=1000)

    bpy.utils.register_class(RDMusclePoints)
    pathPoints = CollectionProperty(type=RDMusclePoints)


@PluginManager.register_property_group()
class RDModelMeta(bpy.types.PropertyGroup):
    '''
    Property group that contains model meta data suc as name, version and description
    '''
    model_version = StringProperty(name='Version', default="1.0")
    model_folder = StringProperty(name='Folder', default="")
    model_description = StringProperty(name='Description')


@PluginManager.register_property_group()
class RDAuthor(bpy.types.PropertyGroup):
    '''
    Property group that contains author details such as name and email
    '''
    authorName = StringProperty(name="author name")
    authorEmail = StringProperty(name="author email")


@PluginManager.register_property_group(bpy.types.Object)
class RDObjects(bpy.types.PropertyGroup):
    '''
    Property group that stores general information for individual Blender
    objects with respect to the RobotDesigner
    '''
    fileName = StringProperty(name="Mesh File Name")
    tag = EnumProperty(
        items=[('DEFAULT', 'Default', 'Default'),
               ('MARKER', 'Marker', 'Marker'),
               ('PHYSICS_FRAME', 'Physics Frame', 'Physics Frame'),
               ('ARMATURE', 'Armature', 'Armature'),
               ('COLLISION', 'Collision', 'Collision'),
               ('SENSOR', 'Sensor', 'Sensor')
               ]
    )

    fileName = StringProperty(name="Mesh File Name")
    sensor_type = EnumProperty(
        items=[('CAMERA_SENSOR', 'Camera sensor', 'Camera sensor'),
               ('LASER_SENSOR', 'Laser sensor', 'Laser sensor'),
               ('CONTACT_SENSOR', 'Contact Sensors', 'Edit contact sensors'),
               ('FORCE_TORQUE_SENSOR', 'Force Torque Sensors', 'Edit force torque sensors'),
               ('DEPTH_CAMERA_SENSOR', 'Depth Camera Sensors', 'Edit depth camera sensors'),
               ('ALTIMETER_SENSOR', 'Altimeter Sensors', 'Edit altimeter sensors'),
               ('IMU_SENSOR', 'IMU Sensors', 'Edit IMU sensors')]
    )

    dynamics = PointerProperty(type=RDDynamics)
    modelMeta = PointerProperty(type=RDModelMeta)
    author = PointerProperty(type=RDAuthor)
    cameraSensor = PointerProperty(type=RDCamera)
    contactSensor = PointerProperty(type=RDContactSensor)
    forceTorqueSensor = PointerProperty(type=RDForceTorqueSensor)
    depthCameraSensor = PointerProperty(type=RDDepthCameraSensor)
    altimeterSensor = PointerProperty(type=RDAltimeterSensor)
    imuSensor = PointerProperty(type=RDIMUSensor)
    laserSensor = PointerProperty(type=RDLaserSensor)
    muscles = PointerProperty(type=RDMuscle)
