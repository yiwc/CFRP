from PyFlow.Core.Common import *
from PyFlow.Core import FunctionLibraryBase
from PyFlow.Core import IMPLEMENT_NODE

import torchvision.transforms as transforms
import torchvision.models as models
import torch
from PIL import Image   # (R, G, B)

PIN_ALLOWS_ANYTHING = {
    PinSpecifires.ENABLED_OPTIONS: PinOptions.AllowAny | PinOptions.ArraySupported
                                   | PinOptions.DictSupported | PinOptions.TensorSupported}


class DeepLearningLib(FunctionLibraryBase):
    def __init__(self, packageName):
        super(DeepLearningLib, self).__init__(packageName)
        self.name = "DeepLearning"

    @staticmethod
    @IMPLEMENT_NODE(returns=('StringPin', ''),
                    meta={NodeMeta.CATEGORY: 'DeepLearningLib',
                          NodeMeta.KEYWORDS: []})
    def makeURL(URL=('StringPin', '')):
        '''Make URL(string).'''
        print("URL set to -> {}".format(URL))
        return URL
    #refer from makestring

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                      meta={NodeMeta.CATEGORY: 'DeepLearningLib',
                            NodeMeta.KEYWORDS: []})
    def image_to_tensor(address=("AnyPin", None, PIN_ALLOWS_ANYTHING.copy())):
        '''Returns tensor from URL.jpg'''
        image = Image.open(address)  # 打开文件夹中图片,URL
        print('(W，H) = ', image.size)  # (W，H)
        tran = transforms.ToTensor()  # 调用
        img_tensor = tran(image)  # 将PIL.Image读的图片转换成(C,H,W)的Tensor格式且/255归一化到[0,1.0]之间
        print('(C，H, W) = ', img_tensor.size())  # (C，H, W), 通道顺序（R,G,B)
        print('归一化', img_tensor)  # 通道顺序（R,G,B)，/255归一化到[0,1.0]之间
        return img_tensor

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                      meta={NodeMeta.CATEGORY: 'DeepLearningLib',
                            NodeMeta.KEYWORDS: []})
    def resnet18(img_tensor=("AnyPin", None, PIN_ALLOWS_ANYTHING.copy())):
        '''import tensor to resnet18'''
        # tensor = img_tensor.strip('"')
        input = torch.unsqueeze(img_tensor, dim=0)  # 增加1个维度
        resnet18 = models.resnet18()  # 调用
        output = resnet18(input)
        print('resnet18_output', output)
        return output
