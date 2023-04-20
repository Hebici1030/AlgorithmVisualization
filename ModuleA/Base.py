from typing import List

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ModuleBase.BaseObject import DataGenerator
class Signal(QObject):
    enableBtn = pyqtSignal()
class STATUS:
    UNSROTED = 0
    SORTED = 1
    INDEXI = 2
    INDEXJ = 3
    COMPARING = 4

    SORTEDCOLOR = "#59f7ff"
    INDEXICOLOR = "#fff45c"
    INDEXJCOLOR = "#2097ff"
    COMPARINGCOLOR = "#ff2e2e"
class Rect(QWidget):
    def __init__(self,parent,rect:QRect,num:int,color:str):
        super(Rect, self).__init__(parent)
        self.rect :QRect = rect
        self.num :int= num
        self.status = STATUS.UNSROTED
        self.setGeometry(self.rect)
        self.color:str = color
    def setRect(self,rect):
        self.rect = rect
        self.setGeometry(rect)
    def paintEvent(self, a0: QtGui.QPaintEvent):
        super(Rect, self).paintEvent(a0)
        qp = QPainter(self)
        qp.begin(self)
        if self.status==STATUS.UNSROTED :
            qp.setBrush(QColor(self.color))
            temprect = QRect(0,0,self.rect.width(),self.rect.height()).adjusted(0,0,-1,-1)
            qp.drawRect(temprect)
            qp.drawText(temprect,Qt.AlignCenter,str(self.num))
            qp.setBrush(Qt.NoBrush)
        elif self.status == STATUS.SORTED:
            qp.setBrush(QColor(STATUS.SORTEDCOLOR))
            temprect = QRect(0, 0, self.rect.width(), self.rect.height()).adjusted(0, 0, -1, -1)
            qp.drawRect(temprect)
            qp.drawText(temprect, Qt.AlignCenter, str(self.num))
            qp.setBrush(Qt.NoBrush)
        elif self.status == STATUS.INDEXJ:
            qp.setBrush(QColor(STATUS.INDEXJCOLOR))
            temprect = QRect(0, 0, self.rect.width(), self.rect.height()).adjusted(0, 0, -1, -1)
            qp.drawRect(temprect)
            qp.drawText(temprect, Qt.AlignCenter, str(self.num))
            qp.setBrush(Qt.NoBrush)
        elif self.status == STATUS.INDEXI:
            qp.setBrush(QColor(STATUS.INDEXICOLOR))
            temprect = QRect(0, 0, self.rect.width(), self.rect.height()).adjusted(0, 0, -1, -1)
            qp.drawRect(temprect)
            qp.drawText(temprect, Qt.AlignCenter, str(self.num))
            qp.setBrush(Qt.NoBrush)
        elif self.status == STATUS.COMPARING:
            qp.setBrush(QColor(STATUS.COMPARINGCOLOR))
            temprect = QRect(0, 0, self.rect.width(), self.rect.height()).adjusted(0, 0, -1, -1)
            qp.drawRect(temprect)
            qp.drawText(temprect, Qt.AlignCenter, str(self.num))
            qp.setBrush(Qt.NoBrush)
        qp.end()
class AnimationWidget(QWidget):
    def __init__(self,parent):
        super(AnimationWidget, self).__init__(parent)
        self.rectList :List[Rect] = []
        self.CellTime = 100
        self.baseHeight = 5
        self.baseWidget = 5
        self.indexI = 0
        self.indexJ = 0
        self.leftGap = 0
        self.bottomGap = 0
        self.fisrtStart = True

        self.signalObject = Signal()

    def ReInital(self):
        for i in self.rectList:
            i.setParent(None)
            i.deleteLater()
        self.rectList: List[Rect] = []
        self.CellTime = 100
        self.baseHeight = 5
        self.baseWidget = 5
        self.indexI :int= 0
        self.indexJ :int= 0
        self.basecolor = "#29ffad"
    def RandomInitalRectList(self,size:int):
        dg = DataGenerator()
        tempList = dg.GenerateList(size)
        startPoint = self.__GetLeftBottom(size=size)
        index = 0
        for i in tempList:
            qrect = QRect(QPoint(startPoint.x()+index*self.baseWidget,\
                         startPoint.y()-i*self.baseHeight),QSize(self.baseWidget,i*self.baseHeight))
            c = QColor(self.basecolor)
            c.darker(100)
            print(c.name())
            rect = Rect(parent=self,rect=qrect,num=i,color=c.name())
            self.rectList.append(rect)
            index+=1
        if len(self.rectList) !=0:
            for i in self.rectList:
                i.show()
                i.update()

    def __GetLeftBottom(self, size: int):
        center = self.rect().center()
        baseW = int(self.width() / size)
        baseH = int(self.height() / size)
        if baseH > self.baseHeight:
            self.baseHeight = baseH
        if baseW > self.baseWidget:
            self.baseWidget = baseW
        startX = int(center.x() - self.baseWidget * size / 2)
        if (startX <= 0):
            startX = self.leftGap
        return QPoint(startX, self.height() - self.bottomGap)
    def paintEvent(self, a0: QtGui.QPaintEvent):
        super(AnimationWidget, self).paintEvent(a0)
        qp = QPainter(self)
        qp.begin(self)
        qp.drawRect(self.rect().adjusted(0,0,-1,-1))
        qp.end()
    def StartBubble(self):
        if self.fisrtStart:
            self.indexI = 0
            self.indexJ = 0
            self.fisrtStart=False
        self.CellTime = 100
        self.AnimationTimer = QTimer()
        self.AnimationTimer.setInterval(self.CellTime*10)
        self.AnimationTimer.timeout.connect(self.OneStep)
        self.AnimationTimer.start()
    def OneStep(self):
        print(self.indexI,self.indexJ)
        if self.indexI < len(self.rectList):
            # self.rectList[self.indexI].status = STATUS.INDEXI
            # self.rectList[self.indexI].repaint()
            if self.indexJ < len(self.rectList)-self.indexI-1:
                # if(self.indexI!=self.indexJ):
                self.rectList[self.indexJ].status = STATUS.INDEXJ
                self.rectList[self.indexJ].repaint()
                if self.rectList[self.indexJ].num > self.rectList[self.indexJ+1].num:
                    #更新状态
                    # self.rectList[self.indexJ + 1].status = STATUS.COMPARING
                    # self.rectList[self.indexJ + 1].repaint()
                    # self.rectList[self.indexJ].setRect(QRect(
                    #     QPoint(self.rectList[self.indexJ].rect.x()+self.baseWidget,\
                    #                                                self.rectList[self.indexJ].rect.y()),\
                    #                                         self.rectList[self.indexJ].rect.size()))
                    an = QPropertyAnimation(self.rectList[self.indexJ],b'geometry',self)
                    an.setDuration(self.CellTime*5)
                    an.setStartValue(QRect(
                        QPoint(self.rectList[self.indexJ].rect.x(),\
                                                                   self.rectList[self.indexJ].rect.y()),\
                                                            self.rectList[self.indexJ].rect.size()))
                    an.setEndValue(QRect(
                        QPoint(self.rectList[self.indexJ].rect.x()+self.baseWidget,\
                                                                   self.rectList[self.indexJ].rect.y()),\
                                                            self.rectList[self.indexJ].rect.size()))
                    self.rectList[self.indexJ].setRect(QRect(
                        QPoint(self.rectList[self.indexJ].rect.x()+self.baseWidget,\
                                                                   self.rectList[self.indexJ].rect.y()),\
                                                            self.rectList[self.indexJ].rect.size()))
                    bn = QPropertyAnimation(self.rectList[self.indexJ+1], b'geometry',self)

                    bn.setDuration(self.CellTime*5)
                    bn.setStartValue(QRect(
                        QPoint(self.rectList[self.indexJ+1].rect.x(), \
                               self.rectList[self.indexJ+1].rect.y()), \
                        self.rectList[self.indexJ+1].rect.size()))
                    bn.setEndValue(QRect(
                        QPoint(self.rectList[self.indexJ+1].rect.x() - self.baseWidget, \
                               self.rectList[self.indexJ+1].rect.y()), \
                        self.rectList[self.indexJ+1].rect.size()))
                    self.rectList[self.indexJ+1].setRect(QRect(
                        QPoint(self.rectList[self.indexJ+1].rect.x() - self.baseWidget, \
                               self.rectList[self.indexJ+1].rect.y()), \
                        self.rectList[self.indexJ+1].rect.size()))
                    an.start()
                    bn.start()

                    self.rectList[self.indexJ],self.rectList[self.indexJ+1] = \
                        self.rectList[self.indexJ+1], self.rectList[self.indexJ]

                    self.indexJ+=1
                    return
                self.rectList[self.indexJ + 1].status = STATUS.INDEXJ
                self.rectList[self.indexJ + 1].repaint()
                self.rectList[self.indexJ ].status = STATUS.UNSROTED
                self.rectList[self.indexJ ].repaint()
                self.indexJ+=1
                return
            else:
                self.rectList[self.indexJ].status = STATUS.SORTED
                self.rectList[self.indexJ].repaint()
                self.indexJ=0
                self.indexI+=1
                return
        else:
            self.indexI=0
            self.indexJ=0
            self.fisrtStart = True
            self.signalObject.enableBtn.emit()
            self.AnimationTimer.stop()

    def PauseBubble(self):
        self.AnimationTimer.stop()