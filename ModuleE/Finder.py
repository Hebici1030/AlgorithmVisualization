import random
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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
    def initialValue(self):
        self.AnimationTime = 1000
        self.search = SearchWay()
        self.ui.SearchWay.addItem(self.search.LINERSEARCH)
        self.ui.SearchWay.addItem(self.search.BINARYSEARCH)
        self.ui.HashFuntion.addItem(self.search.MODSEARCH)
        self.ui.Collapes.addItem(self.search.LINEARPROBING)
        self.ui.Collapes.addItem(self.search.QUADRATICPROBING)
        self.ui.Collapes.addItem(self.search.SEPARATECHAING)
        self.LeftIndex = 0
        self.RightIndex = 0
        self.ordered = False
        self.AnimationTimer = QTimer()
        self.AnimationTimer.setInterval(self.AnimationTime)
        self.Initaltimer = QTimer()
        self.Initaltimer.setSingleShot(True)
        self.Initaltimer.setInterval(1000)
        self.Initaltimer.timeout.connect(self.initalUI)
        self.Initaltimer.start()

    def initalUI(self):
        self.Arrow = ArrowLabel(parent=self.ui.widget)
        self.list = QCustomizeList(parent=self.ui.widget)
        self.Arrow.show()
        self.list.show()

        self.map = QCustomizeHash(parent=self.ui.HashWidget)
        self.mapfunction = QCustomizeLabel(str="Key:",parent=self.ui.HashWidget)
        self.map.show()
        self.mapfunction.show()

    def MapInfo(self):
        str = "哈希表Size:{}\n" \
              "哈希表Capacity:{}\n" \
              "哈希表Hash函数:{}\n" \
              "哈希表碰撞处理方法:{}\n" \
              "当前运行碰撞次数:{}\n".format(len(self.map.NumList),self.map.capacity,self.ui.HashFuntion.currentText(),
                                     self.ui.Collapes.currentText(),self.map.collpseTime)
        self.ui.MapINFO.setText(str)
    def connectSlot(self):
        self.ui.ListInital.editingFinished.connect(self.InitalList)
        self.AnimationTimer.timeout.connect(self.FindTarget)
        self.ui.start.clicked.connect(self.AnimationTimer.start)
        self.ui.HashSize.editingFinished.connect(self.InitalHash)
        self.ui.MapInsert.clicked.connect(self.hashInsert)
        self.ui.tabWidget.currentChanged.connect(self.UIrepaint)
        self.ui.MapSearch.clicked.connect(self.hashFind)
    def UIrepaint(self,index):
        if(index==0):
            print("update")
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
        print(self.map.NumList.__str__())
        print(self.map.RectList.__str__())
        self.map.repaint()
    def hashFind(self):
        self.HashFindTarget()
    def HashFindTarget(self):
        if self.ui.KeyEditor.text() == "":
            return
        self.map.collpseTime=0
        key = int(self.ui.KeyEditor.text())
        index = self.map.ModHash(key)
        self.map.currentIndex = index
        self.map.MoveCenter()
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
        num = self.list.NumList[self.list.currentIndex]
        rect = self.list.RectList[self.list.currentRectIndex]
        self.showMessage("当前下标：{}，数组该下标下的数字：{}".format(self.list.currentIndex, num))
        self.MoveArrow(rect=rect)
        if (num == int(self.ui.ListTarget.text())):
            self.AnimationTimer.stop()
            self.showMessage("当前下标：{}，数组该下标下的数字：{},找到目标数字".format(self.list.currentIndex, num))
            self.list.currentIndex = 0
            self.list.currentRectIndex = 0
            self.AnimationTimer.stop()
            return
        self.list.currentIndex += 1
        self.list.currentRectIndex += 1
    def MoveArrow(self,rect :QRect):
        animation = QPropertyAnimation(self.Arrow,b'geometry',self.ui.widget)
        animation.setDuration(self.AnimationTime-800)
        animation.setStartValue(self.Arrow.geometry())
        print(self.Arrow.geometry())
        animation.setEndValue(QRect(QPoint(int(rect.center().x()-self.Arrow.width()/2)\
                                           ,int(self.list.y()-self.Arrow.height()-10)),self.Arrow.size()))
        print(self.Arrow.geometry())
        print(self.Arrow)
        print(QPoint(int(rect.center().x()-self.Arrow.width()/2)\
                                           ,int(self.list.y()-10)).__str__())
        animation.start()
    def showMessage(self,messgae:str):
        self.statusBar().showMessage(messgae,5000)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Finder()
    win.show()
    sys.exit(app.exec_())