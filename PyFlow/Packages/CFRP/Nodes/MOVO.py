from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *
from PyFlow.Packages.CFRP.Nodes.RobotNode import Robot


class MOVO(Robot):
    def __init__(self, name):
        super(MOVO, self).__init__(name)
        self.name = "MOVO"
        # self.obj.setName(name='obj')
        self.obj.setData("MOVO")



    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."


