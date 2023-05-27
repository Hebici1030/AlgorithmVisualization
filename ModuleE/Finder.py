import random
import sys

import matplotlib
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from ModuleBase.BaseObject import QCustomizeList, ArrowLabel, DataGenerator, SearchWay, QCustomizeHash, QCustomizeLabel
from ModuleE.UI import Ui_UI


class Finder(QMainWindow):
    def __init__(self):
        super(Finder, self).__init__()
        self.ui = Ui_UI()
        self.ui.setupUi(UI=self)
        self.initialValue()
        self.connectSlot()
        # self.initalUI()
        self.InitiPlot()
    def initialValue(self):
        self.AnimationTime = 1000
        self.search = SearchWay()
        self.ui.SearchWay.addItem(self.search.LINERSEARCH)
        self.ui.SearchWay.addItem(self.search.BINARYSEARCH)
        self.ui.HashFuntion.addItem(self.search.MODSEARCH)
        self.ui.Collapes.addItem(self.search.LINEARPROBING)
        self.ui.Collapes.addItem(self.search.QUADRATICPROBING)
        # self.ui.Collapes.addItem(self.search.SEPARATECHAING)
        self.LeftIndex = 0
        self.RightIndex = 0
        self.ordered = False
        self.AnimationTimer = QTimer()
        self.AnimationTimer.setInterval(self.AnimationTime)
        self.Initaltimer = QTimer()
        self.Initaltimer.setSingleShot(True)
        self.Initaltimer.setInterval(10)
        self.Initaltimer.timeout.connect(self.initalUI)
        self.Initaltimer.start()
        self.ax=["线性查找", "二分查找"]
        self.colors = ["red","blue"]
        self.ay = [0,0]
        #UI组件
        self.Arrow = None
        self.list  = None
        self.map = None
        self.mapfunction = None
        self.time = 0
    def InitiPlot(self):
        plt.ion()
        matplotlib.rc("font",family='YouYuan')
        self.fig,self.pax = plt.subplots()
        self.pax.bar(self.ax,self.ay)
        self.pax.set_xlabel("FindWay")
        self.pax.set_ylabel("Way")
        self.pax.set_title("Times")
        self.canvas = FigureCanvas(self.fig)
        self.ui.verticalLayout_6.addWidget(self.canvas)
    def initalUI(self):
        index = self.ui.tabWidget.currentIndex()
        if index==0:
            self.Arrow = ArrowLabel(parent=self.ui.widget)
            self.list = QCustomizeList(parent=self.ui.widget)
            self.ui.verticalLayout_7.addWidget(self.list)
            self.Arrow.show()
            self.list.show()
        elif index==1:

            self.map = QCustomizeHash(parent=self.ui.HashWidget)
            self.mapfunction = QCustomizeLabel(str=" Key:", parent=self.ui.HashWidget)
            self.map.show()
            self.map.message.message.connect(self.MapInfo)
            self.map.message.stop.connect(self.stopA)
            self.mapfunction.show()
    def stopA(self):
        self.showMessage("无法找到空槽用于插入当前值")
    def changeUI(self,index):
        if index==0:
            self.ListUI()
        elif index==1:
            self.MapUI()
    def ListUI(self):
        if(self.Arrow!=None):
            return
        self.Arrow = ArrowLabel(parent=self.ui.widget)
        self.list = QCustomizeList(parent=self.ui.widget)
        self.ui.verticalLayout_7.addWidget(self.list)
        self.Arrow.show()
        self.list.show()
    def MapUI(self):
        if(self.map!=None):
            return
        self.map = QCustomizeHash(parent=self.ui.HashWidget)
        self.mapfunction = QCustomizeLabel(str=" Key:", parent=self.ui.HashWidget)
        self.map.show()
        self.map.message.message.connect(self.MapInfo)
        self.map.message.stop.connect(self.stopA)
        self.mapfunction.show()
    def MapInfo(self):
        temp = self.MapDetail()
        str = "哈希表Size:{}\n" \
              "哈希表Capacity:{}\n" \
              "哈希表Hash函数:{}\n" \
              "哈希表碰撞处理方法:{}\n" \
              "当前运行碰撞次数:{}\n" \
              "当前哈希表存储一览：\n {}".format(len(self.map.NumList),self.map.capacity,self.ui.HashFuntion.currentText(),
                                     self.ui.Collapes.currentText(),self.map.collpseTime,temp)

        self.ui.textBrowser.setText(str)
    def MapDetail(self):
        if self.map==None:
            return
        if len(self.map.NumList)==0:
            return
        str = ""
        for i in range(len(self.map.NumList)):
            if self.map.NumList[i]=="None":
                continue
            str+="key:{}->Value:{},".format(i,self.map.NumList[i])
        return "[" + str[0:-1] + "]"

    def connectSlot(self):
        self.ui.ListInital.editingFinished.connect(self.InitalList)
        self.AnimationTimer.timeout.connect(self.FindTarget)
        self.ui.start.clicked.connect(self.AnimationTimer.start)
        self.ui.HashSize.editingFinished.connect(self.InitalHash)
        self.ui.MapInsert.clicked.connect(self.hashInsert)
        self.ui.tabWidget.currentChanged.connect(self.UIrepaint)
        self.ui.MapSearch.clicked.connect(self.hashFind)
        self.ui.tabWidget.currentChanged.connect(self.changeUI)

    def UIrepaint(self,index):
        if(index==0):
            self.ui.widget.update()
        elif index == 1:
            self.ui.HashWidget.update()
    def InitalHash(self):
        str = self.ui.HashSize.text()
        if str=='':
            return
        size = int(self.ui.HashSize.text())
        self.map.setSize(size=size)
        for i in range(size):
            self.map.NumList.append("None")
            # j = i%size
            self.map.RectList.append(QRect(QPoint(0,int(self.map.RectSize.height()*i)),\
                                           self.map.RectSize))
        for i in range(self.map.Initalcapacity):
            value = random.randint(0, len(self.map.NumList)*2)
            key = self.map.ModHash(value)
            self.map.NumList[key] = value
        self.MapInfo()
        self.map.repaint()
    def hashFind(self):
        self.HashFindTarget()
    def HashFindTarget(self):
        if self.ui.KeyEditor.text() == "":
            return
        self.MapInfo()
        self.map.collpseTime=0
        key = int(self.ui.KeyEditor.text())
        self.mapfunction.setText("Key:{}".format(key))
        index = self.map.ModHash(key)
        self.map.currentIndex = index
        self.map.MoveCenter()
        self.MapInfo()
        if self.map.NumList[index]=="None":
            self.showMessage("当前下标内容:{}为空，说明哈希表中没有数值:{}".format(index, key))
            return
        if (self.map.NumList[index] != "None"):
            if (self.map.NumList[index] == key):
                self.showMessage("当前下标内容:{}为{}，与查找对象相同，停止哈希".format(index, self.map.NumList[index], ))
                return
            self.map.Target = key
            if(self.ui.Collapes.currentText()==self.search.LINEARPROBING):
                self.map.LineCollideTimer.start()
            # elif (self.ui.Collapes.currentText()==self.search.SEPARATECHAING):
            #     print("进入链表碰撞")
            else:
                print("进入二次碰撞")
    def hashInsert(self):
        self.HashInsertTarget()
        # self.map.currentIndex = random.randint(0,9)
        # print(self.map.currentIndex)
        # self.map.MoveCenter()
    def HashInsertTarget(self):
        if self.ui.KeyValue.text()=='':
            self.showMessage("请先输入需要查找的数值")
            return
        key = int(self.ui.KeyValue.text())

        index = self.map.ModHash(key)
        self.map.currentIndex = index
        self.map.MoveCenter()
        if(self.map.NumList[index]=="None"):
            self.showMessage("当前下标内容:{}为空，说明哈希表中没有数值:{},因此在表中插入数值：{}".format(index,key,key))
            self.map.NumList[self.map.currentIndex] = key
            self.map.capacity+=1
            self.map.repaint()
            self.map.MoveCenter()
            return
        if(self.map.NumList[index]!="None"):
            self.showMessage("当前下标内容:{}为{}，发生了哈希碰撞,调用碰撞处理方法".format(index, self.map.NumList[index],
                                                                    self.ui.Collapes.currentText()))
            if(self.map.NumList[index]==key):
                self.showMessage("当前下标内容:{}为{}，与查找对象相同，停止哈希".format(index, self.map.NumList[index],))
                return
            self.map.Target = key
            self.map.LineCollideTimer.start()
        self.MapInfo()

    def InitalList(self):
        if self.ui.ListInital.text() == '' :
            return
        dg = DataGenerator()
        self.list.NumList = dg.GenerateList(int(self.ui.ListInital.text()))
        self.list.RectList = []
        self.list.currentIndex = 0
        self.list.currentRectIndex = 0
        self.LeftIndex = 0
        self.RightIndex = len(self.list.NumList)
        self.list.repaint()
        self.ordered = False

    #currentIndex下标，RectList为窗口.如果
    def FindTarget(self):
        if(self.ui.SearchWay.currentText()==SearchWay().LINERSEARCH):
            self.LinerSearch()
        else:
            if not self.ordered:
                self.list.NumList = sorted(self.list.NumList)
                self.list.RectList = []
                self.list.currentIndex = 0
                self.list.currentRectIndex = 0
                self.list.repaint()
                self.ordered = True
            self.BinarySearch()
    def BinarySearch(self):
        mid = ((self.RightIndex - self.LeftIndex)>>1) + self.LeftIndex
        num = self.list.NumList[mid]
        rect = self.list.RectList[mid]
        self.showMessage("当前mid下标：{}，数组该下标下的数字：{}".format(self.list.currentIndex, num))
        self.MoveArrow(rect=rect)
        self.time +=1
        self.ay[1] = self.time
        self.pax.bar(self.ax, self.ay,color=self.colors)
        self.canvas.draw()
        if num > int(self.ui.ListTarget.text()):
            self.showMessage("当前mid下标：{}，数组该下标下的数字：{}大于查找数值：{}".format(mid,num,int(self.ui.ListTarget.text())))
            self.RightIndex = mid-1
        elif num < int(self.ui.ListTarget.text()):
            self.showMessage("当前mid下标：{}，数组该下标下的数字：{}小于查找数值：{}".format(mid, num, int(self.ui.ListTarget.text())))
            self.LeftIndex = mid+1
        else:
            self.showMessage("当前下标：{}，数组该下标下的数字：{},找到目标数字".format(mid, num))
            self.AnimationTimer.stop()
            return
    def LinerSearch(self):
        if (self.ui.ListTarget.text() == ''):
            self.AnimationTimer.stop()
            return
        if self.list.currentIndex >= len(self.list.NumList):
            self.showMessage("当前数组没有数值:{}".format(int(self.ui.ListTarget.text())))
            self.AnimationTimer.stop()
            return
        if self.list.Windowindex > self.list.totalCellNum:
            print("suit")
            self.list.Windowindex = 0;
            self.list.setGeometry(0-self.list.cellSize.width()*self.list.currentIndex,
                                  int(self.list.widget.height()/2+self.list.cellSize.height()/2),self.list.cellSize.width()*len(self.list.NumList),self.list.cellSize.height())
            print(self.list.geometry())
            self.list.update()
        num = self.list.NumList[self.list.currentIndex]
        rect = self.list.RectList[self.list.currentRectIndex]
        self.showMessage("当前下标：{}，数组该下标下的数字：{}".format(self.list.currentIndex, num))
        self.MoveArrow(rect=rect)
        self.ay[0] = self.list.currentIndex
        self.pax.bar(self.ax,self.ay,color =self.colors)
        self.canvas.draw()
        if (num == int(self.ui.ListTarget.text())):
            self.AnimationTimer.stop()
            self.showMessage("当前下标：{}，数组该下标下的数字：{},找到目标数字".format(self.list.currentIndex, num))
            self.list.currentIndex = 0
            self.list.currentRectIndex = 0
            self.AnimationTimer.stop()
            return
        self.list.currentIndex += 1
        self.list.Windowindex +=1
        self.list.currentRectIndex += 1
    def MoveArrow(self,rect :QRect):
        animation = QPropertyAnimation(self.Arrow,b'geometry',self.ui.widget)
        animation.setDuration(self.AnimationTime-800)
        animation.setStartValue(self.Arrow.geometry())
        if self.list.Windowindex > self.list.totalCellNum:
            animation.setEndValue(QRect(QPoint(int((rect.center().x()-self.list.cellSize.width()*self.list.currentIndex - self.Arrow.width() / 2)) \
                                               , int(self.list.y() - self.Arrow.height() - 10)), self.Arrow.size()))
        else:
            animation.setEndValue(QRect(QPoint(int(rect.center().x()-self.Arrow.width()/2)\
                                           ,int(self.list.y()-self.Arrow.height()-10)),self.Arrow.size()))
        animation.start()
    def showMessage(self,messgae:str):
        self.statusBar().showMessage(messgae,5000)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Finder()
    win.show()
    sys.exit(app.exec_())