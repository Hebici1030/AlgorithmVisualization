import time
from time import sleep
from typing import List

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ModuleBase.BaseObject import DataGenerator
class Signal(QObject):
    enableBtn = pyqtSignal()
    refreshInfo = pyqtSignal()
    suitWindow = pyqtSignal()
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
        self.setMouseTracking(True)
        self.end =-1
    def setRect(self,rect):
        self.rect = rect
        self.setGeometry(rect)
    def enterEvent(self, a0):
        super(Rect, self).enterEvent(a0)
        if self.status == STATUS.UNSROTED:
            QToolTip.showText(QCursor.pos(),"当前坐标后矩形未排序")
        elif self.status == STATUS.SORTED:
            QToolTip.showText(QCursor.pos(),"当前坐标后矩形已排序")
        elif self.status == STATUS.INDEXI:
            QToolTip.showText(QCursor.pos(),"外循环参数I指向当前矩形")
        elif self.status == STATUS.INDEXJ:
            QToolTip.showText(QCursor.pos(), "内循环参数J指向当前矩形")
        elif self.status == STATUS.COMPARING:
            QToolTip.showText(QCursor.pos(), "内循环J矩形与当前矩形进行比较")

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
        elif self.status == STATUS.COMPARING:
            qp.setBrush(QColor(STATUS.COMPARINGCOLOR))
            temprect = QRect(0, 0, self.rect.width(), self.rect.height()).adjusted(0, 0, -1, -1)
            qp.drawRect(temprect)
            qp.drawText(temprect, Qt.AlignCenter, str(self.num))
            qp.setBrush(Qt.NoBrush)

        if self.end == STATUS.INDEXI:
            qp.setPen(QPen(Qt.black, 5))
            # qp.setBrush(QColor(STATUS.INDEXICOLOR))
            qp.setBrush(QColor(STATUS.SORTEDCOLOR))
            temprect = QRect(0, 0, self.rect.width(), self.rect.height()).adjusted(0, 0, -1, -1)
            qp.drawRect(temprect)
            qp.drawText(temprect, Qt.AlignCenter, str(self.num))
            qp.setBrush(Qt.NoBrush)
        qp.end()

class AnimationWidget(QWidget):
    def __init__(self,parent):
        super(AnimationWidget, self).__init__(parent)
        self.rectList :List[Rect] = []
        self.tempList = []
        self.BackList =[]
        self.CellTime = 100
        self.baseTime = 5
        self.baseHeight = 5
        self.baseWidget = 5
        self.indexI = 0
        self.indexJ = 0
        self.leftGap = 0
        self.bottomGap = 0
        self.fisrtStart = True
        self.compareTime = 0
        self.swapTime = 0
        self.signalObject = Signal()
        self.AnimationTimer = QTimer()
        self.basecolor = "#29ffad"
        self.resizeEvent = self.my_resieze
    def ReInital(self):
        for i in self.rectList:
            i.setParent(None)
            i.deleteLater()
        self.rectList: List[Rect] = []
        self.CellTime = 100
        self.baseTime = 5
        self.baseHeight = 5
        self.baseWidget = 5
        self.indexI :int= 0
        self.indexJ :int= 0
        self.compareTime = 0
        self.swapTime = 0
        self.basecolor = "#29ffad"
    def __SendInfo(self):
        self.signalObject.refreshInfo.emit()
    def RandomInitalRectList(self,size:int):
        dg = DataGenerator()
        self.tempList = dg.GenerateList(size)
        self.BackList = self.tempList.copy()
        startPoint = self.__GetLeftBottom(size=size)
        index = 0
        for i in self.tempList:
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
        self.__SendInfo()
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
    def my_resieze(self,event):
        self.__SuitWindow()
    def __SuitWindow(self):

        self.ReInital()
        if( len(self.tempList)<=0):
            return
        startPoint = self.__GetLeftBottom(size=len(self.tempList))
        index = 0
        for i in self.tempList:
            qrect = QRect(QPoint(startPoint.x() + index * self.baseWidget, \
                                 startPoint.y() - i * self.baseHeight), QSize(self.baseWidget, i * self.baseHeight))
            c = QColor(self.basecolor)
            c.darker(100)
            print(c.name())
            rect = Rect(parent=self, rect=qrect, num=i, color=c.name())
            self.rectList.append(rect)
            index += 1
        if len(self.rectList) != 0:
            for i in self.rectList:
                i.show()
                i.update()
        self.__SendInfo()
    def StartBubble(self):
        if self.fisrtStart:
            self.indexI = 0
            self.indexJ = 0
            self.fisrtStart=False
        self.AnimationTimer.setInterval(self.CellTime*self.baseTime*2)
        self.AnimationTimer.timeout.connect(self.OneStep)
        self.AnimationTimer.start()
        self.__SendInfo()
    def OneStep(self):
        #将上次一次迭代循环时状态更新
        for i in self.rectList:
            if i.status != STATUS.SORTED:
                i.status = STATUS.UNSROTED
                i.repaint()
            else:
                self.rectList[len(self.rectList)  - self.indexI].end = STATUS.INDEXI
        #外循环下标范围判断
        if self.indexI < len(self.rectList):
            #更新所有已排序矩形状态
            for i in range(len(self.rectList)):
                if i > (len(self.rectList) - self.indexI -1):
                    self.rectList[i].status = STATUS.SORTED
                    self.rectList[i].repaint()
            self.__SendInfo()
            #内循环下标范围判断
            if self.indexJ < len(self.rectList)-self.indexI-1:
                #更新内循环下表矩形状态以及与当前下表比较矩形的状态
                self.rectList[self.indexJ].status = STATUS.INDEXJ
                self.rectList[self.indexJ].repaint()
                self.rectList[self.indexJ+1].status = STATUS.COMPARING
                self.rectList[self.indexJ+1].repaint()
                self.compareTime+=1
                if self.rectList[self.indexJ].num > self.rectList[self.indexJ+1].num:
                    self.swapTime+=1
                    #当IndexJ矩形数据小于IndexJ+1矩形数据创建动画并运行
                    an = QPropertyAnimation(self.rectList[self.indexJ],b'geometry',self)
                    an.setDuration(self.CellTime*self.baseTime)
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

                    bn.setDuration(self.CellTime*self.baseTime)
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
                    self.tempList[self.indexJ],self.tempList[self.indexJ+1] = \
                        self.tempList[self.indexJ+1], self.tempList[self.indexJ]
                    an.start()
                    bn.start()
                    self.rectList[self.indexJ],self.rectList[self.indexJ+1] = \
                        self.rectList[self.indexJ+1], self.rectList[self.indexJ]
                    self.rectList[self.indexJ + 1].repaint()
                    self.rectList[self.indexJ].repaint()
                    self.indexJ+=1
                    self.__SendInfo()
                    return
                #当前内循环迭代下标范围没有变化
                self.indexJ+=1
                self.__SendInfo()
                return
            else:

                self.rectList[self.indexJ].repaint()
                self.indexJ=0
                self.indexI+=1
                self.__SendInfo()
                return
        else:
            self.__SendInfo()
            self.indexJ=0
            #将一次内循环结束后的IndexJ的状态设置为已排序
            self.rectList[self.indexJ].status = STATUS.SORTED
            self.rectList[self.indexJ].repaint()
            self.fisrtStart = True
            #发送信号使能恢复与单步执行按钮
            self.signalObject.enableBtn.emit()
            self.AnimationTimer.stop()

    # def SwapRect(self):
    #     self.rectList[self.indexJ + 1].status = STATUS.INDEXJ
    #     self.rectList[self.indexJ + 1].repaint()
    #     self.rectList[self.indexJ].status = STATUS.UNSROTED
    #     self.rectList[self.indexJ].repaint()
    def AddValue(self,num:int):
        self.ReInital()
        self.tempList.append(num)
        self.BackList.append(num)
        startPoint = self.__GetLeftBottom(size=len(self.tempList))
        if self.baseHeight*max(self.tempList) > self.rect().height():
            self.baseHeight = 5
        index = 0
        for i in self.tempList:
            qrect = QRect(QPoint(startPoint.x() + index * self.baseWidget, \
                                 startPoint.y() - i * self.baseHeight), QSize(self.baseWidget, i * self.baseHeight))
            c = QColor(self.basecolor)
            c.darker(100)
            print(c.name())
            rect = Rect(parent=self, rect=qrect, num=i, color=c.name())
            self.rectList.append(rect)
            index += 1
        if len(self.rectList) != 0:
            for i in self.rectList:
                i.show()
                i.update()
        self.__SendInfo()
    def Recover(self):
        self.ReInital()
        self.tempList = self.BackList
        startPoint = self.__GetLeftBottom(size=len(self.tempList))
        index = 0
        for i in self.tempList:
            qrect = QRect(QPoint(startPoint.x() + index * self.baseWidget, \
                                 startPoint.y() - i * self.baseHeight), QSize(self.baseWidget, i * self.baseHeight))
            c = QColor(self.basecolor)
            c.darker(100)
            print(c.name())
            rect = Rect(parent=self, rect=qrect, num=i, color=c.name())
            self.rectList.append(rect)
            index += 1
        if len(self.rectList) != 0:
            for i in self.rectList:
                i.show()
                i.update()
        self.__SendInfo()
    def PauseBubble(self):
        self.AnimationTimer.stop()
    def ChangeBaseTime(self,num:int):
        self.baseTime = num
        self.AnimationTimer.setInterval(self.CellTime * self.baseTime * 2)