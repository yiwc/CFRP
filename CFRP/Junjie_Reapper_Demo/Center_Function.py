import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QDesktopWidget, QWidget

class Center(QWidget):



    def fCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
