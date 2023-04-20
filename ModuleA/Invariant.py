import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ModuleA.Base import AnimationWidget
from ModuleA.bbUI import Ui_MainWindow


class Invariant(QMainWindow):
    def __init__(self):
        super(Invariant, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow=self)
        self.InitalValue()
        self.ConnectSlot()
    def InitalValue(self):
        self.intimer=QTimer()
        self.intimer.setSingleShot(100)
        self.intimer.timeout.connect(self.InitalUI)
        self.intimer.start()
    def InitalUI(self):
        self.AnWidget = AnimationWidget(self.ui.WorkArea)
        self.ui.WorkLayout.addWidget(self.AnWidget)
        self.AnWidget.show()
        self.AnWidget.signalObject.enableBtn.connect(self.EnableBTN)
        self.BaseInfo()
    def ConnectSlot(self):
        self.ui.IntialSize.editingFinished.connect(self.InitalWorkArea)
        self.ui.StartBTN.clicked.connect(self.StartSort)
        self.ui.PauseBTN.clicked.connect(self.PauseSort)
        self.ui.NextBTN.clicked.connect(self.NextBtn)
    def InitalWorkArea(self):
        if not self.ui.IntialSize.text().isdigit():
            return
        size = int(self.ui.IntialSize.text())
        if(size<=0):
            return
        print("signal")
        self.AnWidget.ReInital()
        self.AnWidget.RandomInitalRectList(size)
        self.AnWidget.update()
    def StartSort(self):
        self.AnWidget.StartBubble()
        self.ui.NextBTN.setEnabled(False)
        self.ui.PrvBTN.setEnabled(False)
    def PauseSort(self):
        self.AnWidget.PauseBubble()
        self.ui.NextBTN.setEnabled(True)
        self.ui.PrvBTN.setEnabled(True)
    def EnableBTN(self):
        self.ui.NextBTN.setEnabled(True)
        self.ui.PrvBTN.setEnabled(True)
    def BaseInfo(self):
        self.ui.textBrowser_3.setText("冒泡排序是一种基本的排序算法，其基本思想是通过相邻元素之间的比较和交换来将一个序列按照升序或者降序排列。//\
        而循环不变量则是在程序设计中常用的一种技术，用于证明程序的正确性。在冒泡排序中，我们使用两重循环来实现排序。外层循环控制轮数，内层循环则进行相邻元素之间的比较和交换操作。循环不变量指的是在每次外层循环结束后，内层循环能够保证当前序列的前i个元素已经被排好序了，其中i表示当前轮数。")
    def NextBtn(self):
        self.AnWidget.OneStep()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Invariant()
    win.show()
    sys.exit(app.exec_())