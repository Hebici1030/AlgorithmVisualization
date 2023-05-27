from decimal import Decimal
from typing import List

from PyQt5.QtCore import QThread
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ModuleBase.BaseObject import Meta, TimeTag

class sign(QObject):
    finish = pyqtSignal()
    progress = pyqtSignal(int)
class Work(QThread):
    def __init__(self,meta,XLimt:int):

        super(Work, self).__init__()
        self.metas = meta
        self.X = XLimt
        self.sign = sign()
    def run(self):
        index = 0
        for meta in self.metas:
            self.sign.progress.emit(index)
            meta.listx = []
            meta.listy = []
            for i in range(0, self.X, int(self.X / int(self.X / 2))):
                meta.listx.append(i)
            for i in meta.listx:
                tempNum = Decimal()
                for j in meta.functionStr.split("+"):
                    if (j.startswith("N^")):
                        j += (",k=" + str(j[2:]))
                    if (j.endswith("^N")):
                        j += (",k=" + str(j[0:-2]))
                    tempNum += Decimal(str(TimeTag.calculator(TimeTag(), j, i)))
                meta.listy.append(tempNum)
        self.sign.finish.emit()

