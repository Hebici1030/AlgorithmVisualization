import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from ModuleA.Invariant import start, Invariant
from ModuleB.FastWayUi import  Faster
from ModuleC.Function import Function
from ModuleD.TreeNo import ThreeNotation
from ModuleE.Finder import Finder
from ModuleF.Sort import Sort
from inter import Ui_MainWindow


class Input(QMainWindow):
    def __init__(self):
        super(Input, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow=self)
        self.ui.pushButton.clicked.connect(self.Notation)
    def FastWayStart(self):
        self.win = Faster()
        self.win.show()
    def Bubble(self):
        self.bubble = Invariant()
        self.bubble.show()
    def Function(self):
        self.fun = Function()
        self.fun.show()
    def Notation(self):
        self.notation = ThreeNotation()
        self.notation.show()
    def Finder(self):
        self.finder = Finder()
        self.finder.show()
    def Sort(self):
        self.sort = Sort()
        self.sort.show()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Input()
    main.show()
    sys.exit(app.exec_())

