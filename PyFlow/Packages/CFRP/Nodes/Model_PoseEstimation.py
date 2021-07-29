from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *
from PyFlow.Packages.CFRP.Nodes.ModelNode import Model

class PoseEstimation(Model):
    def __init__(self, name):
        super(PoseEstimation, self).__init__(name)
        self.name = "PoseEstimation"


    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."
