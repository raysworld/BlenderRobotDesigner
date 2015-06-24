"""
Module for importing robots specified in the URDF file format.
"""

__author__ = 'Stefan Ulbrich'
import sys

from . import urdf_dom

def set_value(l):
    """
    helper function that creates a string out of a list of floats
    :param l: python list of floats
    :return: string representing the list
    """
    return ' '.join(i for i in l)


class URDFTree(object):
    """
    A class that parses and represents a robot described by a URDF file.
    The data is stored in a tree of linked instances of this class. Therefore, a root element (or several) has to be
    detectable in the file excluding closed kinematic loops at the moment.
    Each instance represents a *blender/RobotDesigner bone* that is a compound of joint and link.
    It uses a document object model (DOM) created by generateDS.py (in version 2.14a -- the newest
    that does not depend on the lxml module, which is not included in blender).
    """

    def __init__(self, connected_joints, connected_links, robot=None):
        """ Constructor
        :param root: if specified, the constructor copies the cross-references in the XML file from another
        URDFTree instance.
        :param connected_joints: If specified, the connectedJoints (cross-reference in the XML file) is set.
        :param connected_links: If specified, the connectedLinks (cross-reference in the XML file) is set.
        :return:
        """
        # super(URDFTree, self).__init__()
        self.children = []

        self.robot = robot
        self.joint = None
        self.link = None

        self.connectedLinks = connected_links
        self.connectedJoints = connected_joints

    @staticmethod
    def parse(file_name):
        """ Parses a URDF file and builds up a tree representing the kinematic structure of a robot.
        Explanation: The URDF file format stores links (i.e., rigid bodies) and joints (i.e., connection between links)
        in a flat structure (as opposed to a tree data structure). Links have no references while joints refer to the
        NAMES of have exactly one parent (link) and child (link). This method first resolves these cross references
        and calls the recursive URDFTree.build() method to create a tree-like data structure representing the
        kinematic tree(s) of the robot.
        :param file_name: the name of the file to open
        """

        # read the file
        robot = urdf_dom.parse(file_name, silence=True)

        # create mapping from (parent) links to joints
        connected_joints = {link: [joint for joint in robot.joint if link.name == joint.parent.link] for link
                            in robot.link}

        # create mapping from joints to their child links
        connected_links = {joint: link for link in robot.link for joint in robot.joint if
                           link.name == joint.child.link}

        # find root links (i.e., links that are NOT connected to a joint)
        child_links = [link.name for link in robot.link for joint in robot.joint if
                       link.name == joint.child.link]
        root_links = [link for link in robot.link if link.name not in child_links]


        kinematic_chains = []

        for link in root_links:
            tree = URDFTree(connected_links=connected_links, connected_joints=connected_joints, robot=robot)
            kinematic_chains.append(tree)
            for joint in connected_joints[link]:
                tree.build(connected_links[joint], joint)

        return robot.name, root_links, kinematic_chains

    def build(self, link, joint=None):
        """
        Recursive function that builds up the tree representation of the robot. You do not have to call it manually (
        Called by parse).
        :param link: The link the kinematics subtree starts with
        :param joint: The joint connecting to the previous link (if any)
        """
        self.children = []
        self.joint = joint
        self.link = link
        self.set_defaults()

        children = self.connectedJoints[link]
        for joint in children:
            tree = URDFTree(connected_links=self.connectedLinks, connected_joints=self.connectedJoints, robot=self.robot)
            self.children.append(tree)
            tree.build(self.connectedLinks[joint], joint)

    @staticmethod
    def create_empty(name):

        tree = URDFTree(connected_links={}, connected_joints={}, robot=urdf_dom.robot())
        tree.robot.name = name
        tree.link = urdf_dom.link()
        tree.link.name = "base_link"
        tree.robot.link.append(tree.link)
        tree.joint = urdf_dom.joint()
        tree.set_defaults()
        return tree


    def write(self, file_name):
        """
        Should only be called on the root element.
        :param file_name:
        :return:
        """

        for joint, link in self.connectedLinks.items():
            joint.child.link = link.name

        for link, joints in self.connectedJoints.items():
            for joint in joints:
                joint.parent.link = link.name

        # Connect root joints to self.link (the root link)
        for joint in self.robot.joint:
            if joint.parent is None:
                joint.parent = self.link.name

        with open(file_name,"w") as f:
            f.write('<?xml version="1.0" ?>')
            self.robot.export(f,0)


    def _write(self):
        """
        Recursion that builds the creates the cross links for the DOM (might not be necessary)
        """
        pass

    def add(self):
        """
        Creates and adds another URDFTree instance to this node. Do not add children to the subtree manually as
        references are not created then. Note that if there is no robot member defined yet (i.e., you are *exporting*),
        it will be created automatically.
        :param link: a urdf_dom link element
        :param joint: a urdf_dom joint element
        :return: a reference to the newly created URDFTree instance.
        """

        tree = URDFTree(connected_links=self.connectedLinks, connected_joints=self.connectedJoints, robot=self.robot)
        tree.joint = urdf_dom.joint()
        tree.link = urdf_dom.link()
        tree.robot.link.append(tree.link)
        tree.robot.joint.append(tree.joint)
        tree.set_defaults()
        tree.joint.child = urdf_dom.child()
        tree.joint.parent = urdf_dom.parent()

        self.connectedLinks[tree.joint] = tree.link
        if self.link in self.connectedJoints:
            self.connectedJoints[self.link].append(tree.joint)
        else:
            self.connectedJoints[self.link] = [tree.joint]

        return tree

    def add_mesh(self, file_name):
        """

        :param link:
        :return:
        """
        visual = urdf_dom.visual()
        self.link.visual.append(visual)
        visual.geometry = urdf_dom.geometry()
        visual.origin = urdf_dom.pose()
        visual.geometry.mesh = urdf_dom.mesh()
        visual.geometry.mesh.filename = file_name
        return visual

    def set_defaults(self):
        """
        Adds some default values to the DOM.
        """

        joint = self.joint
        link = self.link
        if joint.axis is None:
            joint.axis = urdf_dom.axis()

        if joint.limit is None:
            joint.limit = urdf_dom.limit()

        if joint.calibration is None:
            joint.calibraiton = urdf_dom.calibration()
            # joint.calibration.rising  # there are no default values in the XSD?
            # joint.calibration.falling

        if joint.origin is None:
            joint.origin = urdf_dom.pose()

        for visual in link.visual:
            if visual.origin is None:
                visual.origin = urdf_dom.pose()

        if joint.dynamics is None:
            joint.dynamics = urdf_dom.dynamics()

            # if joint.mimic is None: # truely optional
            # if joint.safety_controller is None: # ignored

            # if link.inertial is None:

            # todo continue and remove if statements from urdf_blender

    def show(self, depth=0):
        """
        Prints the kinematic tree to the command line (for debugging).
        This function serves as an example for export export.
        :param depth: the depth of the kinematics sub tree for indention
        """
        if depth > 1:
            print(
                "%s, link: %s, joint: %s, type: %s" % ("*" * depth, self.link.name, self.joint.name, self.joint.type_))
        elif depth == 1:
            print("Root link: %s" % self.link.name)
        for tree in self.children:
            tree.show(depth + 1)

# debugging the module
if __name__ == "__main__":
    robot = URDFTree()
    robot.parse("../../models/hollie.urdf")
    robot.show()