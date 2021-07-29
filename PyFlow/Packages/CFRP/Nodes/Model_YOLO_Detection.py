from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *
from PyFlow.Packages.CFRP.Nodes.ModelNode import Model

class YOLO_Detection(Model):
    def __init__(self, name):
        super(YOLO_Detection, self).__init__(name)
        self.name = "YOLO_Detection"


    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."
