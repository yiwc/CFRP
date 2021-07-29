# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Camera_View.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Camera_View(object):
    def setupUi(self, Camera_View):
        Camera_View.setObjectName("Camera_View")
        Camera_View.resize(772, 492)
        self.label = QtWidgets.QLabel(Camera_View)
        self.label.setGeometry(QtCore.QRect(40, 20, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Camera_View)
        self.label_2.setGeometry(QtCore.QRect(40, 220, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Camera_View)
        QtCore.QMetaObject.connectSlotsByName(Camera_View)

    def retranslateUi(self, Camera_View):
        _translate = QtCore.QCoreApplication.translate
        Camera_View.setWindowTitle(_translate("Camera_View", "Camera_View"))
        self.label.setText(_translate("Camera_View", "Left Camera"))
        self.label_2.setText(_translate("Camera_View", "Right Camera"))

