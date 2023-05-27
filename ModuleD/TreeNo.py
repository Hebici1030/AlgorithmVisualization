import re
import sys
from typing import List

import matplotlib
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ModuleD.Base import Notation, NotationFactory, ArrayMonitorArray, CaculatorMonitor, Data, Sign, LineCaculator
from ModuleD.Notation import Ui_TreeNotaion
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class ThreeNotation(QMainWindow):
    def __init__(self):
        super(ThreeNotation, self).__init__()
        self.ui = Ui_TreeNotaion()
        self.ui.setupUi(TreeNotaion=self)
        self.connectSlot()
        self.intPlot()
        self.iniValue()
        self.intUI()
    def intUI(self):
        self.ui.XSlider.setMinimum(100)
        self.ui.XSlider.setMaximum(1000)
        self.ui.XSlider.setSingleStep(200)
        self.ui.XSlider.setTickPosition(QSlider.TicksBothSides)
        self.ui.XSlider.setTickInterval(200)
        self.ui.YSlider.setMinimum(100)
        self.ui.YSlider.setMaximum(5000)
        self.ui.YSlider.setSingleStep(200)
        self.ui.YSlider.setTickPosition(QSlider.TicksBothSides)
        self.ui.YSlider.setTickInterval(1000)
    def iniValue(self):
        self.factory = NotationFactory()
        self.function:List[str] = []
        self.prvlen = 0
        self.funQtimer = QTimer()
        self.funQtimer.setInterval(500)
        self.funQtimer.timeout.connect(self.DisPlayNotation)
        self.funQtimer.start()
        self.data = Data()
        self.XLimit = 100
        self.XSampling = int(self.XLimit/2)
        self.YLimit = 100
        self.sign = Sign()
        self.sign.plotSign.connect(self.DrawLine)
        # self.PlotMonitor = CaculatorMonitor()
        self.PlotMonitor = LineCaculator(self.factory, len(self.factory.notations.notations),self.data,self.XLimit,self.sign)

    def handleXValueChanged(self, value):
        step = self.ui.XSlider.singleStep()
        remainder = value % 100
        if remainder != 0:
            new_value = value - remainder
            self.ui.XSlider.setValue(new_value)
    def handleYValueChanged(self, value):
        step = self.ui.YSlider.singleStep()
        remainder = value % 100
        if remainder != 0:
            new_value = value - remainder
            self.ui.YSlider.setValue(new_value)

    def intPlot(self):
        plt.ion()
        self.fig = plt.Figure()
        self.pax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.pax.set_xlim([1, 1000])
        self.pax.set_ylim([1, 10000])
        self.pax.set_xlabel("Input")
        self.pax.set_ylabel("Output")
        self.pax.set_title("Three Notation")
        self.fig.legend()
        self.cavans = FigureCanvas(self.fig)
        # 将绘制好的图像设置为中心 Widget
        self.ui.PlotLayout.addWidget(self.cavans)
    def DrawLine(self):
        for i in self.pax.lines:
            i.remove()
        self.pax.set_xlim([1, self.XLimit])
        self.pax.set_ylim([1, self.YLimit])
        self.pax.plot(self.data.ax,self.data.ay,color="black",label="Function")
        self.pax.plot(self.data.Oax, self.data.Oay,color="yellow",label="BigO")
        self.pax.plot(self.data.OmAx, self.data.OmAy,color="red",label = "Omega")
        self.pax.plot(self.data.OmUpAx, self.data.OmUpAy,color="green",label = "ThetaTop")
        self.pax.plot(self.data.OmDownAx, self.data.OmDownAy,color="green",label = "ThetaBottom")
        self.fig.legend()
        self.cavans.draw()
    def connectSlot(self):
        self.ui.N.clicked.connect(self.NBtn)
        self.ui.Nlogn.clicked.connect(self.NlogN)
        self.ui.LogN.clicked.connect(self.LogNBtn)
        self.ui.N2.clicked.connect(self.N2)
        self.ui.N3.clicked.connect(self.N3)
        self.ui.NK.clicked.connect(self.NK)
        self.ui.KN.clicked.connect(self.KN)
        self.ui.FN.clicked.connect(self.FN)
        self.ui.TwoN.clicked.connect(self.TwoN)
        self.ui.Plus.clicked.connect(self.Plus)
        self.ui.remove.clicked.connect(self.ReDuce)
        self.ui.ConstantEditor.editingFinished.connect(self.Constant)
        self.ui.XSlider.valueChanged.connect(self.changeInfo)
        self.ui.YSlider.valueChanged.connect(self.changeInfo)
        self.ui.XSlider.valueChanged.connect(self.handleXValueChanged)
        self.ui.YSlider.valueChanged.connect(self.handleYValueChanged)
        self.ui.XSlider.sliderReleased.connect(self.changePlotRange)
    def BtnOne(self):
        pass
    def changeInfo(self):
        self.ui.label_9.setText(self.ui.XSlider.value().__str__())
        self.ui.label_10.setText(self.ui.YSlider.value().__str__())
        self.XLimit = self.ui.XSlider.value()
        self.YLimit = self.ui.YSlider.value()
        self.PlotMonitor.Xlim = self.XLimit
        self.pax.set_xlim([1, self.XLimit])
        self.pax.set_ylim([1, self.YLimit])
        self.cavans.draw()
    def changePlotRange(self):
        self.PlotMonitor.asign.sign.emit()

    def DisPlayNotation(self):
        if self.prvlen != len(self.function):
            self.prvlen = len(self.function)
            Omiga = ""
            for i in self.function:
                Omiga+=i
            self.factory.notations.getBigO()
            self.factory.notations.getTheta()
            self.factory.notations.getAcurateTheta()
            BigO = ""
            if re.search(",",self.factory.notations.biggest.notation):
                BigO = self.factory.notations.biggest.notation.split(",")[0]
            else:
                BigO = self.factory.notations.biggest.notation
            Theta = ""
            if re.search(",",self.factory.notations.biggest.notation):
                Theta = self.factory.notations.biggest.notation.split(",")[0]
            else:
                Theta = self.factory.notations.biggest.notation
            self.ui.BigDispalyer.setText("O({}),Co={},No={}".format(BigO,self.factory.notations.BigOC0.__str__()\
                                                                    ,self.factory.notations.BigON0.__str__()))

            self.ui.OmigaDispalyer.setText("Θ({})".format(Omiga))

            self.ui.ThetaDispalyer.setText("Ω({}),Co={},No={}".format(Theta,self.factory.notations.ThetaCo\
                                                                      ,self.factory.notations.ThetaNo))

            self.PlotMonitor.asign.sign.emit()
    def NBtn(self):
        if self.ui.MultEditor.text() == "":
            mult = 1
        else:
            if self.ui.MultEditor.text().isdigit():
                mult = int(self.ui.MultEditor.text())
            else:
                return
        self.function.append("N")
        self.factory.addSingleNotation("N^1,m={}".format(mult))
    def LogNBtn(self):
        if self.ui.MultEditor.text() == "":
            mult = 1
            self.function.append("LogN".format(mult))
        else:
            if self.ui.MultEditor.text().isdigit():
                mult = int(self.ui.MultEditor.text())
                self.function.append("{}LogN".format(mult))
            else:
                return
        self.factory.addSingleNotation("LogN,m={}".format(mult))
    def Constant(self):
        str = self.ui.ConstantEditor.text()
        print(str)
        if str.isdigit():
            self.function.append(str.__str__())
            self.factory.addSingleNotation(str.__str__())
    def NlogN(self):
        self.factory.addSingleNotation("NLogN")
        self.function.append("NLogN")
    def N2(self):
        if self.ui.MultEditor.text() == "":
            mult = 1
            self.function.append("N^2")
        else:
            if self.ui.MultEditor.text().isdigit():
                mult = int(self.ui.MultEditor.text())
                self.function.append("{}N^2".format(mult))
            else:
                return
        self.factory.addSingleNotation("N^2,m={}".format(mult))
    def N3(self):
        if self.ui.MultEditor.text() == "":
            mult = 1
            self.function.append("N^3")
        else:
            if self.ui.MultEditor.text().isdigit():
                mult = int(self.ui.MultEditor.text())
                self.function.append("{}N^3".format(mult))
            else:
                return
        self.factory.addSingleNotation("N^3,m={}".format(mult))
    def NK(self):
        exp = self.ui.ExpEditor.text()
        mult = self.ui.MultEditor.text()
        if exp == "" or exp=="1":
            exp = "1"
        if mult == "" or mult=="1":
            mult = "1"
            self.function.append("N^{}".format(exp))
        else:
            self.function.append("{}N^{}".format(mult,exp))
        self.factory.addSingleNotation("N^{},m={}".format(exp,mult))
    def KN(self):
        dom = self.ui.ExpEditor.text()
        if dom =="":
            dom = "2"
        elif dom=="1":
            return
        self.function.append("{}^N".format(dom))
        self.factory.addSingleNotation("{}^N".format(dom))
    def FN(self):
        self.function.append("N!")
        self.factory.addSingleNotation("N!")
    def TwoN(self):
        self.factory.addSingleNotation("2^N")
        self.function.append("2^N")
    def Plus(self):
        self.function.append("+")
    def ReDuce(self):
        if len(self.function)>0:
            if self.function[-1]!="+":
                self.factory.notations.deltail()
            self.function.remove(self.function[-1])
    def ReInitial(self):
        self.factory = NotationFactory()
    def closeEvent(self, a0: QtGui.QCloseEvent):
        super(ThreeNotation, self).closeEvent(a0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = ThreeNotation()
    win.show()
    sys.exit(app.exec_())