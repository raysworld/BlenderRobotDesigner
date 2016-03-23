# The BlenderRobotDesigner of the *Neurorobotics Platform (NRP)* of the *Human Brain Project*

## Introduction
### About

The *NRP RobotDesigner* software developed in the scope
of the [Human Brain Project](The Human Brain Project) in the sub-project
[SP10 Neurorobtics](http://neurorobotics.net/index.php). It is part of the *Neurorobotics Platform* which
aims at providing easy accessible and usable tools to neuro-scientists and neuro-roboticists for simulating robots
that are controlled by artificial brains in virtual environments. The *RobotDesinger* is a modeling tool that
allows to generate *geometric*, *kinematic* and *dynamic* models, and sensor placement that can be used in the simulation environment of NRP–or any ROS/Gazebo-based environment.
While other services of the NRP are created as web-based services that do not require installation and, therefore,
administration expertise, the *RobotDesigner* is a plugin for the freely available (GPL licensed)
[Blender 3D modeling suite](http://blender.org).
This design decision has been made due to three reasons:

1. The full capabilities of a feature-rich modeling suite such as Blender is an enormous undertaking.
2. Robot design is a process that requires advanced engineering expertise and is time consuming justifying a more complex installation process and interruption of the web-based workflow.
3. Blender is freely available for a wide range of platforms and installation is very easy.
4. It is easily extendible.

Under the hood, the plugin extends the built-in data types and provides an improved and clear interface to
the modeling software. Future development plans of the robot designer, however, include provide a simplified web-based interface integrated into the NRP to construct robots from building blocks. Therefore, the code base of the standalone software is planned to be used and will be further maintained.

### History

The foundations of the *NRP RobotDesigner* has been initially developed under the name *OpenGRASP RobotEditor*
from 2008-2012 at the [Humanoids and Intelligence Systems Lab (HIS) at the
Institute for Anthropomatics and Robotics (IAR)](http://his.anthropomatik.kit.edu/english/index.php)  of the
[Karlsruhe Institute of Technology](http://www.kit.edu/english/index.php) during the
[European GRASP project](http://www.csc.kth.se/grasp/)<sup>[1](#f1),[2](#f2)</sup>
as port of the [OpenGRASP software](http://opengrasp.sourceforge.net/).
This simulation environment has been published under the [GPL v2](http://www.gnu.org/licenses/gpl-2.0.html) license.
This Python plugin restricted to the
Blender version 2.49 was mainly developed by [Stefan Ulbrich (FZI)](mailto:stefan.ulbrich@fzi.de).
One of the most notable features of the *RobotEditor* was support for the
[Collada v1.5](https://www.khronos.org/collada/) data 3D asset exchange format. This file format has large support from
the industry including companies such as Daimler and Sony. The RobotEditor was the only freely available
tool creating valid models for Collada v1.5 which supported the new description facilities for kinematics and dynamics.

Afterwards, the *RobotEditor*<sup>[3](#f3)</sup> has been completely rewritten to comply the programming interface of newer Blender
versions (>2.69) at the [High Perfomance Humanoid Technologies Lab (H<sup>2</sup>T) at the (IAR)](http://h2t.anthropomatik.kit.edu/enligsh/index.php) of
[KIT](http://www.kit.edu/english/index.php) by the main authors
[Michael Bechtel](mailto:michael.bechtel@kit.edu) and [Stefan Ulbrich (FZI)](mailto:stefan.ulbrich@fzi.de). Many new
feature such as *physical properties*, *joint dynamics*, *sensors for matching motion capture data* support for
the [Simox robot simulator](http://simox.sourceforge.net/)<sup>[4](#f4)</sup> have been added to the software. This software is still
developed and available [under the open source GPL license](http://www.gnu.org/licenses/gpl-2.0.html) from [here](https://gitlab.com/h2t/roboteditor).

he *NRP RobotDesigner* is a fork of the *RobotEditor*, which has been chosen as the basis after a comparison to competing projects
(e.g., [phobos](https://github.com/rock-simulation/phobos>)). It will enrich the existing project
by components required for the NRP (e.g., for communication/file exchange), additional file formats, support for simulators, an installer and  an adapted user interface.

### license

Similar to its predecessor *the RobotEditor* the NRP RobotDesigner is published as open source software under the [GPLv2 license](http://www.gnu.org/licenses/gpl-2.0.html).

## The NRP RobotDesigner

### The Human Brain Project<sup>[5](#f5)</sup>

The European Commission has selected the [Human Brain Project](https://www.humanbrainproject.eu>) as one of its two Flagship projects. Over the course of
10 years, the HBP will create an integrated system of six ICT platforms, one dedicated to Neurorobotics.
The Neurorobotics Subproject of the HBP is coordinated by a research group led by [Prof. Alois Knoll](http://www6.in.tum.de/Main/Knoll).
The Human Brain Project is part of the FET Flagship Programme, which is a new initiative launched by the
European Commission as part of its
[Future and Emerging Technologies (FET)](http://cordis.europa.eu/fp7/ict/programme/fet/flagship/) initiative.
The goal is to encourage
visionary, “mission-oriented” research with the potential to deliver breakthroughs in information technology
with major benefits for European society and industry. The Commission envisages the Flagship program as a highly
ambitious initiative involving close collaboration with National and Regional funding agencies, industry and
partners from outside the European Union. [Read more...](http://neurorobotics.net/the-human-brain-project/)

### The Neurorobotics Platform<sup>[6](#f6)</sup>

The Neurorobotics sub-project will develop the Neurorobotics Platform which will offer scientists and technology
developers a software and hardware infrastructure allowing them to connect pre-validated brain models to detailed
simulations of robot bodies and environments and to use the resulting neurorobotic systems in in silico experiments
and technology development.
The goal for the ramp-up phase (*editor's note: The first two years of the project ending in March 2016*) will be to develop the Neurorobotics Platform version 1 which will allow researchers
to design and run simple experiments in cognitive neuroscience using simulated robots and simulated environments
linked to simplified versions of HBP brain models. The *Neurorobotics Platform* will include a Robot Designer, an
Environment Builder, and a Closed-Loop engine, as well as the *Neurorobotics Platform* host facility.
The *Neurorobotics Platform* will exploit the 3D modelling capabilities provided by commercial and open source gaming
platforms (the choice of platform will be made in the early stage of the project). The *HBP Neurorobotics Platform*
will allow researchers to conduct closed-loop experiments, in which a virtual robot is connected to a brain model,
running on the HPC platform or on neuromorphic hardware (*editor's note: E.g., the [SpiNNaker](http://apt.cs.manchester.ac.uk/projects/SpiNNaker/) boards*). Although the capabilities to model virtual robots and
environments already exist, and although various labs have created closed-loop set-ups with simple brain models,
the HBP platform will be the first to couple robots to detailed models of the brain. This will make it possible to
perform experiments exploring the link between low level brain circuitry and high-level function. The first release
of the *Neurorobotics Platform* will offer extremely simple functionality. The majority of technical development work
will focus on the goals fixed for the second release, which will provide a flexible environment in which researchers
can perform experiments using simulated robots connected to different classes of brain model – simplified versions of
the models provided by the Brain Simulation Platform, high level models coming from the
[Cognitive Architectures](https://www.humanbrainproject.eu/de/cognitive-architectures) and
[Theoretical Neuroscience](https://www.humanbrainproject.eu/de/theoretical-neuroscience) sub-projects.

## installation

Obtain the current master branch by downloading the [``.zip`` file](https://github.com/HBPNeurorobotics/BlenderRobotDesigner/archive/master.zip) or using git (you need Python 3 installed). On Linux, for instance, you can run:

    user@host ~/Projects $ git clone git@github.com:HBPNeurorobotics/BlenderRobotDesigner.git
    user@host ~/Projects $ cd BlenderRobotDesigner
    user@host ~/Projects/BlenderRobotDesigner $ pip install -r robotde_signer_plugin/requirements.txt
    user@host ~/Projects/BlenderRobotDesigner $ cd doc
    user@host ~/Projects/BlenderRobotDesigner/doc $ make html

This will build the documentation including the user's and developers manual with further information.

## Features

* **Installer**

 The installer comes in a form of a ``.blend`` file that contains an installer script that can be directly executed from within Blender. That way, it can detect the used operating system and
 Blender version and link the files to the correct location as well as select the
 correct binaries for the platform.
 For more information, refer to the documentation.

* **Robot modeling**

 The robot designer adds functionality to the Blender software with respect to robotics:

 * Kinematic modeling in a scientific/engineering way
  (e.g., entering transformations in *Denavit-Hartenberg* convention)
 * Editing of dynamic properties (center of mass and distribution, friction, etc.)
 * Automatic mesh generation
   * Creation of collision models using geometries with fixed size of vertices and safety distance
   * Convex hull computation
   * Conversion from deformable meshes to rigid bodies. This is useful to transform deformable actors such as those created by [MakeHuman](http://www.makehuman.org/) into robots. This is used to provide a standard humanoid robot model to the NRP.
   * Generation of links and joint geometries based on the kinematic description (*still experimental*).
 * Placing of sensors (*Note: Currently, this includes cameras only. More to follow on request by the NRP and users)


* **File format and ROS/Gazebo support**

 In order to interchange models with the *Neurorobotics platform* the Robot designer has to support additional file
 formats.

 At first, this will be limited to the [unified robot description format (URDF)](http://wiki.ros.org/urdf/XML) format which is very popular among the [Robot Operating System (ROS)](http://wiki.ros.org) community. It will be enriched by additional information tags supported by the [Gazebo](http://gazebosim.org/) simulator–especially for supporting a plugin developed for the NRP to include joint controllers directly in the robot description file. This file support relies on [the PyXB package](http://pyxb.sourceforge.net/)–a software that translates XML scheme definitions (XSD) into a Python document object model. Currently, the RobotDesigner supports export and limited import of these files. Currently, the abstraction from PyXB is in the process of being refactored in order to release URDF support as an independent package and make support of additional file formats much simpler.

 In the future, support for the [Simulator Description Format (SDF)](http://sdformat.org/spec?elem=sdf) file format is planned although conversion in between URDF and SDF [is already possible](http://gazebosim.org/tutorials/?tut=ros_urdf) with Gazebo.



* **Plugin Core Framework**

 Although the RobotEditor is already feature rich, development is cumbersome due to Blender's conventions for plugin design. The ``Plugin Core`` framework is a python package that abstracts and simplifies many of the boiler plate thus allowing the design of larger applications based on Blender.

 Especially the dynamic nature of how functionality is added to Blender makes a modern Python development with IDEs (Integrated Development Environments) such as the excellent [PyCharm<sup>TM</sup>](https://www.jetbrains.com/pycharm/) which support code completion and refactoring difficult. By using decorators ([PEP 0318](https://www.python.org/dev/peps/pep-0318/)) and handlers for [Blender Operators](https://www.blender.org/api/blender_python_api_current/bpy.types.Operator.html#bpy.types.Operator) and [Properties](https://www.blender.org/api/blender_python_api_current/bpy.types.Property.html#bpy.types.Property), and *extended exception handling* and *logging*, developers can easily create even larger projects comfortably. Integration of *external debugging* is planned and currently under development. Further, mock ups for the Blender API can be generated and used for code completion.

 Current development focuses on extending the framework to support [static type checking](https://en.wikipedia.org/wiki/Type_system#Type_checking) using [MyPy](http://mypy-lang.org/) and code analysis ([PyLint](https://www.pylint.org/)) on
 plugin loading.

 The ``Plugin Core`` has an extensive documentation and might be released as a separated project in the future for inclusion in different projects.

* **Documentation**

 The RobotDesigner comes with extensive documentation in form of a user's and developers manual which explains all steps necessary to setup and run the software as well on how to extend it and use the ``Plugin Core`` in general.

## Planned features

One of the key aspects of the ongoing development is data persistence, that is, the ability to store robot models in different file formats and different storage mechanisms.
* GIT integration:
The distributed version control system [GIT](https://git-scm.com/) will be used to directly upload exported models
to a remote repository that can be accessed by the *Neurorobotics Platform*. That way, it will not be necessary
to upload and store robot models and create a seamless integration of the RobotDesigner in the web-based NRP.
* File formats
  * Simulation Description format (see [above's section](File format and ROS/Gazebo support))
  * More file formats will be supported upon demand. By the inclusion and abstraction of the ``PyXB`` interface XML-based systems can be integrated easily.

Furthermore, the *plugin core* framework will be separated from the main project and will be extended to a web application that allows running a sub-set of Blender's design capabilities in a web browser. Work on this has been already initiated.

The installer will be improved to install external dependencies automatically for the installed Blender version.

---
<sup><a name="f1">1</a></sup>Funded by the European Commission through its Cognition Unit under the Information Society Technologies of the seventh Framework Programme (FP7)

<sup><a name="f2">2</a></sup>B. Leon, S. Ulbrich, R. Diankov, G. Puche, M. Przybylski, A. Morales, T. Asfour, S. Moisio, J. Bohg, J. Kuffner and R. Dillmann , *OpenGRASP: A Toolkit for Robot Grasping Simulation,* 2nd International Conference on Simulation, Modeling, and Programming for Autonomous Robots (SIMPAR), November 15, 2010

<sup><a name="f3">3</a></sup>N. Vahrenkamp, M. Kröhnert, S. Ulbrich, T. Asfour, G. Metta, R. Dillmann  and G. Sandini, *Simox: A Robotics Toolbox for Simulation, Motion and Grasp Planning*, International Conference on Intelligent Autonomous Systems (IAS), pp. 585 - 594, 2012

<sup><a name="f4">4</a></sup>C. Mandery, Ö. Terlemez, M. Do, N. Vahrenkamp and T. Asfour, *The KIT Whole-Body Human Motion Database*, International Conference on Advanced Robotics (ICAR), pp. 0 - 0, July, 2015

<sup><a name="f5">5</a></sup>From [the project's website](http://www.humanbrainproject.eu)

<sup><a name="f6">6</a></sup>From [the Neurorobotics website](neurorobotics.net)
