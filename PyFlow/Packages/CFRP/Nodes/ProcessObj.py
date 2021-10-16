from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *

import threading

class AnObject(NodeBase):
    def __init__(self, name):
        super(AnObject, self).__init__(name)
        self.inExec = self.createInputPin("Start", 'ExecPin', None, self.start)
        self.inExec = self.createInputPin("Stop", 'ExecPin', None, self.stop)
        self.entity = self.createInputPin('WordsInput', 'StringPin', defaultValue="Speaker Loaded!",structure=StructureType.Multi)

        self.brunning=False

        thr=threading.Thread(target=self.work)
        thr.start()

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        return helper

    @staticmethod
    def category():
        return 'Tests'

    def start(self, *args, **kwargs):
        self.brunning=True
        pass

    def stop(self, *args, **kwargs):
        pass
        self.brunning=False

    def work(self, *args, **kwargs):
        while True:
            time.sleep(1)
            if self.brunning == False:
                continue
            if self.entity.getData() !="":
                print("your object is working ...")
                print("text is -> {}".format(self.entity.getData()))
                self.entity.setData("")


class ProcessObj(NodeBase):
    def __init__(self, name):
        super(ProcessObj, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.work)
        self.entity = self.createInputPin('entity', 'AnyPin', structure=StructureType.Multi)
        self.entity.enableOptions(PinOptions.AllowAny)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')

        self.WordsToSay = self.createOutputPin("WordsToSay",'StringPin')

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        return helper

    @staticmethod
    def category():
        return 'Tests'

    def work(self, *args, **kwargs):
        print("processObj Compute..")
        # print(self.entity.getData())
        # obj=self.entity.getData()
        # obj.set_text("Pick a Bolt")
        self.WordsToSay.setData("Pick a Bolt")
