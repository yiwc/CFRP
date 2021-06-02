PACKAGE_NAME = 'CFRP'
# Factories




from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Pins
_PINS = {}
from PyFlow.Packages.CFRP.Pins.DemoPin import DemoPin

# Function based nodes
_NODES = {}
from PyFlow.Packages.CFRP.FunctionLibraries.DemoLib import DemoLib
from PyFlow.Packages.CFRP.FunctionLibraries.ActionLibrary import ActionLibrary
# from PyFlow.Packages.CFRP.FunctionLibraries.ProcControl import ProcControl

# Class based nodes
from PyFlow.Packages.CFRP.Nodes.DemoNode import DemoNode

from PyFlow.Packages.CFRP.Nodes.MOVO import MOVO
_NODES[MOVO.__name__] = MOVO
from PyFlow.Packages.CFRP.Nodes.IIWA import IIWA
_NODES[IIWA.__name__] = IIWA
from PyFlow.Packages.CFRP.Nodes.TurtleBot import TurtleBot
_NODES[TurtleBot.__name__] = TurtleBot
from PyFlow.Packages.CFRP.Nodes.Model_PoseEstimation import PoseEstimation
_NODES[PoseEstimation.__name__] = PoseEstimation
from PyFlow.Packages.CFRP.Nodes.Model_RL_Insert import RL_Insert
_NODES[RL_Insert.__name__] = RL_Insert
from PyFlow.Packages.CFRP.Nodes.Model_YOLO_Detection import YOLO_Detection
_NODES[YOLO_Detection.__name__] = YOLO_Detection
from PyFlow.Packages.CFRP.Nodes.Model_PointCloudClassfication import PointCloudClassfication
_NODES[PointCloudClassfication.__name__] = PointCloudClassfication
from PyFlow.Packages.CFRP.Nodes.ProcControl_SeqExecute import SeqExecute
_NODES[SeqExecute.__name__] = SeqExecute

# Tools
from PyFlow.Packages.CFRP.Tools.DemoShelfTool import DemoShelfTool
from PyFlow.Packages.CFRP.Tools.DemoDockTool import DemoDockTool

_FOO_LIBS = {}
_TOOLS = OrderedDict()
_PREFS_WIDGETS = OrderedDict()
_EXPORTERS = OrderedDict()


_FOO_LIBS[DemoLib.__name__] = DemoLib(PACKAGE_NAME)
_FOO_LIBS[ActionLibrary.__name__] = ActionLibrary(PACKAGE_NAME)

# _NODES[DemoNode.__name__] = DemoNode
# _PINS[DemoPin.__name__] = DemoPin
#
# _TOOLS[DemoShelfTool.__name__] = DemoShelfTool
# _TOOLS[DemoDockTool.__name__] = DemoDockTool


class CFRP(IPackage):
	def __init__(self):
		super(CFRP, self).__init__()

	@staticmethod
	def GetExporters():
		return _EXPORTERS

	@staticmethod
	def GetFunctionLibraries():
		return _FOO_LIBS

	@staticmethod
	def GetNodeClasses():
		return _NODES

	@staticmethod
	def GetPinClasses():
		return _PINS

	@staticmethod
	def GetToolClasses():
		return _TOOLS

