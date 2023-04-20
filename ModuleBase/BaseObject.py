import math
import random
import re
import sys
from decimal import Decimal
from turtle import Shape
from typing import List

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QPoint, QSize, QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QIcon, QRgba64, QPolygon, QPolygonF
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QTreeWidgetItem, QWidget, QPushButton
from PyQt5.QtCore import *


class PlotSignal(QObject):
    start_plot_sign = pyqtSignal()
class Bubble_Rect(QObject):
    def __init__(self,x,y,w,h,num: int):
        super().__init__()
        self.rect = QRect(x,y,w,h)
        self.num = num
        self.statu = -1
    def __lt__(self, other):
        return self.num<other.num

    def __repr__(self):
        return f"{self.num}"
class CPU(QTreeWidgetItem):
    def __init__(self):
        super().__init__()
        self.ipx = 0
        self.name = None
        self.pic:QIcon = None
    def initialValue(self,ipx,name,pic: QIcon = None):
        self.ipx = ipx
        self.name = name
        self.pic  = pic
        self.setText(0,name)
        self.setText(1,str(ipx)+"ipx")

class Task(QTreeWidgetItem):
    def __init__(self):
        super().__init__();
        self.title:str = None
        self.Input:int = None
        self.descri:str = None
        self.timeComplex:str = None
    def initialValue(self,title,inpue,desc,time):
        self.title: str = title
        self.Input: int = inpue
        self.descri: str = desc
        self.timeComplex: str = time
        self.setText(0,self.timeComplex)
        self.setText(1,str(self.Input))
    def initalTitle(self,title,desc):
        self.title = title
        self.setText(0,title)
        self.descri = desc

class TimeTag:
    CONSTANT = "O(1)"
    BIGO_N = "O(N)"
    LOGN = "O(LOGN)"
    NLOGN = "O(NLOGN)"
    SQUAREN = "O(N^K)"
    INDEXN = "O(K^N)"
    FACTORIALN = "O(N!)"

    def calculator(self,expr:str,N:int):
        if("," in expr):
            [exp,kstr] = expr.upper().split(",")
            k = int(re.findall(r'\d+', kstr)[0])
        else:
            exp = expr.upper()
            k = None
        if exp == self.CONSTANT or exp==self.CONSTANT[2:-1]:
            return 1
        elif exp == self.BIGO_N or exp==self.BIGO_N[2:-1]:
            return N
        elif exp == self.LOGN or exp==self.LOGN[2:-1]:
            return 0 if N==0 else  math.log2(N)
        elif exp == self.NLOGN or exp==self.NLOGN[2:-1]:
            return 0 if N==0 else N*math.log2(N);
        elif k != None and  (exp == self.SQUAREN or exp[0:2]==self.SQUAREN[2:4]):
            return N**k
        elif k!=None and (exp == self.INDEXN or exp[-2:]==self.INDEXN[3:5]) :
            return k**N
        elif exp == self.FACTORIALN or exp == self.FACTORIALN[2:-1]:
            return math.factorial(N)
        else:
            return -1

class ArrowLabel(QWidget):

    def __init__(self,parent):
        super(ArrowLabel, self).__init__(parent)
        self.setGeometry(0,0,60,100)

    def paintEvent(self,a0: QtGui.QPaintEvent):
        super().paintEvent(a0)
        painter = QPainter()
        painter.begin(self)
        # painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter.drawRect(self.rect().adjusted(0, 0, -1, -1))
        painter.setBrush(QBrush(QColor("#ff9641")))
        painter.setPen(Qt.NoPen)
        rect = QRect(QPoint(10,0),QSize(40,60))
        painter.drawRect(rect)
        ploy = QPolygon([QPoint(0,60),QPoint(60,60),QPoint(30,90)])
        painter.drawPolygon(ploy)
        painter.end()

class DataGenerator:
    def GenerateList(self,size:int):
        res:List[int] = []
        for i in range(1,size+1):
            res.append(i)
        random.shuffle(res)
        return res

class SearchWay:
    LINERSEARCH = "线性查找"
    BINARYSEARCH= "二分查找"
    MODSEARCH ="取余法"
    LINEARPROBING = "线性勘测"
    QUADRATICPROBING = "二次勘测"
    SEPARATECHAING = "拉链冲突法"

class QCustomizeList(QWidget):
    def __init__(self,cell :QSize = QSize(100,100),parent :QWidget = None):
        super(QCustomizeList, self).__init__(parent)
        self.RectList :List[QRect] = []
        self.NumList = []
        self.currentRectIndex = 0
        self.currentIndex = 0
        self.cellSize :QSize = cell
        self.totalCellNum = int( parent.rect().width()*0.95 / cell.width())
        self.WindowSize = self.totalCellNum - 4
        self.widget = parent
        print(self.widget.geometry().__str__())
        print(self.widget.objectName())
        self.setGeometry(0,int(parent.height()/2+self.cellSize.height()/2),self.widget.width(),self.cellSize.height())
        self.resize(self.widget.width(),self.cellSize.height())

    def paintEvent(self, a0: QtGui.QPaintEvent):
        super(QCustomizeList, self).paintEvent(a0)
        painter =QPainter()
        painter.setPen(Qt.black)
        painter.begin(self)
        painter.drawRect(self.rect().adjusted(0, 0, -1, -1))
        if(len(self.NumList)<=self.totalCellNum):
            print("NumList:{},totalCellNum:{}".format(len(self.NumList),self.totalCellNum))
            self.paintAll(painter)
        painter.end()

    def paintAll(self,p :QPainter):
        if(len(self.NumList)==0):
            return
        startPoint = self.getCenterPoint()
        if len(self.NumList)%2==0 :
            startx = int(startPoint.x() - len(self.NumList)*self.cellSize.width()/2)
            starty = int(startPoint.y() - self.cellSize.height()/2)
            index = 0
            for i in self.NumList:
                print("NUmList-IndexNum:{}".format(i))
                rect = QRect(QPoint(startx+index*self.cellSize.width(),starty),self.cellSize)
                self.RectList.append(rect)
                p.drawRect(rect)
                p.drawText(rect,Qt.AlignCenter,str(i))
                index+=1
        else:
            startx = int(startPoint.x() - (len(self.NumList)) * self.cellSize.width() / 2)
            starty = int(startPoint.y() - self.cellSize.height() / 2)
            index = 0
            for i in self.NumList:
                print("NUmList-IndexNum:{}".format(i))
                rect = QRect(QPoint(startx + index * self.cellSize.width(), starty), self.cellSize)
                self.RectList.append(rect)
                p.drawRect(rect)
                p.drawText(rect, Qt.AlignCenter, str(i))
                index += 1
    # 根据下标和数组大小进行绘图。Finder通过增长CurrentIndex快速改变当前窗口值
    def paintByIndex(self):
        pass
    def paintLeft(self):
        pass
    def paintRight(self):
        pass
    def paintCenter(self):
        pass
    def getStartXY(self):
        startPoint = self.getCenterPoint()
        if len(self.RectList) % 2 == 0:
            startx = int(startPoint.x() - len(self.RectList) * self.cellSize.width() / 2)
            starty = int(startPoint.y() - self.cellSize.height() / 2)
            return QPoint(startx, starty)
        else:
            startx = int(startPoint.x() - len(self.RectList + 1) * self.cellSize.width() / 2)
            starty = int(startPoint.y() - self.cellSize.height() / 2)
            return QPoint(startx,starty)
    def getCenterPoint(self):
        geometry = self.geometry()
        w = geometry.width()
        h = geometry.height()
        baseCol = int(h/2)
        baseRow = int(w/2)
        return QPoint(baseRow,baseCol)
    # def resizeEvent(self, a0: QtGui.QResizeEvent):
    #     self.paintEvent(a0)

class QCustomizeHash(QWidget):
    def __init__(self,parent :QWidget,RecSize :QSize = QSize(100,50),SlotSize:QSize = None):
        super(QCustomizeHash, self).__init__(parent)
        self.NumList :List[int] =[]
        self.RectList :List[QRect]= []
        self.SlotNumList :List[List[int]] = []
        self.currentIndex = -1
        self.currentRectIndex = 0
        self.dense = 0.2
        self.size = 0
        self.Initalcapacity = 0
        self.capacity = 0
        self.mode = -1
        self.RectSize = RecSize
        self.SlotSize = SlotSize
        self.widget = parent
        self.windowSize = int(parent.height()*0.9/self.RectSize.height())
        self.starty = 0
        self.startx = int(parent.geometry().center().x() - self.RectSize.width() / 2)
        self.setGeometry(self.startx,self.starty,self.RectSize.width(),self.widget.height())
        self.AnimationTime = 1000
        self.LineCollideTimer = QTimer()
        self.LineCollideTimer.setInterval(self.AnimationTime)
        self.LineCollideTimer.timeout.connect(self.LineCollide)
        self.Target = 0
        self.collpseTime = 0

    def setSize(self,size :int):
        self.size = size
        self.NumList = []
        self.RectList = []
        self.Target = 0
        self.Initalcapacity = int(self.size*self.dense)
        self.setGeometry(self.startx,self.starty,self.RectSize.width(),size*self.RectSize.height())
        print(self.geometry())
        self.currentIndex = -1
        self.currentRectIndex = 0
        self.capacity = self.Initalcapacity
        self.collpseTime = 0
    def MoveCenter(self):
        if(self.currentIndex == -1):
            return
        # self.move(self.x(),self.starty)
        centerY = int(self.parent().height()/2)
        rect :QRect = self.RectList[self.currentIndex]
        print("current:{},rect:{}".format(self.currentIndex,rect.__str__()))
        gap = int(centerY - rect.y())
        self.__MoveAnimation(gap)
    def __MoveAnimation(self,gap):
        animation = QPropertyAnimation(self,b"geometry",self.widget)
        animation.setDuration(self.AnimationTime)
        animation.setStartValue(self.geometry())
        animation.setEndValue(QRect(self.geometry().x(),self.starty+gap,self.width(),self.height()))
        animation.start()
    #策略模式？？？
    def ModHash(self,num :int):
        return num % len(self.NumList)

    def LineCollide(self):
        # if(self.NumList[self.currentIndex] == "None"):
        #     self.MoveCenter()
        #     self.LineCollideTimer.stop()
        #     return
        if self.NumList[self.currentIndex] != "None" :
            if(self.NumList[self.currentIndex]==self.Target):
                self.LineCollideTimer.stop()
                return
            if(self.currentIndex== len(self.NumList)):
                self.currentIndex = 0
            self.currentIndex +=1
            self.collpseTime+=1
            self.MoveCenter()
            return
        self.NumList[self.currentIndex] = self.Target
        self.repaint()
        self.MoveCenter()
        self.capacity+=1
        self.LineCollideTimer.stop()

    def paintEvent(self, a0: QtGui.QPaintEvent):
        super(QCustomizeHash, self).paintEvent(a0)
        qp = QPainter(self)
        qp.begin(self)
        qp.drawRect(self.rect().adjusted(0,0,-1,-1))
        if(len(self.NumList)!=0):
            for i in range(len(self.NumList)):
                if (i == self.currentIndex):
                    qp.setBrush(QBrush(QColor("#00ff7f")))
                    qp.drawRect(self.RectList[i])
                    qp.drawText(self.RectList[i], Qt.AlignCenter, self.NumList[i].__str__())
                    qp.setBrush(Qt.NoBrush)
                    continue
                qp.drawRect(self.RectList[i])
                qp.drawText(self.RectList[i], Qt.AlignCenter, self.NumList[i].__str__())
        # if(len(self.NumList)!=0):
        #     if (self.currentIndex < self.windowSize):
        #         for i in range(len(self.NumList)):
        #             if (i == self.currentIndex):
        #                 qp.drawRect(self.RectList[i])
        #                 qp.drawText(self.RectList[i], Qt.AlignCenter, self.NumList[i]+i.__str__())
        #                 continue
        #             qp.drawRect(self.RectList[i])
        #             qp.drawText(self.RectList[i], Qt.AlignCenter, self.NumList[i]+i.__str__())
        #     elif self.currentIndex >= len(self.NumList) - self.windowSize:
        #         for i in range(len(self.NumList) - self.windowSize, len(self.NumList)):
        #             if (i == self.currentIndex):
        #                 qp.drawRect(self.RectList[i])
        #                 qp.drawText(self.RectList[i], Qt.AlignCenter, self.NumList[i])
        #                 continue
        #             qp.drawRect(self.RectList[i])
        #     else:
        #         startIndex = int(self.currentIndex - self.windowSize / 2)
        #         for i in range(self.windowSize):
        #             if (startIndex + i == self.currentIndex):
        #                 qp.drawRect(self.RectList[i + startIndex])
        #                 qp.drawText(self.RectList[i + startIndex], Qt.AlignCenter, self.NumList[i + startIndex])
        #                 continue
        #             qp.drawRect(self.RectList[i + startIndex])
        qp.end()

class QCustomizeLabel(QLabel):
    def __init__(self,parent:QWidget,str :str):
        super(QCustomizeLabel, self).__init__(str,parent)
        self.parent = parent
        self.qpoint = QPoint(int(self.parent.width()/20),int(self.parent.height()/2))
        self.setGeometry(QRect(self.qpoint,QSize(100,50)))
    def paintEvent(self, a0: QtGui.QPaintEvent):
        super(QCustomizeLabel, self).paintEvent(a0)
        qp = QPainter(self)
        qp.begin(self)
        qp.drawRect(self.rect().adjusted(0,0,-1,-1))
        qp.drawRoundedRect(self.rect().adjusted(0,0,-1,-1),10,10)
        qp.end()

class Meta:
    def __init__(self):
        self.listx :float = []
        self.listy :Decimal = []
        self.functionStr :str= ""
        self.type :int = -1