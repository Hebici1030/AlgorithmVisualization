import sys
import time

import matplotlib
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib import  *
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pylab import *

from ModuleF.Base import SrotedWay, Method
from ModuleF.SortUI import Ui_MainWindow

class Sort(QMainWindow):
    def __init__(self):
        super(Sort, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow=self)
        self.initalUi()
    def initalUi(self):
        self.methodName = Method()
        for i in range(1,10):
            self.ui.SortMethod.addItem(self.methodName.__getattribute__(self.methodName.__dir__()[i]))
        self.timer = QTimer()
        self.timer.setSingleShot(100)
        self.timer.timeout.connect(self.initWork)
        self.timer.start()
        self.plotTimer = QTimer()
        self.plotTimer.setInterval(10)
        self.plotTimer.timeout.connect(self.PaintPlot)
    def initWork(self):
        self.ax = []
        self.ay = {}
        self.sw = SrotedWay(parent=self.ui.WorkArea)
        self.ui.WorkLayout.addWidget(self.sw)
        self.sw.show()
        self.sw.changeinfo.changeinfo.connect(self.changeinfo)
        self.switcher = {
            self.methodName.BUBBLESORT : self.sw.BubbleSort,
            self.methodName.QUICKSORT : self.sw.QuickSort,
            self.methodName.SHELLSORT : self.sw.ShellSort,
            self.methodName.BUCKETSORT :self.sw.BucketSort,
            self.methodName.INSERTSORT : self.sw.InsertSort,
            self.methodName.SELECTSORT : self.sw.SelectSort,
            self.methodName.MERGERSORT : self.sw.MergeSort,
            self.methodName.DUMPSORT : self.sw.HeapSort,
            self.methodName.COUNTINGSORT:self.sw.radix_sort
        }
        self.connectSlot()
        self.InitiPlot()
    def connectSlot(self):
        self.ui.InitalSize.editingFinished.connect(self.QuickGenerate)
        self.ui.StartBtn.clicked.connect(self.startBtn)
        self.ui.RecoverBTN.clicked.connect(self.recoverBtn)
        self.ui.PauseBtn.clicked.connect(self.Pause)
        self.pauseflag = 1
    def QuickGenerate(self):
        if not self.ui.InitalSize.text().isdigit():
            return
        self.sw.ReStatus()
        self.sw.InitalList(int(self.ui.InitalSize.text()))
    def startBtn(self):
        if not self.ui.InitalSize.text().isdigit():
            return
        sortway = self.switcher.get(self.ui.SortMethod.currentText())
        if not self.ax.__contains__(self.ui.SortMethod.currentText()):
            self.ax.append(self.ui.SortMethod.currentText())
        self.ay[self.ui.SortMethod.currentText()] = 0
        self.sw.move = 0
        self.sw.compare = 0
        self.startTime = time.time()
        sortway()
    def Pause(self):
        if self.pauseflag >0:
            self.sw.IsContinue = False
            self.pauseflag = 0
        else:
            self.sw.IsContinue = True
            self.pauseflag = 1
    def changeinfo(self):
        self.ui.lineEdit.setText(self.sw.compare.__str__())
        self.ui.lineEdit_2.setText(self.sw.move.__str__())
        self.ay[self.ui.SortMethod.currentText()] = time.time() - self.startTime
        self.PaintPlot()
    def recoverBtn(self):
        self.sw.BackStatus()
    def PaintPlot(self):
        plt.cla()
        # self.ui.PlotLayout.removeWidget(self.canvas)
        # matplotlib.rc("font", family='YouYuan')
        # self.fig, self.pax = plt.subplots()
        # self.pax.bar([], [])
        # self.pax.set_xlabel("SortWay")
        # self.pax.set_ylabel("Time")
        # self.pax.set_title("Sort")
        # self.canvas = FigureCanvas(self.fig)
        # self.ui.PlotLayout.addWidget(self.canvas)
        tempay = []
        self.pax.set_xlabel("SortWay")
        self.pax.set_ylabel("Time(/s)")
        self.pax.set_title("Sort")
        for i in self.ax:
            tempay.append(self.ay.get(i))
        self.pax.bar(self.ax,tempay)
        self.canvas.draw()
    def InitiPlot(self):
        plt.ion()
        matplotlib.rc("font",family='YouYuan')
        self.fig,self.pax = plt.subplots()
        self.pax.bar([],[])
        self.pax.set_xlabel("SortWay")
        self.pax.set_ylabel("Time(/s)")
        self.pax.set_title("Sort")
        self.canvas = FigureCanvas(self.fig)
        self.ui.PlotLayout.addWidget(self.canvas)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Sort()
    win.show()
    sys.exit(app.exec_())