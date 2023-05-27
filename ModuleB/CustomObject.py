from functools import partial

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QMetaType
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QTreeWidget, QMenu, QAction, QTreeWidgetItem


class PlotSignal(QObject):
    start_plot_sign = pyqtSignal()
    algsign = pyqtSignal()
    cpusign = pyqtSignal()
    cpudetailsign = pyqtSignal(object)
    algdetailsign = pyqtSignal(object)
    algThemesign = pyqtSignal(object)


class CPU(QTreeWidgetItem):
    def __init__(self,name:str,ipx:int):
        super().__init__()
        self.ipx = ipx
        self.name = name
        self.setText(0, name)
        self.setText(1, str(ipx) + "ipx")
    def initialValue(self,ipx,name):
        self.ipx = ipx
        self.name = name
        self.setText(0,name)
        self.setText(1,str(ipx)+"ipx")

class Theme(QTreeWidgetItem):

    def __init__(self,title :str = None,desc :str=None):
        super(Theme, self).__init__()
        self.title = title
        self.desc = desc
        self.setText(0,title)
        self.TaskMap  = {}

class Task(QTreeWidgetItem):
    def __init__(self,title,input,timeComplex,descri=None):
        super().__init__();
        self.title:str = title
        self.Input:int = input
        self.descri:str = descri
        self.timeComplex:str = timeComplex
        self.setText(0,timeComplex)
        self.setText(1,title)
        self.setText(2,str(input))
    def KeyStr(self):
        return self.title+str(self.Input)+self.timeComplex
class CustomTreeItem(QTreeWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)#打开右键策略
        self.customContextMenuRequested.connect(self.RightPressMenu)
        self.AlgCPU :CPU=None
        self.ComCpu :CPU=None
        self.AlgTask :Task = None
        self.ComTask :Task = None
        self.ui = None
        self.signal = PlotSignal()
        self.itemDoubleClicked.connect(self.handleItemDoubleCliked)

    def handleItemDoubleCliked(self,item,column):
        print(type(item))
        if isinstance(item,Theme):
            self.signal.algdetailsign.emit(item)
        elif isinstance(item,Task):
            self.signal.algdetailsign.emit(item)
        elif isinstance(item,CPU):
            self.signal.cpudetailsign.emit(item)

    def RightPressMenu(self,pos):
        item = self.currentItem()
        item1 = self.itemAt(pos)
        if isinstance(item,Theme):
            return
        if  item != None and item1 != None and item1.parent() != None :

            if(   item1.parent().text(0).__eq__("电脑")):
                popMenu = QMenu()
                popMenu.addAction(QAction(u'更快的算法CPU', self))
                popMenu.addAction(QAction(u'更快的电脑CPU', self))
                popMenu.triggered[QAction].connect(partial(self.processtrigger,item1,item))
                popMenu.exec_(QCursor.pos())
            else:
                popMenu = QMenu()
                popMenu.addAction(QAction(u'更快的算法Task', self))
                popMenu.addAction(QAction(u'更快的电脑Task', self))
                popMenu.triggered[QAction].connect(partial(self.processtrigger,item1,item))
                popMenu.exec_(QCursor.pos())

    def processtrigger(self,item1,parent,q:QAction):
        target = q.text()
        if target == '更快的算法CPU':
            self.AlgCPU = item1
            print(self.AlgCPU.ipx)
        elif target == '更快的电脑CPU':
            self.ComCpu = item1
            print(self.ComCpu.ipx)
        elif target == '更快的算法Task' :
            self.AlgTask = item1
        elif target == '更快的电脑Task':
            self.ComTask = item1
        if (bool(self.ComTask and self.ComCpu)):
            self.signal.cpusign.emit()
        if (bool(self.AlgCPU and self.AlgTask)):
            self.signal.algsign.emit()
        if(bool(self.ComTask and self.AlgTask and self.ComCpu and self.AlgCPU)):
            self.signal.start_plot_sign.emit()

    def mouseDoubleClickEvent(self, e: QtGui.QMouseEvent):
        super().mouseDoubleClickEvent(e)
        pass
    def mousePressEvent(self, e: QtGui.QMouseEvent):
        super().mousePressEvent(e)
        pass 
