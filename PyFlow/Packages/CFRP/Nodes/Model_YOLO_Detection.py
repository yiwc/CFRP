from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *
# import os
from PyFlow.Packages.CFRP.Nodes.YOLO_BIPA.BS3_yolo_client import *


class YOLO_Detection(NodeBase):
    def __init__(self, name):
        super(YOLO_Detection, self).__init__(name)
        self.inExec = self.createInputPin('Activate', 'ExecPin', None, self.compute)
        self.address = self.createInputPin('address', 'StringPin', structure=StructureType.Single)
        # self.sudo = self.createInputPin('sudo', 'StringPin', structure=StructureType.Single)
        # self.address.enableOptions(PinOptions.AllowAny)

        self.obj = self.createOutputPin('object', "AnyPin", structure=StructureType.Multi)
        self.obj.enableOptions(PinOptions.AllowAny)
        self.out = self.createOutputPin('output', 'AnyPin', structure=StructureType.Multi)
        self.out.enableOptions(PinOptions.AllowAny)
        # self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')

        # passcode = self.sudo.getData()
        global a
        a = YOLO_CLIENT()
        # os.popen("sudo -S %s" % ('docker run --rm -p 8000:8081 yolo-v2'), 'w').write(passcode)
        # os.popen("sudo -S %s" % ('docker run --rm -p 8000:8081 yolo-v2'), 'w').write('123456')

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('ExecPin')
        helper.addInputDataType('AnyPin')
        helper.addOutputDataType('AnyPin')
        helper.addInputStruct(StructureType.Multi)
        helper.addInputStruct(StructureType.Single)
        helper.addOutputStruct(StructureType.Multi)
        return helper

    @staticmethod
    def category():
        return 'ML/DL'

    @staticmethod
    def keywords():
        return ['print']

    @staticmethod
    def description():
        return "Model_YOLO_Detection"

    def compute(self, *args, **kwargs):
        img = np.random.randint(0, 255, [128, 128, 3]).astype(np.uint8)
        import cv2
        url = self.address.getData()
        img = cv2.imread(url)
        img = cv2.resize(img, (128, 128))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = a.gen(img)
        print(result)

        self.out.setData(result)
        return result