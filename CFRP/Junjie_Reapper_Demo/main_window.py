import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QDesktopWidget, QWidget, QDockWidget, QTabWidget, \
    QMenu, QVBoxLayout
# from Junjie_Reapper_Demo import Center_Function
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from Junjie_Reapper_Demo.Controller import Ui_COntroller
from Junjie_Reapper_Demo.application_library import Ui_application_library
from Junjie_Reapper_Demo.States import Ui_States
from Junjie_Reapper_Demo.Simulation import Ui_Simulation
from Junjie_Reapper_Demo.Operator import Ui_Operator
from Junjie_Reapper_Demo.Camera_View import Ui_Camera_View
from Junjie_Reapper_Demo.Task_Planner import Ui_Task_Planner
# import PyFlow
from PyFlow.App import PyFlow
import threading, time
import rospy

class main_window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.IntUI()
        self.instance = PyFlow.instance(software="standalone")
        self.menu_bar_setting()
        self.fCenter()
        self.on_app_library_btn_clicked()
        # self.Allclose()
        # self.instance = PyFlow.instance(software="standalone")

    def IntUI(self):
        # size parameter
        # self.showMaximized()
        # initiate Widgets
        self.Controller_UI = QWidget()
        self.App_Library_UI = QWidget()
        self.State_UI = QWidget()
        self.Simulation_UI = QWidget()
        self.Operator_UI = QWidget()
        self.Camera_View_UI = QWidget()
        self.Task_Planner_UI = QWidget()

        # instance the class transfered (实例化调用的class)
        self.ui_controller = Ui_COntroller()
        self.ui_app_library = Ui_application_library()
        self.ui_state = Ui_States()
        self.ui_simluation = Ui_Simulation()
        self.ui_operator = Ui_Operator()
        self.ui_camera_view = Ui_Camera_View()
        self.ui_task_planner = Ui_Task_Planner()

        # create the designed windows
        # this method is also ok:
        # self.controller = Ui_COntroller.setupUi(self.ui_controller, self.Controller_UI)
        self.ui_controller.setupUi(self.Controller_UI)
        self.ui_app_library.setupUi(self.App_Library_UI)
        self.ui_state.setupUi(self.State_UI)
        self.ui_simluation.setupUi(self.Simulation_UI)
        self.ui_operator.setupUi(self.Operator_UI)
        self.ui_camera_view.setupUi(self.Camera_View_UI)
        self.ui_task_planner.setupUi(self.Task_Planner_UI)

        # defined DockWidget
        self.controller_dock = QDockWidget('Controller')
        self.app_library_dock = QDockWidget('Application Library')
        self.state_dock = QDockWidget('State')
        self.simulation_dock = QDockWidget('Simulation')
        self.operator_dock = QDockWidget('Operator')
        self.camera_view_dock = QDockWidget('Camera View')
        self.task_planner_dock = QDockWidget('Task Planner')

        # load Controller_UI as a dock in mainwindow
        self.controller_dock.setWidget(self.Controller_UI)
        self.app_library_dock.setWidget(self.App_Library_UI)
        self.state_dock.setWidget(self.State_UI)
        self.simulation_dock.setWidget(self.Simulation_UI)
        self.operator_dock.setWidget(self.Operator_UI)
        self.camera_view_dock.setWidget(self.Camera_View_UI)
        self.task_planner_dock.setWidget(self.Task_Planner_UI)

        # all area is allowed to dock
        self.controller_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.app_library_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.state_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.simulation_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.operator_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.camera_view_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.task_planner_dock.setAllowedAreas(Qt.AllDockWidgetAreas)

        # assigned the area to specific window
        self.splitDockWidget(self.controller_dock, self.simulation_dock, Qt.Horizontal)
        self.addDockWidget(Qt.RightDockWidgetArea, self.simulation_dock)
        self.addDockWidget(Qt.RightDockWidgetArea, self.camera_view_dock)
        self.addDockWidget(Qt.RightDockWidgetArea, self.task_planner_dock)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.controller_dock)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.app_library_dock)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.state_dock)

        self.camera_view_dock.hide()
        self.show()

        # self.splitDockWidget(self.controller_dock, self.simulation_dock, Qt.Horizontal)
        # self.addDockWidget(Qt.RightDockWidgetArea, self.simulation_dock)
        # self.addDockWidget(Qt.RightDockWidgetArea, self.camera_view_dock)
        # self.addDockWidget(Qt.RightDockWidgetArea, self.task_planner_dock)
        # self.addDockWidget(Qt.LeftDockWidgetArea, self.controller_dock)
        # self.addDockWidget(Qt.LeftDockWidgetArea, self.app_library_dock)
        # self.addDockWidget(Qt.LeftDockWidgetArea, self.state_dock)
        #
        # self.camera_view_dock.hide()

    def menu_bar_setting(self):
        # defined menubar
        self.bar = self.menuBar()

        self.Open_file = self.bar.addMenu('Open')

        self.Monitor = QMenu('Monitor', self)
        # self.Programmer_cfrp = QMenu('CFRP', self)

        self.Programmer_cfrp = QAction('CFRP', self)
        self.Open_file.addAction(self.Programmer_cfrp)
        self.Programmer_cfrp.triggered.connect(self.Threading)

        self.Open_file.addMenu(self.Monitor)
        # self.Open_file.addMenu(self.Programmer_cfrp)

        self.action_controller = QAction('Controller', self)
        self.Monitor.addAction(self.action_controller)
        self.action_controller.triggered.connect(self.controller_dock.show)

        self.action_app_library = QAction('App Library', self)
        self.Monitor.addAction(self.action_app_library)
        self.action_app_library.triggered.connect(self.app_library_dock.show)

        self.action_state = QAction('States', self)
        self.Monitor.addAction(self.action_state)
        self.action_state.triggered.connect(self.state_dock.show)

        self.action_simulation = QAction('Simulation', self)
        self.Monitor.addAction(self.action_simulation)
        self.action_simulation.triggered.connect(self.simulation_dock.show)

        self.action_operator = QAction('Operator', self)
        self.Monitor.addAction(self.action_operator)
        self.action_operator.triggered.connect(self.operator_dock.show)

        self.action_camera_view = QAction('Camera View', self)
        self.Monitor.addAction(self.action_camera_view)
        # self.action_camera_view.triggered.connect(self.camera_view_dock.show)
        self.action_camera_view.triggered.connect(self.Camera_Show)

        self.action_task_planner = QAction('Task Planner', self)
        self.Monitor.addAction(self.action_task_planner)
        self.action_task_planner.triggered.connect(self.task_planner_dock.show)

        self.setDockOptions(self.GroupedDragging | self.AllowTabbedDocks | self.AllowNestedDocks)
        self.setTabPosition(Qt.AllDockWidgetAreas, QTabWidget.North)
        # self.resize(1900, 1000)
        self.resize(1000, 600)

    def Threading(self):
        CFRP_thread = threading.Thread(target=self.Show_CFRP(), name='CFRP_thread')
        CFRP_thread.start()
        CFRP_thread.join()

    def Show_CFRP(self):
        time.sleep(1)

        if self.instance is not None:
            self.instance.show()

    # def Allclose(self):
    #     if self.close():
    #         self.instance.close()
    #     else:
    #         pass

    #     instance = PyFlow.instance(software="standalone")
    #     if instance is not None:
    #         app.setActiveWindow(instance)
    #         instance.show()
    #     else:
    #         print('error')

    def fCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def Camera_Show(self, state):
        # if state:
        self.camera_view_dock.show()

    def on_app_library_btn_clicked(self):
        self.ui_app_library.pushButton.pressed.connect(self.controller_dock.show)
        self.ui_app_library.pushButton_2.pressed.connect(self.state_dock.show)
        self.ui_app_library.pushButton_3.pressed.connect(self.simulation_dock.show)
        self.ui_app_library.pushButton_4.pressed.connect(self.camera_view_dock.show)
        self.ui_app_library.pushButton_5.pressed.connect(self.operator_dock.show)
        self.ui_app_library.pushButton_6.pressed.connect(self.task_planner_dock.show)
    # else:
    #     self.camera_view_dock.hide()
    # def toggleMenu(self, state):
    #
    #     if state:
    #         self.camera_view_dock.show()
    #     else:
    #         self.camera_view_dock.hide()


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # controller = QWidget()
    # MainWindow = main_window(controller)
    # controller.show()
    # # controller = QWidget()
    # # MainWindow = main_window(controller)
    # # controller.show()
    #
    # sys.exit(app.exec_())
    # def Show_CFRP(app):
    # rospy.init_node("test")
    app = QApplication([])
    main = main_window()

    # app1 = QApplication([])

    sys.exit(app.exec_())
    # main.show()
    # instance = PyFlow.instance(software="standalone")
    # if instance is not None:
    #     # app1.setActiveWindow(instance)
    #     instance.show()
    #     sys.exit(app1.exec_())
    # main.Programmer_cfrp.triggered.connect(main.Show_CFRP)

    # app.exec_()

# Cannot mix incompatible Qt library (5.15.0) with this library (5.15.2)

# PyQt5-Qt5                     5.15.2
