from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *

class Robot(NodeBase):
    def __init__(self, name):
        super(Robot, self).__init__(name)
        self.inp = self.createInputPin('Activate', 'ExecPin')
        self.out = self.createOutputPin('Execute', 'ExecPin')
        # self.obj = self.createOutputPin('obj',"AnyPin")
        self.obj = self.createOutputPin('obj',"StringPin")

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('ExecPin')
        helper.addOutputDataType('ExecPin')
        helper.addInputStruct(StructureType.Single)
        helper.addOutputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'Robot'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    def compute(self, *args, **kwargs):
        inputData = self.inp.getData()
        self.out.call()
        self.obj.setData(self)
