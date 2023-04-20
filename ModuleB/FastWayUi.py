from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
import matplotlib.pyplot  as plt
from  matplotlib import *
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from matplotlib.pyplot import figure
from PyQt5.QtCore import *
from numpy import linspace, pi
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ModuleB.WhoFaster import Ui_MainWindow
from ModuleBase.BaseObject import CPU, Task, PlotSignal, TimeTag
from CustomObject import CustomTreeItem
import sys


class Faster(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow=self)
        self.initValue()
        self.signalConnect()

    def initValue(self):
        self.TaskItem = self.ui.Inventory.topLevelItem(0)
        self.ComputerItem = self.ui.Inventory.topLevelItem(1)
        self.ui.Inventory.setUi(self.ui)
        cpu = CPU()
        cpu.initialValue(200,"PX-A")
        cpu2 = CPU()
        cpu2.initialValue(100, "PX-B")
        task = Task()
        task.initalTitle("字符串匹配","测试")
        task1 =  Task()
        task1.initialValue("字符串匹配",800,"测试","O(N^K),K=2")
        task2 = Task()
        task2.initialValue("字符串匹配", 800, "测试", "O(NLOGN)")
        self.TaskItem.addChild(task)
        task.addChild(task1)
        task.addChild(task2)
        self.ComputerItem.addChild(cpu)
        self.ComputerItem.addChild(cpu2)
        self.plot_()

    def signalConnect(self):
        self.ui.add_cpu.clicked.connect(self.AddComputerItem)
        self.ui.del_cpu.clicked.connect(self.DelComputerItem)
        self.ui.add_task_btn.clicked.connect(self.AddTaskItem)
        self.signal = PlotSignal()
        self.signal.start_plot_sign.connect(self.startPlot)
        self.ui.Inventory.setSignal(self.signal)


    def AddComputerItem(self):
        cpu = CPU()
        str_name = self.ui.name_edit.text()
        str_ipx = self.ui.ipx_edit.text()
        if(str_name == '' and str_ipx == ''):
            print("禁止为空")
            return
        cpu.initialValue(int(str_ipx),str_name)
        self.ComputerItem.addChild(cpu)

    def DelComputerItem(self):
        strname = self.ui.name_edit.text()
        if(strname==''):
             print("禁止为空ID")
        for i in range(self.ComputerItem.childCount()) :
            child = self.ComputerItem.child(i)
            print(child.text(0))
            print(strname)
            if child.text(0).__eq__(strname):
                self.ComputerItem.removeChild(child)

    def AddTaskItem(self):

        title = self.ui.In_title.text()
        size = self.ui.In_Size.text()
        comp = self.ui.In_Complex.text()
        desc = self.ui.textEdit.toPlainText()
        if(bool(title) and (not bool(size and comp and desc))):
            task = Task()
            task.initalTitle(title,desc)
            self.TaskItem.addChild(task)
            return
        if not bool(title and size and comp and desc) :
            print("输入完整")
            return
        task = Task()
        task.initialValue(title, int(size), desc, comp)
        for i in range(self.TaskItem.childCount()):
            if title == self.TaskItem.child(i).text(0):
                self.TaskItem.child(i).addChild(task)
                return
        print("没有找到父类，请检查输入")

        # if (str_name == '' and str_ipx == ''):
        #     print("禁止为空")
        #     return
        # cpu.initialValue(int(str_ipx), str_name)
        # self.ComputerItem.addChild(cpu)

    def startPlot(self):
        algtask:Task = self.ui.Inventory.AlgTask
        algcpu:CPU = self.ui.Inventory.AlgCPU
        comtask:Task = self.ui.Inventory.ComTask
        comcpu:CPU= self.ui.Inventory.ComCpu

        algtotal = int(TimeTag().calculator(algtask.timeComplex,algtask.Input))
        comtotal = int(TimeTag().calculator(comtask.timeComplex,comtask.Input))

        algx = range(0,algtotal,int(algtotal/40))
        comx = range(0,comtotal,int(comtotal/40))
        algy = []
        comy = []

        for i in algx:
            algy.append(i/algcpu.ipx)
        for i in comx:
            comy.append(i/comcpu.ipx)
        self.fig.clf()
        self.ui.VisualLayout.removeWidget(self.cavans)
        # self.fig.plot(list(algx),algy)
        # self.fig.plot(list(comx),comy)

        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.ax.set_xlim([0, min(algtotal,comtotal)])
        self.ax.set_ylim([0, min(algy[-1],comy[-1])])
        # plt.xlabel("任务量")
        # plt.ylabel("任务量/秒")
        self.ax.plot(list(algx),algy,"r*-",label="更快的算法")
        self.ax.plot(list(comx),comy,"g+--",label="更快的电脑")
        self.cavans = FigureCanvas(self.fig)
        # 将绘制好的图像设置为中心 Widget
        self.ui.VisualLayout.addWidget(self.cavans)

    def plot_(self):
        self.fig = plt.Figure()
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.ax.set_xlim([1, 10000])
        self.ax.set_ylim([1, 10000])
        self.cavans = FigureCanvas(self.fig)
        # 将绘制好的图像设置为中心 Widget
        self.ui.VisualLayout.addWidget(self.cavans)






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Faster()
    win.show()
    sys.exit(app.exec_())

