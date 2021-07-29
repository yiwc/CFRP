# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Controller.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_COntroller(object):
    def setupUi(self, COntroller):
        COntroller.setObjectName("COntroller")
        COntroller.resize(831, 467)
        font = QtGui.QFont()
        font.setPointSize(20)
        COntroller.setFont(font)
        COntroller.setAutoFillBackground(False)
        self.label_2 = QtWidgets.QLabel(COntroller)
        self.label_2.setGeometry(QtCore.QRect(419, 9, 153, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_1 = QtWidgets.QLabel(COntroller)
        self.label_1.setGeometry(QtCore.QRect(9, 9, 107, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.But_Pos_1 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_1.setGeometry(QtCore.QRect(20, 100, 71, 71))
        self.But_Pos_1.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_1.setMaximumSize(QtCore.QSize(100, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.But_Pos_1.setPalette(palette)
        self.But_Pos_1.setAutoFillBackground(False)
        self.But_Pos_1.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"")
        self.But_Pos_1.setObjectName("But_Pos_1")
        self.But_Pos_2 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_2.setGeometry(QtCore.QRect(140, 100, 71, 71))
        self.But_Pos_2.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_2.setMaximumSize(QtCore.QSize(100, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.But_Pos_2.setPalette(palette)
        self.But_Pos_2.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"")
        self.But_Pos_2.setObjectName("But_Pos_2")
        self.But_Pos_3 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_3.setGeometry(QtCore.QRect(260, 100, 71, 71))
        self.But_Pos_3.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_3.setMaximumSize(QtCore.QSize(100, 100))
        self.But_Pos_3.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"\n"
"")
        self.But_Pos_3.setObjectName("But_Pos_3")
        self.But_Pos_4 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_4.setGeometry(QtCore.QRect(20, 210, 71, 71))
        self.But_Pos_4.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_4.setMaximumSize(QtCore.QSize(100, 100))
        self.But_Pos_4.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"")
        self.But_Pos_4.setObjectName("But_Pos_4")
        self.But_Pos_5 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_5.setGeometry(QtCore.QRect(380, 330, 91, 91))
        self.But_Pos_5.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_5.setMaximumSize(QtCore.QSize(100, 100))
        self.But_Pos_5.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"")
        self.But_Pos_5.setObjectName("But_Pos_5")
        self.But_Pos_6 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_6.setGeometry(QtCore.QRect(260, 210, 71, 71))
        self.But_Pos_6.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_6.setMaximumSize(QtCore.QSize(100, 100))
        self.But_Pos_6.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"")
        self.But_Pos_6.setObjectName("But_Pos_6")
        self.But_Pos_8 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_8.setGeometry(QtCore.QRect(140, 210, 71, 71))
        self.But_Pos_8.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_8.setMaximumSize(QtCore.QSize(100, 100))
        self.But_Pos_8.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"\n"
"")
        self.But_Pos_8.setObjectName("But_Pos_8")
        self.But_Pos_7 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_7.setGeometry(QtCore.QRect(730, 210, 71, 71))
        self.But_Pos_7.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_7.setMaximumSize(QtCore.QSize(100, 100))
        self.But_Pos_7.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"")
        self.But_Pos_7.setObjectName("But_Pos_7")
        self.But_Pos_9 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_9.setGeometry(QtCore.QRect(230, 330, 91, 91))
        self.But_Pos_9.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_9.setMaximumSize(QtCore.QSize(100, 100))
        self.But_Pos_9.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"")
        self.But_Pos_9.setObjectName("But_Pos_9")
        self.But_Pos_10 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_10.setGeometry(QtCore.QRect(490, 210, 71, 71))
        self.But_Pos_10.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_10.setMaximumSize(QtCore.QSize(100, 100))
        self.But_Pos_10.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"")
        self.But_Pos_10.setObjectName("But_Pos_10")
        self.But_Pos_11 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_11.setGeometry(QtCore.QRect(610, 100, 71, 71))
        self.But_Pos_11.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_11.setMaximumSize(QtCore.QSize(100, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.But_Pos_11.setPalette(palette)
        self.But_Pos_11.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"")
        self.But_Pos_11.setObjectName("But_Pos_11")
        self.But_Pos_12 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_12.setGeometry(QtCore.QRect(610, 210, 71, 71))
        self.But_Pos_12.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_12.setMaximumSize(QtCore.QSize(100, 100))
        self.But_Pos_12.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"\n"
"")
        self.But_Pos_12.setObjectName("But_Pos_12")
        self.But_Pos_13 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_13.setGeometry(QtCore.QRect(490, 100, 71, 71))
        self.But_Pos_13.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_13.setMaximumSize(QtCore.QSize(100, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.But_Pos_13.setPalette(palette)
        self.But_Pos_13.setAutoFillBackground(False)
        self.But_Pos_13.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"")
        self.But_Pos_13.setObjectName("But_Pos_13")
        self.But_Pos_14 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_14.setGeometry(QtCore.QRect(730, 100, 71, 71))
        self.But_Pos_14.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_14.setMaximumSize(QtCore.QSize(100, 100))
        self.But_Pos_14.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"\n"
"")
        self.But_Pos_14.setObjectName("But_Pos_14")
        self.But_Pos_15 = QtWidgets.QPushButton(COntroller)
        self.But_Pos_15.setGeometry(QtCore.QRect(530, 330, 91, 91))
        self.But_Pos_15.setMinimumSize(QtCore.QSize(60, 60))
        self.But_Pos_15.setMaximumSize(QtCore.QSize(100, 100))
        self.But_Pos_15.setStyleSheet("background-color: rgb(255,255, 255);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 9pt \"AcadEref\";\n"
"border-style: outset;\n"
"")
        self.But_Pos_15.setObjectName("But_Pos_15")

        self.retranslateUi(COntroller)
        QtCore.QMetaObject.connectSlotsByName(COntroller)

    def retranslateUi(self, COntroller):
        _translate = QtCore.QCoreApplication.translate
        COntroller.setWindowTitle(_translate("COntroller", "Controller"))
        self.label_2.setText(_translate("COntroller", "Orientation"))
        self.label_1.setText(_translate("COntroller", "Position"))
        self.But_Pos_1.setText(_translate("COntroller", "Upward"))
        self.But_Pos_2.setText(_translate("COntroller", "Foward"))
        self.But_Pos_3.setText(_translate("COntroller", "Downward"))
        self.But_Pos_4.setText(_translate("COntroller", "Left"))
        self.But_Pos_5.setText(_translate("COntroller", "Arm Change"))
        self.But_Pos_6.setText(_translate("COntroller", "Right"))
        self.But_Pos_8.setText(_translate("COntroller", "Backward"))
        self.But_Pos_7.setText(_translate("COntroller", "Right"))
        self.But_Pos_9.setText(_translate("COntroller", "Gripper Close"))
        self.But_Pos_10.setText(_translate("COntroller", "Left"))
        self.But_Pos_11.setText(_translate("COntroller", "Foward"))
        self.But_Pos_12.setText(_translate("COntroller", "Backward"))
        self.But_Pos_13.setText(_translate("COntroller", "Upward"))
        self.But_Pos_14.setText(_translate("COntroller", "Downward"))
        self.But_Pos_15.setText(_translate("COntroller", "Gripper Close"))

