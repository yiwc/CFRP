from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *

from PyFlow.Packages.CFRP.Nodes.RobotNode import Robot

class IIWA(Robot):
    def __init__(self, name):
        super(IIWA, self).__init__(name)
        self.name = "IIWA"
        self.obj.setData("IIWA")

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."
