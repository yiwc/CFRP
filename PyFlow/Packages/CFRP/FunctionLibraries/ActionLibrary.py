from PyFlow.Core.Common import *
from PyFlow.Core import FunctionLibraryBase
from PyFlow.Core import IMPLEMENT_NODE
# from HRClib.hrclib_client_v6 import odyssey_Interface,odyssey_interface_dummy
from HRClib.hrclib_client_v6 import odyssey_Interface
import rospy

PIN_ALLOWS_ANYTHING = {
    PinSpecifires.ENABLED_OPTIONS: PinOptions.AllowAny | PinOptions.ArraySupported | PinOptions.DictSupported}


class ActionLibrary(FunctionLibraryBase,odyssey_Interface):
    '''doc string for DemoLib'''
    print(12)
    rospy.init_node("test")
    print('ok')
    Odyssey = odyssey_Interface()
    # Odyssey =odyssey_interface_dummy()

    def __init__(self, packageName):
        super(ActionLibrary, self).__init__(packageName)
        # odyssey_interface_dummy.__init__(self)
        # self.Odyssey = odyssey_interface_dummy()

    @staticmethod
    @IMPLEMENT_NODE(returns=None, nodeType=NodeTypes.Callable,
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    def Hi(robot=('AnyPin', "Robot", PIN_ALLOWS_ANYTHING.copy())):
        print("Robot say: Hi!")

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    nodeType=NodeTypes.Callable,
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    def set_dual_grippers(
            robot=('StringPin', "Robot", PIN_ALLOWS_ANYTHING.copy()),
            value=('FloatPin', 1.0),

    ):
        '''Returns attribute from object using "getattr(name)"'''

        ActionLibrary.Odyssey._L0_dual_set_gripper(value=value, wait=True)
        print("{} Gripper set to->{} ".format(robot, value))
        # Odyssey_Interface_Dummy = odyssey_interface_dummy()
        # Odyssey_Interface_Dummy._L0_dual_set_gripper(value=value, wait=True)
        # return getattr(obj, name)
        return True

    # @staticmethod
    # @IMPLEMENT_NODE(returns=None, nodeType=NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'ActionLibrary', NodeMeta.KEYWORDS: []})
    # def set_grippers():
    #     print("Robot say: Hi!")

    # @staticmethod
    # @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()), meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    # def set_grippers(robot=('AnyPin', "Robot", PIN_ALLOWS_ANYTHING.copy()),
    #                  # value=('FloatPin', 'Value/0~1')
    #                  value=('FloatPin', 0)
    #                  ):
    #     '''Returns attribute from object using "getattr(name)"'''
    #
    #     print("{} Gripper set to->{}".format(robot.name,value))
    #     # return getattr(obj, name)
    #     return True

    ### L0_Library
    ###

    # @staticmethod
    # @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
    #                 nodeType=NodeTypes.Callable,
    #                 meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    # def set_dual_grippers(
    #                       robot=('StringPin', "Robot", PIN_ALLOWS_ANYTHING.copy()),
    #                       value=('FloatPin', 0.0),
    #                       ):
    #     '''Returns attribute from object using "getattr(name)"'''
    #
    #     print("{} Gripper set to->{} ".format(robot, value))
    #     Odyssey_Interface_Dummy = odyssey_interface_dummy()
    #     Odyssey_Interface_Dummy._L0_dual_set_gripper(value=value, wait=True)
    #
    #     # print("{} Gripper set to->{}".format(robot, value))
    #
    #     # return getattr(obj, name)
    #     return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    nodeType=NodeTypes.Callable,
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    def dual_jp_move_safe_relate(
            robot=('AnyPin', "Robot", PIN_ALLOWS_ANYTHING.copy()),
            jp_r=('StringPin', "[0,-0.2,0,0,-0.06,1.8,0]", PIN_ALLOWS_ANYTHING.copy()),
            jp_l=('StringPin', "[0,0.2,0,0,0.06,-1.8,0]", PIN_ALLOWS_ANYTHING.copy()),
            lmaxforce=('StringPin', "[10,10,10,5,5,5]", PIN_ALLOWS_ANYTHING.copy()),
            rmaxforce=('StringPin', "[10,10,10,5,5,5]", PIN_ALLOWS_ANYTHING.copy()),
            duration=('FloatPin', 3, PIN_ALLOWS_ANYTHING.copy())):
        '''Returns attribute from object using "getattr(name)"'''
        # print("{} {} {} {} {} {}".format(robot, jp_r, jp_l, lmaxforce, rmaxforce, duration))
        # Odyssey_Interface_Dummy1 = odyssey_interface_dummy()
        # Odyssey_Interface_Dummy1._L0_dual_jp_move_safe_relate(jp_r=jp_r, jp_l=jp_l, lmaxforce=lmaxforce,
        #                                                       rmaxforce=rmaxforce, duration=duration, wait=True,
        #                                                       hard=False)
        jp_l=eval(jp_l)
        jp_r=eval(jp_r)
        lmaxforce=eval(lmaxforce)
        rmaxforce=eval(rmaxforce)
        ActionLibrary.Odyssey._L0_dual_jp_move_safe_relate(jp_r=jp_r, jp_l=jp_l, lmaxforce=lmaxforce,
                                                              rmaxforce=rmaxforce, duration=duration, wait=True,
                                                              hard=False)

        # print("{} Gripper set to->{}".format(robot.name, value))
        # print("{} Gripper set to->{}".format(robot, value))
        # return getattr(obj, name)
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    nodeType=NodeTypes.Callable,
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    def single_task_move_safe(
            robot=('AnyPin', "Robot", PIN_ALLOWS_ANYTHING.copy()),
            arm=('StringPin', "left", PIN_ALLOWS_ANYTHING.copy()),
            pos=('StringPin', "[0.444+0.3,0.130,0.8]", PIN_ALLOWS_ANYTHING.copy()),
            orn=('StringPin', "[math.pi/2,0,0]", PIN_ALLOWS_ANYTHING.copy()),
            maxforce=('StringPin', "[20,20,20,20,20,20]", PIN_ALLOWS_ANYTHING.copy())
    ):
        '''Returns attribute from object using "getattr(name)"'''
        # print("{} {} {} {} {} {}".format(robot, jp_r, jp_l, lmaxforce, rmaxforce, duration))
        # Odyssey_Interface_Dummy1 = odyssey_interface_dummy()

        pos=eval(pos)
        orn=eval(orn)
        maxforce=eval(maxforce)
        ActionLibrary.Odyssey._L0_single_task_move_safe(arm=arm, pos=pos, orn=orn, maxforce=maxforce, wait=True,
                                                           hard=False)

        # print("{} Gripper set to->{}".format(robot.name, value))
        # print("{} Gripper set to->{}".format(robot, value))
        # return getattr(obj, name)
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    nodeType=NodeTypes.Callable,
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    def dual_task_move_safe_relate(
            robot=('AnyPin', "Robot", PIN_ALLOWS_ANYTHING.copy()),
            lmove=('StringPin', '[0.15,0.1,0.15]', PIN_ALLOWS_ANYTHING.copy()),
            rmove=('StringPin', '[0.15,-0.1,0.15]', PIN_ALLOWS_ANYTHING.copy()),
            time=('FloatPin', 3, PIN_ALLOWS_ANYTHING.copy()),
            rmaxforce=('StringPin', '[10,10,10,10,10,10]', PIN_ALLOWS_ANYTHING.copy()),
            lmaxforce=('StringPin', '[10,10,10,10,10,10]', PIN_ALLOWS_ANYTHING.copy())
    ):
        '''Returns attribute from object using "getattr(name)"'''
        # print("{} {} {} {} {} {}".format(robot, jp_r, jp_l, lmaxforce, rmaxforce, duration))
        # Odyssey_Interface_Dummy1 = odyssey_interface_dummy()
        lmove=eval(lmove)
        rmove=eval(rmove)
        # time=float(time)
        rmaxforce=eval(rmaxforce)
        lmaxforce=eval(lmaxforce)
        ActionLibrary.Odyssey._L0_dual_task_move_safe_relate(lmove=lmove, rmove=rmove, time=time,
                                                                rmaxforce=rmaxforce, lmaxforce=lmaxforce, wait=True,
                                                                hard=False)

        # print("{} Gripper set to->{}".format(robot.name, value))
        # print("{} Gripper set to->{}".format(robot, value))
        # return getattr(obj, name)
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    nodeType=NodeTypes.Callable,
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    def upper_jp_move_safe(
            robot=('AnyPin', "Robot", PIN_ALLOWS_ANYTHING.copy()),
            jpl=('StringPin', "[1.1 ,1.5, -0.1, 2.1, 0, -0.6, 1.69]", PIN_ALLOWS_ANYTHING.copy()),
            jpr=('StringPin', "[-1.1,-1.5,0.1, -2.1, 0, 0.6, -1.69]", PIN_ALLOWS_ANYTHING.copy()),
            jph=('StringPin', "[9.853695701167453e-06, -0.602746069431304]", PIN_ALLOWS_ANYTHING.copy()),
            jplinear=('StringPin', "0.2585753381252289", PIN_ALLOWS_ANYTHING.copy()),
            duration=('StringPin', "10.0", PIN_ALLOWS_ANYTHING.copy()),
            lforce=('StringPin', "[10,10,10,10,10,10]", PIN_ALLOWS_ANYTHING.copy()),
            rforce=('StringPin', "[10,10,10,10,10,10]", PIN_ALLOWS_ANYTHING.copy())):
        '''Returns attribute from object using "getattr(name)"'''
        # Odyssey_Interface_Dummy1 = odyssey_interface_dummy()
        jpl=eval(jpl)
        jpr=eval(jpr)
        jph=eval(jph)
        duration=float(duration)
        jplinear=float(jplinear)
        lforce=eval(lforce)
        rforce=eval(rforce)
        ActionLibrary.Odyssey._L0_upper_jp_move_safe(jpl=jpl, jpr=jpr, jph=jph, jplinear=jplinear, duration=duration,
                                                        lforce=lforce, rforce=rforce, wait=True, hard=False)
        # print("{} Gripper set to->{}".format(robot.name, value))
        # print("{} Gripper set to->{}".format(robot, value))
        # return getattr(obj, name)
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    nodeType=NodeTypes.Callable,
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    def set_single_gripper(
            robot=('AnyPin', "Robot", PIN_ALLOWS_ANYTHING.copy()),
            rl=('StringPin', "r/l"),
            value=('FloatPin', 0.0)):
        '''Returns attribute from object using "getattr(name)"'''
        # Odyssey_Interface_Dummy1 = odyssey_interface_dummy()
        ActionLibrary.Odyssey._L0_gripper(rl=rl, value=value)
        # print("{} Gripper set to->{}".format(robot.name, value))
        # print("{} Gripper set to->{}".format(robot, value))
        # return getattr(obj, name)
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    nodeType=NodeTypes.Callable,
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    def arm_cart_move(robot=("AnyPin", "Robot", PIN_ALLOWS_ANYTHING.copy()),
                      arm=('StringPin', "Arm (l/r)"),
                      pos=('AnyPin', "pos=[x,y,z]"),
                      orn=('AnyPin', "orn=[a,b,c,g]"),
                      maxforce=('AnyPin', "maxforce=[Fx,Fy,Fz,Fr,Fp,Fy]"),
                      wait=('BoolPin', "wait=True/False")
                      ):
        '''Returns attribute from object using "getattr(name)"'''
        print("Robot {} execute arm_cart_move to pos={} orn ={} with maxforce ={}".format(
            robot.name, arm, pos, orn, maxforce
        ))

        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L0', NodeMeta.KEYWORDS: []})
    def base_move(robot=("AnyPin", "Robot", PIN_ALLOWS_ANYTHING.copy())
                  ):
        '''Returns attribute from object using "getattr(name)"'''
        return True

    ### L1 Library
    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    nodeType=NodeTypes.Callable,
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L1', NodeMeta.KEYWORDS: []})
    def single_task_move_safe_relate(
            robot=('AnyPin', "Robot", PIN_ALLOWS_ANYTHING.copy()),
            arm=('StringPin', "Arm (l/r)"),
            move=('AnyPin', "move=[x,y,z]", PIN_ALLOWS_ANYTHING.copy()),
            maxforce=('AnyPin', "maxforce=[Fx,Fy,Fz,Fr,Fp,Fy]"),
            time=('AnyPin', "time=xxs", PIN_ALLOWS_ANYTHING.copy()), ):
        '''Returns attribute from object using "getattr(name)"'''
        # Odyssey_Interface_Dummy1 = odyssey_interface_dummy()
        ActionLibrary.Odyssey._L1_single_task_move_safe_relate(arm=arm, move=move, maxforce=maxforce, time=time,
                                                                  wait=True, hard=False)
        # print("{} Gripper set to->{}".format(robot.name, value))
        # print("{} Gripper set to->{}".format(robot, value))
        # return getattr(obj, name)
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L1', NodeMeta.KEYWORDS: []})
    def Pick(robot=("AnyPin", "Robot", PIN_ALLOWS_ANYTHING.copy()),
             execute=('ExecPin', "Execute")
             ):
        '''Returns attribute from object using "getattr(name)"'''
        print("Do Pick")
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L1', NodeMeta.KEYWORDS: []})
    def Place(robot=("AnyPin", "Robot", PIN_ALLOWS_ANYTHING.copy()),
              execute=('ExecPin', "Execute")
              ):
        print("Do Place")
        '''Returns attribute from object using "getattr(name)"'''
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L1', NodeMeta.KEYWORDS: []})
    def Insert(robot=("AnyPin", "Robot", PIN_ALLOWS_ANYTHING.copy())
               ):
        '''Returns attribute from object using "getattr(name)"'''
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L1', NodeMeta.KEYWORDS: []})
    def Screw(robot=("AnyPin", "Robot", PIN_ALLOWS_ANYTHING.copy())
              ):
        '''Returns attribute from object using "getattr(name)"'''
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L2', NodeMeta.KEYWORDS: []})
    def PickInsertScrew(robot=("AnyPin", "Robot", PIN_ALLOWS_ANYTHING.copy())
                        ):
        '''Returns attribute from object using "getattr(name)"'''
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('AnyPin', None, PIN_ALLOWS_ANYTHING.copy()),
                    meta={NodeMeta.CATEGORY: 'ActionLibrary-L2', NodeMeta.KEYWORDS: []})
    def PickInsert(robot=("AnyPin", "Robot", PIN_ALLOWS_ANYTHING.copy())
                   ):
        '''Returns attribute from object using "getattr(name)"'''
        return True
