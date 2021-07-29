from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *
from PyFlow.Packages.CFRP.Nodes.RobotNode import Robot


class TurtleBot(Robot):
    def __init__(self, name):
        super(TurtleBot, self).__init__(name)
        self.name = "TurtleBot"
        self.obj.setData("TurtleBot")

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."
