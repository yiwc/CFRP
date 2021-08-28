from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *

import torchvision.transforms as transforms
import torchvision.models as models
import torch
from PIL import Image   # (R, G, B)


class resnet18(NodeBase):
    def __init__(self, name):
        super(resnet18, self).__init__(name)
        self.inExec = self.createInputPin('Activate', 'ExecPin', None, self.compute)
        self.address = self.createInputPin('address', 'StringPin', structure=StructureType.Single)
        # self.address.enableOptions(PinOptions.AllowAny)

        self.obj = self.createOutputPin('object', "AnyPin", structure=StructureType.Multi)
        self.obj.enableOptions(PinOptions.AllowAny)
        self.out = self.createOutputPin('output', 'AnyPin', structure=StructureType.Multi)
        self.out.enableOptions(PinOptions.AllowAny)
        # self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')

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
        return "Model_resnet18"

    def compute(self, *args, **kwargs):
        image = Image.open(self.address.getData())  # 打开文件夹中图片,URL
        print('(W，H) = ', image.size, type(image.size))  # (W，H)
        tran = transforms.ToTensor()  # 调用
        img_tensor = tran(image)  # 将PIL.Image读的图片转换成(C,H,W)的Tensor格式且/255归一化到[0,1.0]之间
        print('(C，H, W) = ', img_tensor.size(), type(img_tensor.size()))  # (C，H, W), 通道顺序（R,G,B)
        print('归一化\t', img_tensor, '\ntype:', type(img_tensor))  # 通道顺序（R,G,B)，/255归一化到[0,1.0]之间
        in_tensor = torch.unsqueeze(img_tensor, dim=0)  # 增加1个维度
        resnet18 = models.resnet18()  # 调用
        out_tensor = resnet18(in_tensor)
        print('resnet18_output\t', out_tensor, '\ntype:', type(out_tensor))
        self.out.setData(out_tensor)
        return out_tensor