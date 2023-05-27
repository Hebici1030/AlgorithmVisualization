import sys
from decimal import Decimal
from functools import partial
from typing import List

import matplotlib
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QListWidgetItem
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
# from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D

from ModuleBase.BaseObject import Meta, TimeTag
from ModuleC import FunctionUI
from ModuleC.Base import Work


class Function(QMainWindow):
    def __init__(self):
        super(Function, self).__init__()
        self.ui = FunctionUI.Ui_MainWindow()
        self.ui.setupUi(MainWindow=self)
        self.initValue()
        self.connectBtn()
        self.InitalDraw()

    def initValue(self):
        self.meatMap = {}
        self.prvLine :Line2D = None
        self.prvStr = None
        self.mapLines = {}
        self.currentFunctionStr :List[str] = []
        self.X=1000
        self.Y=10000

    def connectBtn(self):
        self.ui.O1.clicked.connect(partial(self.InputFouctionStr,self.ui.O1.text()))
        self.ui.ON.clicked.connect(partial(self.InputFouctionStr, self.ui.ON.text()))
        self.ui.OLOGN.clicked.connect(partial(self.InputFouctionStr, self.ui.OLOGN.text()))
        self.ui.NLOGN.clicked.connect(partial(self.InputFouctionStr, self.ui.NLOGN.text()))
        self.ui.N2.clicked.connect(partial(self.InputFouctionStr, self.ui.N2.text()))
        self.ui.fractrialN.clicked.connect(partial(self.InputFouctionStr, self.ui.fractrialN.text()))
        self.ui.PLUSBTN.clicked.connect(partial(self.pulsTest,self.ui.PLUSBTN.text()))
        self.ui.twoN.clicked.connect(partial(self.InputFouctionStr,self.ui.twoN.text()))
        self.ui.KN.clicked.connect(partial(self.InputExpNotation,self.ui.KN.text()))
        self.ui.NK.clicked.connect(partial(self.InputExpNotation, self.ui.NK.text()))
        self.ui.AddBTN.clicked.connect(self.AddFucntion)
        self.ui.DelBtn.clicked.connect(self.DelNotation)
        self.ui.XEdit.editingFinished.connect(self.cheakXNum)
        self.ui.YEdit.editingFinished.connect(self.cheakYNum)
        self.ui.functionWidget.itemDoubleClicked.connect(self.doubleClickItem)

    def InitalDraw(self):
        # plt.ion()
        # # plt.rcParams['agg.path.chunksize'] = 10000
        # self.fig = plt.Figure()
        # self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        # self.ax.set_xlim([1, self.X])
        # self.ax.set_ylim([1, self.Y])
        # # 使用FigureCanvasQTAgg替代FigureCanvas
        # self.canvas = FigureCanvas(self.fig)
        # # 将canvas的父类设置为QWidget并添加到布局管理器中
        # self.ui.showLayout.addWidget(self.canvas)
        plt.ion()
        matplotlib.rc("font", family='YouYuan')
        self.fig, self.ax = plt.subplots()
        self.ax.plot([0.1,0.1,0.8,0.8])
        self.ax.set_xlabel("SortWay")
        self.ax.set_ylabel("Time")
        self.ax.set_title("Sort")
        self.ax.set_xlim([1, self.X])
        self.ax.set_ylim([1, self.Y])
        self.canvas = FigureCanvas(self.fig)
        self.ui.showLayout.addWidget(self.canvas)

    def drawOneLine(self,m :Meta):
        line = self.ax.plot(m.listx,m.listy,label=m.functionStr)
        self.mapLines[m.functionStr] = line
        self.ax.legend()
        self.canvas.draw()


    def doubleClickItem(self,item :QListWidgetItem):
        if (self.prvStr != None):
            prvline :Line2D = self.mapLines[self.prvStr[2:-1]][0]
            prvline.set_color(self.prvLine.get_color())
            prvline.set_linestyle(self.prvLine.get_linestyle())
            prvline.set_marker(self.prvLine.get_marker())
            prvline.set_markersize(self.prvLine.get_markersize())
        str = item.text()
        self.prvStr = str
        lines = self.mapLines[str[2:-1]]
        line :Line2D = lines[0]
        self.prvLine :Line2D= Line2D(line.get_xdata(),line.get_ydata(),color=line.get_color(),linestyle=line.get_linestyle(),marker=line.get_marker(),markersize=line.get_markersize())
        line.set_color('black')
        line.set_linestyle('--')
        # line.set_marker('*')
        line.set_markersize(5)
        existing_legend = self.ax.get_legend()
        if existing_legend:
            existing_legend.remove()
        self.fig.legend()
        self.canvas.draw()
    def InputExpNotation(self,notation :str):
        if self.pulsTest(notation) != 1:
            return
        if(self.ui.KEdit.text()==""):
            print(self.ui.KEdit.text())
            self.showMessage("请在第三个LineEdit输入k的取值")
            return
        notation = notation.replace("k",self.ui.KEdit.text())
        tag = notation[2:-1]
        self.currentFunctionStr.append(tag)
        self.ui.founctionBrower.setText("O(" + self.tranList2Str() + ")")

    def InputFouctionStr(self,notaion :str):
        if self.pulsTest(notaion) != 1:
            return
        tag = notaion[2:-1]
        self.currentFunctionStr.append(tag)
        self.ui.founctionBrower.setText("O("+self.tranList2Str()+")")

    def pulsTest(self,notaion):
        if (notaion == "+"):
            if (len(self.currentFunctionStr) == 0):
                self.showMessage("请至少输入一个算法复杂度符号")
                return
            elif self.currentFunctionStr[-1] == "+":
                self.showMessage("请输入正确的式子")
                return
            else:
                self.currentFunctionStr.append(notaion)
                self.ui.founctionBrower.setText("O(" + self.tranList2Str() + ")")
                return
        if (notaion != "+" and len(self.currentFunctionStr) > 0):
            if (self.currentFunctionStr[-1] != "+"):
                self.showMessage("请不要连续输入算法符号")
                return
        return 1

    def AddFucntion(self):
        meta = Meta()
        meta.functionStr = self.tranList2Str()
        if(len(meta.functionStr)==0):
            self.showMessage("添加符号为空请输入至少一个时间复杂度符号")
            return
        if self.meatMap.get(meta.functionStr)!=None :
            self.showMessage("请勿重复添加相同的算式")
            return
        self.meatMap[meta.functionStr] = meta
        self.finishMeta(meta)
        self.drawOneLine(meta)

        self.ui.functionWidget.addItem("O("+meta.functionStr+")")
        self.ui.founctionBrower.clear()
        self.currentFunctionStr.clear()

    def DelNotation(self):
        if (len(self.currentFunctionStr) == 0):
            self.showMessage("删除无效")
            return
        self.currentFunctionStr.__delitem__(-1)
        self.ui.founctionBrower.setText("O(" + self.tranList2Str() + ")")

    def finishMeta(self,meta:Meta):
        if(meta.functionStr.startswith("N!") or meta.functionStr.startswith("^N")):
            meta.type=1
        else :
            meta.type=0

        for i in range(0,self.X,int(self.X/int(self.X/2))):
            meta.listx.append(i)

        for i in meta.listx:
            tempNum = Decimal()
            for j in meta.functionStr.split("+"):
                if(j.startswith("N^")):
                    j+=(",k="+str(j[2:]))
                if(j.endswith("^N")):
                    j+=(",k="+str(j[0:-2]))
                tempNum+=Decimal(str(TimeTag.calculator(TimeTag(),j,i)))
            meta.listy.append(tempNum)
    def ReCaculate(self):
        print("recacluete")
        self.work = Work(self.meatMap.values(),self.X)
        self.work.sign.progress.connect(self.progress)
        self.work.sign.finish.connect(self.finish)
        self.work.start()
    def progress(self,index):
        print("progress")
        self.showMessage("正在重新计算取值采样{}".format((index / len(self.meatMap.values())).__str__()))
    def finish(self):
        print("finish")
        self.showMessage("完成取值采样")
        self.ui.showLayout.removeWidget(self.canvas)
        plt.clf()
        self.fig, self.ax = plt.subplots()
        self.ax.plot([0.1, 0.1, 0.8, 0.8])
        self.ax.set_xlabel("SortWay")
        self.ax.set_ylabel("Time")
        self.ax.set_title("Sort")
        self.ax.set_xlim([1, self.X])
        self.ax.set_ylim([1, self.Y])
        self.canvas = FigureCanvas(self.fig)
        self.ui.showLayout.addWidget(self.canvas)
        for i in self.meatMap.values():
            self.drawOneLine(i)
    def tranList2Str(self):
        tempStr = ""
        for i in self.currentFunctionStr:
            tempStr+=i
        return tempStr

    def showMessage(self,message:str):
        self.statusBar().showMessage(message,5000)

    def RepaintLine(self):
        self.ui.showLayout.removeWidget(self.canvas)
        self.startPlot();
        for i in self.meatMap.values():
            self.drawOneLine(i)

    def cheakXNum(self):
        if not self.ui.XEdit.text().isdigit():
            return
        if (self.ui.XEdit.text() == ""):
            self.showMessage("本次输入无内容，不改变X的取值")
            return
        if (int(self.ui.XEdit.text()) < 100):
            self.showMessage("取值范围≥100")
            return
        if (int(self.ui.XEdit.text()) == self.X):
            self.showMessage("横坐标取值未变，不重新绘图")
            return
        self.X = int(self.ui.XEdit.text())
        self.ax.set_xlim([0,self.X])
        self.ReCaculate()

    def cheakYNum(self):
        if(self.ui.YEdit.text() == ""):
            self.showMessage("本次输入无内容，不改变Y的取值")
            return
        if(int(self.ui.YEdit.text()) <100):
            self.showMessage("取值范围≥100")
            return
        if(int(self.ui.YEdit.text())==self.Y):
            self.showMessage("纵坐标取值未变，不重新绘图")
            return
        self.Y= int(self.ui.YEdit.text())
        self.ax.set_ylim([0, self.Y])
    def startPlot(self):
        plt.ion()
        self.fig,self.ax = plt.subplot()
        self.ax:Axes = self.ax
        self.ax.set_xlim(0,float(self.X))
        self.ax.set_ylim(0,float(self.Y))
        self.ax.set_xlabel("输入任务数")
        self.ax.set_ylabel("输出任务总数")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Function()
    win.show()
    sys.exit(app.exec_())