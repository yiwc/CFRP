from PyFlow.Core.Common import *
from PyFlow.Core import FunctionLibraryBase
from PyFlow.Core import IMPLEMENT_NODE

PIN_ALLOWS_ANYTHING = {PinSpecifires.ENABLED_OPTIONS: PinOptions.AllowAny | PinOptions.ArraySupported | PinOptions.DictSupported}



class ActionLibrary(FunctionLibraryBase):
    '''doc string for DemoLib'''

    def __init__(self, packageName):
        super(ActionLibrary, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=None, nodeType=NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    def Hi(robot=('AnyPin', "Robot", PIN_ALLOWS_ANYTHING.copy())):
        print("Robot say: Hi!")

    # @staticmethod
    # @IMPLEMENT_NODE(returns=None, nodeType=NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'ActionLibrary', NodeMeta.KEYWORDS: []})
    # def set_grippers():
    #     print("Robot say: Hi!")

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()), meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    def set_grippers(robot=('AnyPin', "Robot", PIN_ALLOWS_ANYTHING.copy()),
                     value=('FloatPin', 'Value/0~1')
                     ):
        '''Returns attribute from object using "getattr(name)"'''

        print("{} Gripper set to->{}".format(robot.name,value))
        # return getattr(obj, name)
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()), meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    def arm_cart_move(robot=("AnyPin","Robot", PIN_ALLOWS_ANYTHING.copy()),
                      arm=('StringPin', "Arm (l/r)"),
                      pos=('AnyPin',"pos=[x,y,z]"),
                      orn=('AnyPin',"orn=[a,b,c,g]"),
                      maxforce=('AnyPin',"maxforce=[Fx,Fy,Fz,Fr,Fp,Fy]"),
                      wait=('BoolPin',"wait=True/False")
                     ):
        '''Returns attribute from object using "getattr(name)"'''
        print("Robot {} execute arm_cart_move to pos={} orn ={} with maxforce ={}".format(
            robot.name,arm,pos,orn,maxforce
        ))

        return True



    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()), meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    def base_move(robot=("AnyPin","Robot", PIN_ALLOWS_ANYTHING.copy())
                     ):
        '''Returns attribute from object using "getattr(name)"'''
        return True


    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()), meta={NodeMeta.CATEGORY: 'ActionLibrary-L1', NodeMeta.KEYWORDS: []})
    def Pick(robot=("AnyPin","Robot", PIN_ALLOWS_ANYTHING.copy()),
             execute=('ExecPin', "Execute")
                     ):
        '''Returns attribute from object using "getattr(name)"'''
        print("Do Pick")
        return True


    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()), meta={NodeMeta.CATEGORY: 'ActionLibrary-L1', NodeMeta.KEYWORDS: []})
    def Place(robot=("AnyPin","Robot", PIN_ALLOWS_ANYTHING.copy()),
              execute=('ExecPin', "Execute")
                     ):

        print("Do Place")
        '''Returns attribute from object using "getattr(name)"'''
        return True


    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()), meta={NodeMeta.CATEGORY: 'ActionLibrary-L1', NodeMeta.KEYWORDS: []})
    def Insert(robot=("AnyPin","Robot", PIN_ALLOWS_ANYTHING.copy())
                     ):
        '''Returns attribute from object using "getattr(name)"'''
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()), meta={NodeMeta.CATEGORY: 'ActionLibrary-L1', NodeMeta.KEYWORDS: []})
    def Screw(robot=("AnyPin","Robot", PIN_ALLOWS_ANYTHING.copy())
                     ):
        '''Returns attribute from object using "getattr(name)"'''
        return True


    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()), meta={NodeMeta.CATEGORY: 'ActionLibrary-L2', NodeMeta.KEYWORDS: []})
    def PickInsertScrew(robot=("AnyPin","Robot", PIN_ALLOWS_ANYTHING.copy())
                     ):
        '''Returns attribute from object using "getattr(name)"'''
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()), meta={NodeMeta.CATEGORY: 'ActionLibrary-L2', NodeMeta.KEYWORDS: []})
    def PickInsert(robot=("AnyPin","Robot", PIN_ALLOWS_ANYTHING.copy())
                     ):
        '''Returns attribute from object using "getattr(name)"'''
        return True


