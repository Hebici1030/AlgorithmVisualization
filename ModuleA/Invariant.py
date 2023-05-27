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
        self.ui.SpeedSlider.setRange(0,10)
        self.ui.SpeedSlider.setValue(5)
    def InitalUI(self):
        self.AnWidget = AnimationWidget(self.ui.WorkArea)
        self.ui.WorkLayout.addWidget(self.AnWidget)
        self.AnWidget.show()
        self.AnWidget.signalObject.enableBtn.connect(self.EnableBTN)
        self.AnWidget.signalObject.refreshInfo.connect(self.RefreshINFO)
        self.ui.CBrower.insertPlainText("无待排序数组")
        self.ui.CBrower.setAlignment(Qt.AlignCenter)
    def ConnectSlot(self):
        self.ui.IntialSize.editingFinished.connect(self.InitalWorkArea)
        self.ui.StartBTN.clicked.connect(self.StartSort)
        self.ui.PauseBTN.clicked.connect(self.PauseSort)
        self.ui.NextBTN.clicked.connect(self.NextBtn)
        self.ui.SpeedSlider.valueChanged.connect(self.ChangeSpeed)
        self.ui.InsertBTN.clicked.connect(self.AddNum)
        self.ui.PrvBTN.clicked.connect(self.Recover)
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
        self.ui.SpeedSlider.setValue(5)
        self.ui.NextBTN.setEnabled(False)
        self.ui.PrvBTN.setEnabled(False)
    def PauseSort(self):
        self.AnWidget.PauseBubble()
        self.ui.NextBTN.setEnabled(True)
        self.ui.PrvBTN.setEnabled(True)
    def EnableBTN(self):
        self.ui.NextBTN.setEnabled(True)
        self.ui.PrvBTN.setEnabled(True)
    def NextBtn(self):
        if(len(self.AnWidget.tempList)<=0):
            return
        self.AnWidget.OneStep()
    def Recover(self):
        self.AnWidget.Recover()
    def RefreshINFO(self):
        self.ui.CBrower.setAlignment(Qt.AlignLeft)
        str = "{}\n第{}次迭代,\n数组大小:{}\n外层循环下标:{}\n内层循环下标:{}\n数组:{}".format(
            self.StatusInfo(),
            self.AnWidget.indexI+1,
            len(self.AnWidget.rectList),
            self.AnWidget.indexI,
            self.AnWidget.indexJ,
            self.AnWidget.tempList.__str__()
        )
        self.ui.CBrower.setText(str)
    def StatusInfo(self):
        if self.AnWidget.indexI == 0 and self.AnWidget.indexJ==0:
            self.ui.BBubble.setChecked(True)
            self.ui.CBubble.setChecked(False)
            self.ui.EBubble.setChecked(False)
            return "初始化:\n在第一次遍历之前，整个数组是未排序的。"
        elif self.AnWidget.indexI == len(self.AnWidget.rectList):
            self.ui.BBubble.setChecked(False)
            self.ui.CBubble.setChecked(False)
            self.ui.EBubble.setChecked(True)
            return "终止：\n当遍历完成时，整个数组都已经按照升序排列"
        else:
            self.ui.BBubble.setChecked(False)
            self.ui.CBubble.setChecked(True)
            self.ui.EBubble.setChecked(False)
            return "迭代：\n第 i({})次遍历时， i-1({})个元素已经按从小到大的顺序排好了，而剩下的 n-i+1({})元素仍未排序完成。".format(
                self.AnWidget.indexI + 1, self.AnWidget.indexI, len(self.AnWidget.rectList) - self.AnWidget.indexI + 1
            )
    def ChangeSpeed(self,num):
        self.AnWidget.ChangeBaseTime(num)
    def AddNum(self):
        if not self.ui.lineEdit.text().isdigit():
            return
        num = int(self.ui.lineEdit.text())
        self.AnWidget.AddValue(num)
def start():
        app = QtWidgets.QApplication(sys.argv)
        win = Invariant()
        win.show()
        sys.exit(app.exec_())
if __name__ == "__main__":
    start()