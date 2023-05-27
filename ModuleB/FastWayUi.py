import re

from PyQt5 import QtWidgets
import matplotlib.pyplot  as plt
from matplotlib.backends.backend_template import FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from ModuleB.CustomObject import CPU, Task, Theme
from ModuleB.WhoFaster import Ui_MainWindow
from ModuleBase.BaseObject import TimeTag

import sys


class Faster(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow=self)
        self.signalConnect()
        self.CpuMap = {}
        self.ThemeMap = {}
        self.initValue()

    def initValue(self):
        self.TaskItem = self.ui.Inventory.topLevelItem(0)
        self.ComputerItem = self.ui.Inventory.topLevelItem(1)
        self.timetag = TimeTag()
        self.ComputerItem.addChild(CPU("IPX-2000",400))
        self.ComputerItem.addChild(CPU("IPX-200",200))
        theme = Theme("字符串匹配","字符串匹配")
        self.ThemeMap["字符串匹配"] = theme
        self.TaskItem.addChild(theme)
        self.ui.TaskTheme.addItem("字符串匹配", theme)
        theme.addChild(Task("暴力破解",1000,"O(N^2)"))
        theme.addChild(Task("KMP算法",1000,self.timetag.BIGO_N))
        self.ui.TimeComplex_2.addItem(self.timetag.CONSTANT)
        self.ui.TimeComplex_2.addItem(self.timetag.LOGN)
        self.ui.TimeComplex_2.addItem(self.timetag.BIGO_N)
        self.ui.TimeComplex_2.addItem(self.timetag.NLOGN)
        self.ui.TimeComplex_2.addItem("O(N^2)")
        self.ui.TimeComplex_2.addItem("O(N^3)")
        self.ui.TimeComplex_2.addItem("O(2^N)")
        self.ui.TimeComplex_2.addItem("O(3^N)")
        self.AlgSampleNum = 100
        self.CpuSampleNUm = 100
        self.plot_()

    def signalConnect(self):
        self.ui.add_cpu.clicked.connect(self.AddComputerItem)
        self.ui.del_cpu.clicked.connect(self.DelComputerItem)
        self.ui.Inventory.signal.start_plot_sign.connect(self.startPlot)
        self.ui.AddTheme.clicked.connect(self.AddTheme)
        self.ui.DelTheme.clicked.connect(self.DelTheme)
        self.ui.add_task_btn.clicked.connect(self.AddTaskItem)
        self.ui.del_task_btn.clicked.connect(self.DelTaskItem)
        self.ui.Inventory.signal.algsign.connect(self.AlgDetail)
        self.ui.Inventory.signal.cpusign.connect(self.CpuDetail)
        self.ui.Inventory.signal.algdetailsign.connect(self.changeInfo)
        self.ui.Inventory.signal.algThemesign.connect(self.changeInfo)
        self.ui.Inventory.signal.cpudetailsign.connect(self.changeInfo)
    def changeInfo(self,item):
        if isinstance(item,Theme):
            self.ui.themeTitle.setText(item.title)
            self.ui.themeDesc.setText(item.desc)
        elif isinstance(item,Task):
            self.ui.AlgName.setText(item.title)
            self.ui.In_Size.setText(str(item.Input))
            self.ui.textEdit.setText(item.descri)
            for i in range(self.ui.TimeComplex_2.count()):
                if self.ui.TimeComplex_2.itemText(i) == item.timeComplex:
                    self.ui.TimeComplex_2.setCurrentIndex(i)
        elif isinstance(item,CPU):
            self.ui.name_edit.setText(item.name)
            self.ui.ipx_edit.setText(str(item.ipx))
    def AddComputerItem(self):
        if self.ui.name_edit.text() == "":
            return
        if not self.ui.ipx_edit.text().isdigit():
            return
        name = self.ui.name_edit.text()
        ipx = int(self.ui.ipx_edit.text())
        if ipx <= 0:
            return
        if self.CpuMap.get(name) != None:
            return
        cpu = CPU(name,ipx)
        self.CpuMap[name] = cpu
        self.ComputerItem.addChild(cpu)

    def DelComputerItem(self):
        if self.ui.name_edit.text() == "":
            return
        name = self.ui.name_edit.text()
        if self.CpuMap.get(name) == None:
            return
        self.ComputerItem.removeChild(self.CpuMap[name])
        del self.CpuMap[name]
    def AddTheme(self):
        title = self.ui.themeTitle.text()
        desc = self.ui.Desc.text()
        if title == "" or desc == "":
            return
        if self.ThemeMap.get(title) != None:
            return
        tempTheme = Theme(title,desc)
        self.ThemeMap[title] = tempTheme
        self.TaskItem.addChild(tempTheme)
        self.ui.TaskTheme.addItem(title,tempTheme)
    def DelTheme(self):
        title = self.ui.themeTitle.text()
        if title == "":
            return
        if self.ThemeMap.get(title) == None:
            return
        self.TaskItem.removeChild(self.ThemeMap[title])
        index = self.ui.TaskTheme.findText(title)
        self.ui.TaskTheme.removeItem(index)
        del self.ThemeMap[title]

    def AddTaskItem(self):
        if self.ui.TaskTheme.currentText() == "" or self.ui.TaskTheme.currentText() == None :
            return
        if self.ui.TimeComplex_2.currentText() == "" or self.ui.TimeComplex_2.currentText() == None:
            return
        if  self.ui.AlgName.text()=="" or self.ui.In_Size.text() == "" :
            return
        insize = int(self.ui.In_Size.text())
        if insize <= 100:
            insize=100
        algname = self.ui.AlgName.text()
        desc = self.ui.textEdit.toPlainText()
        tempTask = Task(algname,insize,self.ui.TimeComplex_2.currentText(),desc)
        theme :Theme= self.ui.TaskTheme.itemData(0)
        if theme.TaskMap.get(tempTask.KeyStr()) != None:
            return
        theme.addChild(tempTask)
        theme.TaskMap[tempTask.KeyStr()] = tempTask

    def DelTaskItem(self):
        if self.ui.TaskTheme.currentText() == "" or self.ui.TaskTheme.currentText() == None :
            return
        if self.ui.TimeComplex_2.currentText() == "" or self.ui.TimeComplex_2.currentText() == None:
            return
        if  self.ui.AlgName.text()=="" or self.ui.In_Size.text() == "" :
            return
        insize = int(self.ui.In_Size.text())
        if insize <= 100:
            return
        algname = self.ui.AlgName.text()
        desc = self.ui.textEdit.toPlainText()
        tempTask = Task(algname, insize, self.ui.TimeComplex_2.currentText(),desc)
        theme: Theme = self.ui.TaskTheme.itemData(0)
        if theme.TaskMap.get(tempTask.KeyStr()) == None:
            return
        theme.removeChild(theme.TaskMap[tempTask.KeyStr()])
        del theme.TaskMap[tempTask.KeyStr()]
    def AlgDetail(self):
        algtask: Task = self.ui.Inventory.AlgTask
        algcpu: CPU = self.ui.Inventory.AlgCPU
        algListX = []
        algListY = []
        for i in range(0,algtask.Input,int(algtask.Input/(algtask.Input/2))):
            algListX.append(i)
        for i in algListX:
            algListY.append(self.timetag.calculator(expr=algtask.timeComplex,N=i))
        str = "任务:\n任务简称：{}\n任务算法复杂度:{}\n任务输入规模{}\n任务问题规模:{}\n电脑:\n名称:{}\nIPX:{}" \
            .format(algtask.title,algtask.timeComplex,algtask.Input.__str__(),algListY[-1].__str__(),algcpu.name,algcpu.ipx.__str__())
        self.ui.atitle.setText("任务简称：{}".format(algtask.title))
        self.ui.aalg.setText("任务算法复杂度:{}".format(algtask.timeComplex))
        self.ui.algoutput.setText("任务问题规模:{}".format(algtask.Input.__str__()))
        self.ui.label_4.setText("任务问题输出规模:{}".format(algListY[-1].__str__()))
        self.ui.acpuname.setText("电脑名称：{}".format(algcpu.name))
        self.ui.aipx.setText("电脑IPX：{}".format(algcpu.ipx.__str__()))
        self.algfig.clf()
        self.ui.AlgLayout.removeWidget(self.algcavans)
        self.aax = self.algfig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.aax.set_xlim([0, algListX[-1]+10])
        self.aax.set_ylim([0, algListY[-1]+100])
        self.aax.set_xlabel("Input")
        self.aax.set_ylabel("Output")
        self.aax.set_title("Algorithm")
        self.aax.plot(algListX, algListY,label="Algorithm")
        self.algfig.legend()
        self.algcavans = FigureCanvas(self.algfig)
        self.ui.AlgLayout.addWidget(self.algcavans)

    def CpuDetail(self):
        comtask: Task = self.ui.Inventory.ComTask
        comcpu: CPU = self.ui.Inventory.ComCpu
        cpuListX = []
        cpuListY = []
        for i in range(0, comtask.Input, int(comtask.Input / (comtask.Input / 2))):
            cpuListX.append(i)
        for i in cpuListX:
            cpuListY.append(self.timetag.calculator(expr=comtask.timeComplex, N=i))
        str = "任务:\n任务简称:{}\n任务算法复杂度:{}\n任务输入规模:{}\n任务问题规模:{}\n电脑:\n名称:{}\nIPX:{}" \
            .format(comtask.title, comtask.timeComplex, comtask.Input.__str__(), cpuListY[-1].__str__(), comcpu.name,
                    comcpu.ipx.__str__())
        self.ui.label_11.setText("任务简称：{}".format(comtask.title))
        self.ui.label_12.setText("任务算法复杂度:{}".format(comtask.timeComplex))
        self.ui.label_13.setText("任务问题规模:{}".format(comtask.Input.__str__()))
        self.ui.label_5.setText("任务问题输出规模:{}".format(cpuListY[-1].__str__()))
        self.ui.label_14.setText("电脑名称：{}".format(comcpu.name))
        self.ui.label_15.setText("电脑IPX：{}".format(comcpu.ipx.__str__()))
        self.cpufig.clf()
        self.ui.CpuLayout.removeWidget(self.cpucavans)
        self.cax = self.cpufig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.cax.set_xlim([0, cpuListX[-1]+10])
        self.cax.set_ylim([0, cpuListY[-1]+100])
        self.cax.set_xlabel("Input")
        self.cax.set_ylabel("Output")
        self.cax.set_title("CPU")
        self.cax.plot(cpuListX, cpuListY,label="Algorithm")
        self.cpufig.legend()
        self.cpucavans = FigureCanvas(self.cpufig)
        self.ui.CpuLayout.addWidget(self.cpucavans)
    def startPlot(self):
        algtask:Task = self.ui.Inventory.AlgTask
        algcpu:CPU = self.ui.Inventory.AlgCPU
        comtask:Task = self.ui.Inventory.ComTask
        comcpu:CPU= self.ui.Inventory.ComCpu

        algListX = []
        cpuListX = []
        algListY = []
        cpuListY = []
        for i in range(0,algtask.Input,int(algtask.Input/(algtask.Input/2))):
            algListX.append(i)
        for i in range(0,comtask.Input,int(comtask.Input/(comtask.Input/2))):
            cpuListX.append(i)
        for i in algListX:
            algListY.append(self.timetag.calculator(expr=algtask.timeComplex,N=i))
        for i in cpuListX:
            cpuListY.append(self.timetag.calculator(expr=comtask.timeComplex,N=i))

        finalalgYListY = []
        finalcouListY = []
        for i in algListY:
            finalalgYListY.append(i/algcpu.ipx)
        for i in cpuListY:
            finalcouListY.append(i/comcpu.ipx)
        self.fig.clf()
        self.ui.VisualLayout.removeWidget(self.cavans)
        plt.ion()
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.ax.set_xlim([0, max(algtask.Input,comtask.Input)])
        self.ax.set_ylim([0, max(finalalgYListY[-1],finalcouListY[-1])])
        self.ax.set_xlabel("Input")
        self.ax.set_ylabel("Time")
        self.ax.set_title("Who is Faster?")
        self.ax.plot(algListX,finalalgYListY,label="Faster Algorithm")
        self.ax.plot(cpuListX,finalcouListY,label="Faster Computer")
        self.fig.legend()
        self.cavans = FigureCanvas(self.fig)
        self.ui.VisualLayout.addWidget(self.cavans)

    def plot_(self):
        self.fig = plt.Figure()
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.ax.set_xlim([1, 1000])
        self.ax.set_ylim([1, 1000])
        self.ax.set_xlabel("Input")
        self.ax.set_ylabel("Time")
        self.ax.set_title("Who is Faster?")
        self.cavans = FigureCanvas(self.fig)
        # 将绘制好的图像设置为中心 Widget
        self.ui.VisualLayout.addWidget(self.cavans)

        self.cpufig = plt.Figure()
        self.cax = self.cpufig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.cax.set_xlim([1, 1000])
        self.cax.set_ylim([1, 1000])
        self.cax.set_title("Algorithm")
        self.cpucavans = FigureCanvas(self.cpufig)
        # 将绘制好的图像设置为中心 Widget
        self.ui.CpuLayout.addWidget(self.cpucavans)

        self.algfig = plt.Figure()
        self.aax = self.algfig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.aax.set_xlim([1, 1000])
        self.aax.set_ylim([1, 1000])
        self.aax.set_title("Computer")
        self.algcavans = FigureCanvas(self.algfig)
        # 将绘制好的图像设置为中心 Widget
        self.ui.AlgLayout.addWidget(self.algcavans)

def FastWayStart():
    # app = QtWidgets.QApplication(sys.argv)
    win = Faster()
    win.show()
    # sys.exit(app.exec_())




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Faster()
    win.show()
    sys.exit(app.exec_())

