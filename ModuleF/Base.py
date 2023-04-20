from typing import List

from PyQt5 import QtGui
from PyQt5.QtCore import QObject, QRect, QPoint, QSize, Qt, QTimer
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget

from ModuleBase.BaseObject import DataGenerator


class STATUS:
    NONE = 0
    UNSROTED = -1
    SORTED = 1
    WORKING = 2

class Rect(QObject):
    def __init__(self,num,point :QPoint,size:QSize):
        super(Rect, self).__init__()
        self.rect = QRect(point,size)
        self.num :int = num
        self.Status = STATUS.NONE
        self.Sequence = -1

class SrotedWay(QWidget):
    def __init__(self,parent):
        super(SrotedWay, self).__init__(parent)
        self.RectList :List[Rect] = []
        self.AnimationTime = 1000
        self.cellWidth = 5
        self.cellHeight = 5
        self.leftGap = 5
        self.bottomGap = 5
        print("work",parent.geometry())
        self.setGeometry(0,0,parent.rect().width(),parent.rect().height())
    def ReStatus(self):
        self.RectList: List[Rect] = []
        self.cellWidth = 5
        self.cellHeight = 5
        self.leftGap = 5
        self.bottomGap = 5
        self.setGeometry(0, 0, self.parentWidget().width(), self.parentWidget().height())
    def InitalList(self,size :int):
        dg = DataGenerator()
        num :List = dg.GenerateList(size)
        startPoint :QPoint = self.__GetLeftBottom(size)
        print(startPoint)
        seq = 0
        for i in num:
            rect = Rect(i,QPoint(startPoint.x()+seq*self.cellWidth,\
                                 startPoint.y()-i*self.cellHeight),\
                        QSize(self.cellWidth,i*self.cellHeight))
            self.RectList.append(rect)
            seq+=1
        self.repaint()
        print(self.RectList.__str__())

    def __GetLeftBottom(self,size:int):

        center = self.rect().center()
        baseW = int(self.width()/size)
        baseH = int(self.height()/size)
        if baseH>self.cellHeight:
            self.cellHeight = baseH
        if baseW>self.cellWidth:
            self.cellWidth = baseW
        startX = int(center.x() - self.cellWidth*size/2)
        if(startX<0):
            startX = self.leftGap
        return QPoint(startX,self.height()-self.bottomGap)

    def paintEvent(self, a0: QtGui.QPaintEvent):
        super(SrotedWay, self).paintEvent(a0)
        qp = QPainter(self)
        qp.begin(self)
        qp.drawRect(self.rect())
        print(self.geometry())
        for i in self.RectList:
            if i.Status == STATUS.NONE:
                qp.drawRect(i.rect)
                qp.drawText(i.rect,Qt.AlignCenter,i.num.__str__())
            elif i.Status == STATUS.WORKING:
                qp.setBrush(QColor("#55aaff"))
                qp.drawRect(i.rect)
                qp.drawText(i.rect, i.num)
                qp.setBrush(Qt.NoBrush)
            elif i.Status == STATUS.SORTED:
                qp.setBrush(QColor("#00ff7f"))
                qp.drawRect(i.rect)
                qp.drawText(i.rect,i.num)
                qp.setBrush(Qt.NoBrush)
        qp.end()

    def BubbleSort(self):
        self.length = len(self.RectList)
        self.__setattr__("BubbleI",1)
        self.__setattr__("BubbleJ",0)
        self.bubbleTimer = QTimer()
        self.bubbleTimer.setInterval(1000)
        self.bubbleTimer.timeout.connect(self.__BubbleOneStep)
        self.bubbleTimer.start()
    def __BubbleOneStep(self):
        if self.BubbleI < self.length:
            if self.BubbleJ < self.length -self.BubbleI-1:
                if(self.RectList[self.BubbleJ].num > self.RectList[self.BubbleI].num):
                    self.RectList[self.BubbleJ],self.RectList[self.BubbleI] = self.RectList[self.BubbleI],self.RectList[self.BubbleJ]
                    self.RectList[self.BubbleJ].rect.setX(self.RectList[self.BubbleJ].rect.x()+self.cellWidth)
                    self.RectList[self.BubbleI].rect.setX(self.RectList[self.BubbleI].rect.x() - self.cellWidth)
                    self.repaint()
                    return
        self.bubbleTimer.stop()
        return
    def SelectSort(self):
        pass
