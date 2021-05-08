from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *
from PyFlow.Packages.CFRP.Nodes.ModelNode import Model

class RL_Insert(Model):
    def __init__(self, name):
        super(RL_Insert, self).__init__(name)
        self.name = "RL_Insert"


    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."
