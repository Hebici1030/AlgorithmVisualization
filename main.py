import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from ModuleA.Invariant import start
from ModuleB.FastWayUi import  Faster
from inter import Ui_MainWindow


class Input(QMainWindow):
    def __init__(self):
        super(Input, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow=self)
        self.ui.pushButton.clicked.connect(self.FastWayStart)
    def FastWayStart(self):
        self.win = Faster()
        self.win.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Input()
    main.show()
    sys.exit(app.exec_())

