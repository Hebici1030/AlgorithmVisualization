import concurrent.futures
import math
import re
import threading
from copy import copy
from typing import List

from PyQt5.QtCore import QThread, pyqtSignal, QObject


class Sign(QObject):
    plotSign = pyqtSignal()
class CoreNotation:
    priority:int = 0
    def __init__(self,Notation,priority):
        self.priority = priority
        self.notation :str= Notation
    def __eq__(self, other):
        return self.priority == other.priority and self.notation == other.notation

    def compare(self,notaion):
        return self.priority - notaion.priority;
class ExponentNotation(CoreNotation):
    def __init__(self,Notation:str,Priority:int,ExpNumber=1,MultNumber = 1):
        super(ExponentNotation, self).__init__(Notation,Priority)
        self.MultNumber = MultNumber
        self.ExpNumber = ExpNumber
        self.Notation = Notation
class LogNotation(CoreNotation):
    def __init__(self,Notation:str,Priority:int,MultNumber=1,Loga=2):
        super(LogNotation, self).__init__(Notation,Priority)
        self.MultNumber = MultNumber
        self.loga = Loga
    def competition(self):
        return math.log(int(1000/self.MultNumber),self.loga)

class NLogNotation(CoreNotation):
    def __init__(self, Notation: str, Priority: int, MultNumber=1, Loga=2):
        super(NLogNotation, self).__init__(Notation, Priority)
        self.MultNumber = 1
        self.loga = Loga
class ConstantNotation(CoreNotation):
    def __init__(self, Number):
        super(ConstantNotation, self).__init__(Number,1)
        self.MultNumber = 1
        self.Number = Number
class FactorialNotation(CoreNotation):
    def __init__(self,Priority:int):
        super(FactorialNotation, self).__init__("N!",Priority)
        self.MultNumber = 1
        self.Notation = "N!"
class NumberExpNotation(CoreNotation):
    def __init__(self,Notation,Priority:int,DomNumber = 1):
        super(NumberExpNotation, self).__init__(Notation,Priority)
        self.domnumber = DomNumber
        self.MultNumber = 1
        self.Notation = Notation

class Notation:
    def __init__(self):
        self.notations :List[CoreNotation] = []
        self.biggest :CoreNotation = CoreNotation("-",0)
        self.BigO = CoreNotation("-",0)
        self.BigON0 = 0
        self.BigOC0 = 0
        self.ThetaNo = 0
        self.ThetaCo = 0
        self.total = 0
        self.allItem = 0
        self.UpThetaNotations :List[CoreNotation] = []
        self.UpThetaN0 = 0
        self.UpThetaCo = 0
        self.DownThetaNo = 0
        self.DownTehtaC0 = 0
        self.DownThetaNoetations :List[CoreNotation] = []

    def append(self,notation:CoreNotation):
        if isinstance(notation,ConstantNotation):
            self.total+= int(notation.Number)
        if not (isinstance(notation,ConstantNotation) or isinstance(notation,FactorialNotation)):
            self.allItem+=notation.MultNumber
        else:
            self.allItem+=1
        self.SetHighPriority(notation)
        self.notations.append(notation)
    #LogN 和 NLogN应该区分开来
    def SetHighPriority(self,notation):
        if self.biggest.compare(notation) < 0:
            self.biggest = notation
        elif notation.compare(self.biggest) == 0 :
            if isinstance(notation, ExponentNotation):
                if self.biggest.ExpNumber < notation.ExpNumber:
                    self.biggest = notation
            elif isinstance(notation,NumberExpNotation):
                if self.biggest.domnumber < notation.domnumber:
                        self.biggest = notation

    def deltail(self):

        if (isinstance(self.notations[-1],ConstantNotation)):
            self.total-= int(self.notations[-1].Number)
        if  isinstance(self.notations[-1],ConstantNotation) or isinstance(self.notations[-1],FactorialNotation):
            self.allItem -= 1
        else:
            self.allItem-=self.notations[-1].MultNumber
        self.notations.remove(self.notations[-1])
        self.biggest: CoreNotation = CoreNotation("-",0)
        for i in self.notations:
            self.SetHighPriority(i)
    def getAcurateTheta(self):
        if self.biggest.priority == 1 or self.biggest.priority == 0 :
            return
        self.getUpNotation()
        self.getDownNotation()
    def getUpNotation(self):
        self.UpThetaNotations=[]
        for i in self.notations:
            self.UpThetaNotations.append(i)
        if len(self.notations)>1:
            mp = self.biggest.priority
            index = -1
            for i in range(len(self.notations)):
                if self.notations[i].priority == 1:
                    continue
                if self.notations[i].priority < mp:
                    index = i
            if index !=-1:
                self.UpThetaNotations.append(copy(self.notations[i]))
        self.UpThetaCo = 1
        self.UpThetaN0 = 0
    def getDownNotation(self):
        self.DownThetaNoetations=[]
        self.DownThetaNoetations.append(copy(self.biggest))
        if len(self.notations)>1:
            mp = self.biggest.priority
            index = -1
            for i in range(len(self.notations)):
                if self.notations[i].priority == 1:
                    continue
                if self.notations[i].priority < mp:
                    index = i
            if index !=-1:
                self.DownThetaNoetations.append(copy(self.notations[i]))
        self.DownTehtaC0 = 1
        self.DownThetaNo = 0
    def getUpThetaCaculate(self,N):
        res = 0
        for i in self.UpThetaNotations:
            res+=self.caculate(i,N)
        return res
    def getDownThetaCaculate(self,N):
        res = 0
        for i in self.DownThetaNoetations:
            res += self.caculate(i, N)
        return res

    def getTheta(self):
        if (isinstance(self.biggest, ConstantNotation)):
            self.ThetaCo = 1
            self.ThetaNo = self.biggest.Number
            return
        if (isinstance(self.biggest, FactorialNotation)):
            self.ThetaCo = self.biggest.MultNumber
            self.ThetaNo = 0
            return
        if (isinstance(self.biggest, NumberExpNotation)):
            self.ThetaCo = self.biggest.MultNumber
            self.ThetaNo = 0
            return
        if (isinstance(self.biggest, ExponentNotation)):
            self.ThetaCo = self.biggest.MultNumber
            self.ThetaNo = 0
        if (isinstance(self.biggest, LogNotation)):
            self.ThetaCo = self.biggest.MultNumber
            self.ThetaNo = 0
        if (isinstance(self.biggest, NLogNotation)):
            self.ThetaCo = self.biggest.MultNumber
            self.ThetaNo = 0
    def ThetaCaculato(self,N:int):
        res = 0
        for i in self.notations:
            res+=self.caculate(i,N)
        return res
    def caculate(self,notaion:CoreNotation,N:int):
        if isinstance(notaion,ExponentNotation):
            return notaion.MultNumber*math.pow(N,notaion.ExpNumber)
        if isinstance(notaion,LogNotation):
            if(N==0):
                return 0
            return notaion.MultNumber*math.log(N,notaion.loga)
        if isinstance(notaion,NLogNotation):
            if (N == 0):
                return 0
            return N*math.log(N,notaion.loga)
        if isinstance(notaion,ConstantNotation):
            return int(notaion.Number)
        if isinstance(notaion,FactorialNotation):
            return math.factorial(N)
        if isinstance(notaion,NumberExpNotation):
            return math.pow(notaion.domnumber,N)

    def BigOCaculator(self,N):
        tempN = copy(self.biggest)
        tempN.MultNumber = self.BigOC0
        res = tempN.MultNumber*self.caculate(tempN,N)
        return res

    def OmigaCaculator(self,N):
        tempN = copy(self.biggest)
        tempN.MultNumber = 1
        return self.caculate(tempN,N)

    def getBigO(self):
        if(isinstance(self.biggest,ConstantNotation)):
            self.BigOC0 = 1
            self.BigON0 = self.biggest.Number
            return
        if(isinstance(self.biggest,FactorialNotation)):
            self.BigOC0 = self.allItem
            self.BigON0 = self.find_fractorial_input(self.total)
            return
        if(isinstance(self.biggest,NumberExpNotation)):
            self.BigOC0 = self.allItem
            self.BigON0 = self.find_numexp_input(self.total,self.biggest)
            return
        if(isinstance(self.biggest,ExponentNotation)):
            self.BigOC0 = self.allItem
            self.BigON0 = self.find_exp_input(self.total,self.biggest)
        if(isinstance(self.biggest,LogNotation)):
            self.BigOC0 = self.allItem
            self.BigON0 = self.find_log_input(self.total,self.biggest)
        if(isinstance(self.biggest,NLogNotation)):
            self.BigOC0 = self.allItem
            self.BigON0 = self.find_nlogn_input(self.total,self.biggest)
    def find_nlogn_input(self,total:int,nlog:NLogNotation):
        if total==0:
            total=1
        temp = math.pow(self.total,nlog.loga)
        return self.__find_NN(temp)
    def __find_NN(self,target):
        res = 1;
        while math.pow(res,res) < target:
            res+=1
        return res
    def find_log_input(self,total:int,log:LogNotation):
        if total==0:
            total=1
        return math.pow(self.total/log.MultNumber,log.loga)
    def find_exp_input(self,total:int,exp:ExponentNotation):
        if total==0:
            total =1
        return int(math.pow(total/exp.MultNumber,1/exp.ExpNumber))
    def find_numexp_input(self,total:int,exp:NumberExpNotation):
        if total==0:
            total =1
        return int(math.log(total,exp.domnumber))
    def find_fractorial_input(self,num):
        if num ==0:
            num = 1
        if num ==1:
            return num;
        res = 2;
        while math.factorial(res) < num:
            res+=1
        return res

class NotationFactory:
    def __init__(self):
        self.notations = Notation()
        self.gap = 100
        self.PriorityConstant = 1
        self.PriorityLogN = 2
        self.PriorityN = 3
        self.PriorityNLogN = 4
        self.PriorityNK = 5
        self.PriorityKN =6
        self.PriorityFN = 7
    #NlogN 和 LogN的大小该如何确当？
    #对于NK KN 有必要比较优先级
    #对于需要多项式数字符串，采用,mult=Number的方式
    #N^12,m=5
    def addSingleNotation(self,notation:str):
        if not re.search("N",notation):
            self.notations.append(ConstantNotation(notation))
        elif notation == "NLogN":
            self.notations.append(NLogNotation(notation,self.PriorityNLogN))
        elif re.search("Log",notation):
            log,mult = notation.split(",")
            multNumber = int(mult[2:])
            self.notations.append(LogNotation(log,self.PriorityLogN,MultNumber=multNumber))
        elif re.search("N\^",notation):
            nk,mult =  notation.split(",")
            multNumber = int(mult[2:])
            expnnumber = int(nk[2:])
            if(multNumber<0):
                return
            if(multNumber==0):
                self.notations.append(ConstantNotation(1))
                return
            self.notations.append(ExponentNotation(notation,self.PriorityNK,expnnumber,multNumber))
        elif re.search("\^N",notation):
            domnumber = int(notation[:-2])
            if(domnumber==0):
                self.notations.append(ConstantNotation(1))
            if (domnumber == 0):
                return
            self.notations.append(NumberExpNotation(notation,self.PriorityKN,domnumber))
            pass
        elif notation == "N!":
            self.notations.append(FactorialNotation(self.PriorityFN))
class ArrayMonitorArray(QThread):
    def __init__(self,array,size,callback):
        super(ArrayMonitorArray, self).__init__()
        self.array = array
        self.size = size
        self.call = callback
    def run(self):
        while True:
            if len(self.array) != self.size:
                self.call()
                self.size = len(self.array)
class Data:
    def __init__(self):
        self.ax=[]
        self.ay=[]
        self.Oax = []
        self.Oay=[]
        self.OmAx=[]
        self.OmAy=[]
        self.OmUpAx=[]
        self.OmDownAx=[]
        self.OmUpAy = []
        self.OmDownAy = []
    def clear(self):
        self.ax = []
        self.ay = []
        self.Oax = []
        self.Oay = []
        self.OmAx = []
        self.OmAy = []
        self.OmDownAx = []
        self.OmUpAx = []
        self.OmUpAy = []
        self.OmDownAy = []
class ASign(QObject):
    sign = pyqtSignal()
class LineCaculator(QObject):
    def __init__(self,factory:NotationFactory,size:int,data:Data,XLim,sign):
        super(LineCaculator, self).__init__()
        self.factory = factory
        self.size = size
        self.data = data
        self.Xlim = XLim
        self.sign = sign
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        self.asign = ASign()
        self.asign.sign.connect(self.submit)
    def submit(self):
        self.executor.submit(self.caculate)
    def caculate(self):
        self.data.clear()
        for i in range(0, self.Xlim, int(self.Xlim /100)):
            self.data.ax.append(i)
            self.data.Oax.append(i)
            self.data.OmAx.append(i)
            self.data.OmUpAx.append(i)
            self.data.OmDownAx.append(i)
            self.data.ay.append(self.factory.notations.ThetaCaculato(i))
            self.data.Oay.append(self.factory.notations.BigOCaculator(i))
            self.data.OmAy.append(self.factory.notations.OmigaCaculator(i))
            self.data.OmDownAy.append(self.factory.notations.getDownThetaCaculate(i))
            self.data.OmUpAy.append(self.factory.notations.getUpThetaCaculate(i))
        self.size = len(self.factory.notations.notations)
        self.sign.plotSign.emit()

class CaculatorMonitor(threading.Thread):
    def __init__(self,factory:NotationFactory,size:int,data:Data,XLim,Gap,sign:Sign):
        super(CaculatorMonitor, self).__init__()
        self.factory = factory
        self.size = size
        self.data = data
        self.Xlim = XLim
        self.Gap = Gap
        self.sign = sign
    def run(self):
        while True:
            if len(self.factory.notations.notations) != self.size :
                self.data.clear()
                for i in range(0,self.Xlim,int(self.Xlim/self.Gap)):
                    self.data.ax.append(i)
                    self.data.Oax.append(i)
                    self.data.OmAx.append(i)
                    self.data.ay.append(self.factory.notations.ThetaCaculato(i))
                    self.data.Oay.append(self.factory.notations.BigOCaculator(i))
                    self.data.OmAy.append(self.factory.notations.OmigaCaculator(i))
                self.size = len(self.factory.notations.notations)
                self.sign.plotSign.emit()





