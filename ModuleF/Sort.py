import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ModuleF.Base import SrotedWay
from ModuleF.SortUI import Ui_MainWindow


class Sort(QMainWindow):
    def __init__(self):
        super(Sort, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow=self)
        self.initalUi()
        self.connectSlot()
    def initalUi(self):
        self.timer = QTimer()
        self.timer.setSingleShot(1000)
        self.timer.timeout.connect(self.initWork)
        self.timer.start()
    def initWork(self):
        self.sw = SrotedWay(parent=self.ui.WorkArea)
        self.sw.show()
    def connectSlot(self):
        self.ui.InitalSize.editingFinished.connect(self.QuickGenerate)
    def QuickGenerate(self):
        if not self.ui.InitalSize.text().isdigit():
            return
        self.sw.ReStatus()
        self.sw.InitalList(int(self.ui.InitalSize.text()))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Sort()
    win.show()
    sys.exit(app.exec_())