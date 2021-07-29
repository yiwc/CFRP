# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Operator.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Operator(object):
    def setupUi(self, Operator):
        Operator.setObjectName("Operator")
        Operator.resize(688, 305)
        self.label = QtWidgets.QLabel(Operator)
        self.label.setGeometry(QtCore.QRect(260, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Operator)
        self.label_2.setGeometry(QtCore.QRect(290, 200, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Operator)
        self.pushButton.setGeometry(QtCore.QRect(250, 250, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Operator)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 250, 161, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Operator)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 250, 161, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Operator)
        QtCore.QMetaObject.connectSlotsByName(Operator)

    def retranslateUi(self, Operator):
        _translate = QtCore.QCoreApplication.translate
        Operator.setWindowTitle(_translate("Operator", "Operator"))
        self.label.setText(_translate("Operator", "Camera View"))
        self.label_2.setText(_translate("Operator", "Action"))
        self.pushButton.setText(_translate("Operator", "Insert Bolt"))
        self.pushButton_2.setText(_translate("Operator", "Tighten Bolt"))
        self.pushButton_3.setText(_translate("Operator", "Pick Bolt"))

