# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Simulation.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Simulation(object):
    def setupUi(self, Simulation):
        Simulation.setObjectName("Simulation")
        Simulation.resize(538, 336)
        self.label = QtWidgets.QLabel(Simulation)
        self.label.setGeometry(QtCore.QRect(30, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Simulation)
        QtCore.QMetaObject.connectSlotsByName(Simulation)

    def retranslateUi(self, Simulation):
        _translate = QtCore.QCoreApplication.translate
        Simulation.setWindowTitle(_translate("Simulation", "Simulation"))
        self.label.setText(_translate("Simulation", "Simulation"))

