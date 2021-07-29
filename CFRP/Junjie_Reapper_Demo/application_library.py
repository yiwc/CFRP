# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application_library.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_application_library(object):
    def setupUi(self, application_library):
        application_library.setObjectName("application_library")
        application_library.resize(534, 409)
        self.label = QtWidgets.QLabel(application_library)
        self.label.setGeometry(QtCore.QRect(0, 10, 111, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(application_library)
        self.pushButton.setGeometry(QtCore.QRect(40, 90, 91, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(application_library)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 90, 91, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(application_library)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 90, 91, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(application_library)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 250, 91, 81))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(application_library)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 250, 91, 81))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(application_library)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 250, 91, 81))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(application_library)
        QtCore.QMetaObject.connectSlotsByName(application_library)

    def retranslateUi(self, application_library):
        _translate = QtCore.QCoreApplication.translate
        application_library.setWindowTitle(_translate("application_library", "Form"))
        self.label.setText(_translate("application_library", "application library"))
        self.pushButton.setText(_translate("application_library", "Controller"))
        self.pushButton_2.setText(_translate("application_library", "States"))
        self.pushButton_3.setText(_translate("application_library", "Simulation"))
        self.pushButton_4.setText(_translate("application_library", "Camera"))
        self.pushButton_5.setText(_translate("application_library", "Operator"))
        self.pushButton_6.setText(_translate("application_library", "Task Planner"))

