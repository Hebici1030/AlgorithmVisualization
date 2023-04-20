from functools import partial

from PyQt5 import QtGui
from PyQt5.QtCore import  Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QTreeWidget, QMenu, QAction



class CustomTreeItem(QTreeWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)#打开右键策略
        self.customContextMenuRequested.connect(self.RightPressMenu)
        self.AlgCPU = None
        self.ComCpu = None
        self.AlgTask = None
        self.ComTask = None
        self.ui = None

    def RightPressMenu(self,pos):
        item = self.currentItem()
        item1 = self.itemAt(pos)
        print(type(item1),type(item))
        # if item1 != None and item != None:
        #     popMenu = QMenu()
        #     popMenu.addAction(QAction(u'添加为', self))
        #     popMenu.addAction(QAction(u'bbb', self))
        #     popMenu.triggered[QAction].connect(self.processtrigger)
        #     popMenu.exec_(QCursor.pos())
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

    def processtrigger(self,item1:QTreeWidget,parent,q:QAction):

        print(type(item1))
        print(type(parent))
        target = q.text()
        if target == '更快的算法CPU':
            self.AlgCPU = item1
        elif target == '更快的电脑CPU':
            self.ComCpu = item1
        elif target == '更快的算法Task' :
            self.AlgTask = item1
        elif target == '更快的电脑Task':
            self.ComTask = item1
        if(bool(self.ComTask and self.AlgTask and self.ComCpu and self.AlgCPU)):
            print("设置完成，开始绘图")
            self.signal.start_plot_sign.emit()

    def setSignal(self,sign):
        self.signal = sign
    def setUi(self,Ui):
        self.ui = Ui

    def mouseDoubleClickEvent(self, e: QtGui.QMouseEvent):
        super().mouseDoubleClickEvent(e)
        pass
    def mousePressEvent(self, e: QtGui.QMouseEvent):
        super().mousePressEvent(e)
        pass 
