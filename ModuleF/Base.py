from typing import List

from PyQt5 import QtGui
from PyQt5.QtCore import QObject, QRect, QPoint, QSize, Qt, QTimer, QThread
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import  Figure
from matplotlib import *
import matplotlib.pyplot as plt

from ModuleBase.BaseObject import DataGenerator


class STATUS:
    NONE = 0
    UNSROTED = -1
    SORTED = 1
    WORKING = 2
class Method:
    BUBBLESORT= "冒泡排序"
    SELECTSORT = "选择排序"
    INSERTSORT = "插入排序"
    DUMPSORT = "堆排序"
    MERGERSORT = "归并排序"
    QUICKSORT = "快速排序"
    BUCKETSORT = "桶排序"
    SHELLSORT =  "希尔排序"
    COUNTINGSORT = "计数排序"
    RADIXSORT = "基数排序"



class Rect(QObject):
    def __init__(self,num,point :QPoint,size:QSize):
        super(Rect, self).__init__()
        self.rect = QRect(point,size)
        self.num :int = num
        self.Status = STATUS.NONE
        self.Sequence = -1
    def __lt__(self,other):
        return self.num < other.num;
class sortThread(QThread):
    def __init__(self,sw):
        super(sortThread, self).__init__()
        self.sw = sw
        self.methodName = Method()
        self.switcher = {
            self.methodName.BUBBLESORT: self.sw.BubbleSort,
            self.methodName.QUICKSORT: self.sw.QuickSort,
            self.methodName.SHELLSORT: self.sw.ShellSort,
            self.methodName.BUCKETSORT: self.sw.BucketSort,
            self.methodName.INSERTSORT: self.sw.InsertSort,
            self.methodName.SELECTSORT: self.sw.SelectSort,
            self.methodName.MERGERSORT: self.sw.MergeSort
        }
    def run(self):
        pass
class SrotedWay(QWidget):
    def __init__(self,parent):
        super(SrotedWay, self).__init__(parent)
        self.RectList :List[Rect] = []
        self.PrvRectList :List[Rect] = []
        self.AnimationTime = 1000
        self.cellWidth = 5
        self.constantWidth = 5
        self.constantHeight = 5
        self.cellHeight = 5
        self.leftGap = 5
        self.bottomGap = 5
        self.setGeometry(0,0,parent.rect().width(),parent.rect().height())
        self.compare = 0
        self.move = 0
        self.resizeEvent = self.__myresize
    def BackStatus(self):
        self.RectList.clear()
        for i in self.PrvRectList:
            self.RectList.append(Rect(i.num,i.rect.topLeft(),i.rect.size()))
        self.repaint()
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
        self.startPoint :QPoint = self.__GetLeftBottom(size)
        seq = 0
        for i in num:
            rect = Rect(i,QPoint(self.startPoint.x()+seq*self.cellWidth,\
                                 self.startPoint.y()-i*self.cellHeight),\
                        QSize(self.cellWidth,i*self.cellHeight))
            self.RectList.append(rect)
            seq+=1
        self.CopyList()
        self.repaint()
    def CopyList(self):
        self.PrvRectList.clear()
        for i in self.RectList:
            self.PrvRectList.append(Rect(i.num,i.rect.topLeft(),i.rect.size()))
    def __myresize(self, a0: QtGui.QResizeEvent):
        if self.RectList == []:
            return
        print("start resize")
        max = 0
        for i in self.RectList:
            if i.num > max:
                max = i.num
        center = self.rect().center()
        size = len(self.RectList)
        baseW = int(self.width() / size)
        baseH = int(self.height() / max)
        if baseW >self.cellWidth or baseW>self.constantWidth:
            self.cellWidth = baseW;
        if baseH > self.cellHeight or baseH>self.constantHeight :
            self.cellHeight = baseH
        startX = int(center.x() - self.cellWidth * size / 2)
        if (startX < 0):
            startX = self.leftGap
        self.startPoint = QPoint(startX,self.height()-self.bottomGap)
        seq = 0;
        for i in self.RectList:
            i.rect = QRect(QPoint(self.startPoint.x()+seq*self.cellWidth,self.startPoint.y()-i.num*self.cellHeight),QSize(self.cellWidth,self.cellHeight*i.num));
            seq+=1
        self.CopyList()

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
        qp = QPainter(self)
        qp.begin(self)
        qp.drawRect(self.rect().adjusted(0,0,-2,-1))
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

    def swap(self,i,j):
        temp = QRect(self.RectList[i].rect)
        self.RectList[i].rect  = QRect(QPoint(self.RectList[j].rect.x(),self.RectList[i].rect.y()),self.RectList[i].rect.size())
        self.RectList[j].rect = QRect(QPoint(temp.x(),self.RectList[j].rect.y()),self.RectList[j].rect.size())
        self.RectList[i],self.RectList[j] = self.RectList[j],self.RectList[i]
        self.move +=2
        self.repaint()
    def setValue(self,i,rect:Rect):
        rect = Rect(rect.num,QPoint(self.startPoint.x()+i*self.cellWidth,rect.rect.y()),rect.rect.size())
        self.RectList[i] = rect
        self.move+=1
        self.repaint()
    def ShellSort(self):
        Length = len(self.RectList)
        D =  int(Length/2);
        while D > 0:
            i = 0
            while i < Length:
                tmp = self.RectList[i]
                j = i
                while j >= 1 and self.RectList[j-D].num > tmp.num:
                    self.compare+=1
                    self.setValue(j, self.RectList[j-D])
                    j -= D
                self.setValue(j, tmp)
                i += D
            D //= 2
    def BubbleSort(self):
        for i in range(len(self.RectList)-1,-1,-1):
            for j in range(0,i,1):
                if self.RectList[j].num > self.RectList[j+1].num:
                    self.compare += 1
                    self.swap(j,j+1)
    def SelectSort(self):
        for i in range(0, len(self.RectList)):
            min = i;
            for j in range(i+1, len(self.RectList)):
                if self.RectList[min].num > self.RectList[j].num:
                    self.compare += 1
                    min = j
            if min != i:
                self.swap(min,i)
    def InsertSort(self):
        for i in range(len(self.RectList)):
            position = i;
            rect = self.RectList[i]
            while position>0 and self.RectList[position-1].num > rect.num:
                self.compare += 1
                self.setValue(position,self.RectList[position-1])
                position-=1
            self.setValue(position,rect)

    def Merge(self, L, R, RightEnd):
        tmpData = self.RectList.copy()
        LeftEnd = R - 1
        i = L
        j = R
        k = L
        # import ipdb; ipdb.set_trace()
        while i <= LeftEnd and j <= RightEnd:
            if tmpData[i].num < tmpData[j].num:
                self.compare += 1
                self.setValue(k, tmpData[i])
                i += 1
            else:
                self.compare += 1
                self.setValue(k, tmpData[j])
                j += 1
            k += 1
        while i <= LeftEnd:
            self.setValue(k, tmpData[i])
            k += 1
            i += 1
        while j <= RightEnd:
            self.setValue(k, tmpData[j])
            k += 1
            j += 1

    def Sort(self, L, RightEnd):
        # import ipdb; ipdb.set_trace()
        if RightEnd > L:
            mid = (L + RightEnd) // 2
            self.Sort(L, mid)
            self.Sort( mid + 1, RightEnd)
            self.Merge(L, mid + 1, RightEnd)

    def MergeSort(self):
        Length = len(self.RectList)
        self.Sort( 0, Length-1)

    def QuickSort(self):
        Length = len(self.RectList)
        self.QSort(0,Length-1)
    def QSort(self,Left,Right):
        Cutoff = 10
        if Cutoff <=Right-Left:
            Pivot = self.GetPivot(Left, Right)
            low = Left + 1
            high = Right - 2
            while True:
                while self.RectList[low].num < Pivot:
                    self.compare += 1
                    low += 1
                while self.RectList[high].num > Pivot:
                    self.compare += 1
                    high -= 1
                if low < high:
                    self.swap(low, high)
                    low += 1
                    high -= 1
                else:
                    break
            self.swap(low, Right - 1)
            self.QSort(Left, low - 1)
            self.QSort(low + 1, Right)

        else:
            # 元素太少， 用插入排序
            for p in range(Left, Right + 1):
                tmp = self.RectList[p]
                i = p
                while i >= 1 and self.RectList[i - 1].num > tmp.num:
                    self.compare += 1
                    self.setValue(i, self.RectList[i - 1])
                    i -= 1
                self.setValue(i, tmp)
    def GetPivot(self,Left,Right):
        Mid = (Left + Right) // 2
        if self.RectList[Left].num> self.RectList[Right].num:
            self.compare += 1
            self.swap(Left, Right)
        if self.RectList[Left].num > self.RectList[Mid].num:
            self.compare += 1
            self.swap(Left, Mid)
        if self.RectList[Mid].num > self.RectList[Right].num:
            self.compare += 1
            self.swap(Mid, Right)
        self.swap(Mid, Right - 1)
        return self.RectList[Right - 1].num
    # def HeapSort(self):
    #     last = len(self.RectList)-1;
    #     for i in (self.getLeftChildIndex(last),-1,-1):
    #         self.adjustHeap(i,last)
    #     while last>=0:
    #         self.swap(0,last)
    #         last-=1
    #         self.adjustHeap(0,last)
    # def getParentIndex(self,last):
    #     return (last-1)>>1;
    # def getLeftChildIndex(self,parent):
    #     return (parent<<1)+1;
    # def adjustHeap(self,i,len):
    #     left,right,j=0,0,0
    #     left = self.getLeftChildIndex(i)
    #     while left<=len:
    #         right = left+1;
    #         j = left
    #         if (j<len and self.RectList[left].num <self.RectList[right].num):
    #             j+=1;
    #         if self.RectList[i].num < self.RectList[j].num:
    #             self.swap(i,j)
    #             i=j
    #             left = self.getLeftChildIndex(i)
    #         else:
    #             break

    def HeapSort(arr):
        # 构建最大堆
        arr.build_max_heap()
        # 循环将堆顶元素移到末尾，再重新调整堆
        for i in range(len(arr.RectList) - 1, 0, -1):
            arr.compare += 1
            arr.swap(i,0)
            arr.adjust_max_heap( 0, i)

    # 构建最大堆
    def build_max_heap(arr):
        for i in range(len(arr.RectList) // 2 - 1, -1, -1):
            arr.adjust_max_heap(i, len(arr.RectList))

    # 调整堆
    def adjust_max_heap(arr, i, size):
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        max_idx = i
        if lchild < size and arr.RectList[lchild].num > arr.RectList[max_idx].num:
            arr.compare += 1
            max_idx = lchild
        if rchild < size and arr.RectList[rchild].num > arr.RectList[max_idx].num:
            arr.compare += 1
            max_idx = rchild
        if max_idx != i:
            arr.swap(i,max_idx)
            arr.adjust_max_heap(max_idx, size)
    def BucketSort(self,bucket_size=5):
        max_value = 0
        for i in self.RectList:
            if max_value < i.num:
                self.compare += 1
                max_value = i.num
        min_value = max_value
        for i in self.RectList:
            if min_value > i.num:
                self.compare += 1
                min_value = i.num

        bucket_count = (max_value - min_value) // bucket_size + 1
        buckets = [[] for _ in range(bucket_count)]
        # 将元素放入对应的桶中
        for val in self.RectList:
            buckets[(val.num - min_value) // bucket_size].append(val)
        # 对每个桶进行排序，并将排序后的结果放回原数组中
        index = 0
        for b in buckets:
            b.sort()
            # sorted(b)
            for val in b:
                self.setValue(index,val)
                index += 1
    def radix_sort(self):
        max_value = -1
        for i in self.RectList:
            if i.num > max_value:
                self.compare += 1
                max_value = i.num
        # 计算最大值有多少位数字，以确定需要进行几轮排序
        digit_num = len(str(max_value))
        # 从低位到高位依次进行排序
        for i in range(digit_num):
            buckets = [[] for _ in range(10)]
            # 将元素放入对应的桶中
            for val in  self.RectList:
                digit = (val.num // (10 ** i)) % 10
                buckets[digit].append(val)
            # 将桶中的元素按顺序放入原数组中
            index = 0
            for b in buckets:
                for val in b:
                    self.setValue(index,val)
                    index += 1