# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Notation.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TreeNotaion(object):
    def setupUi(self, TreeNotaion):
        TreeNotaion.setObjectName("TreeNotaion")
        TreeNotaion.resize(1080, 855)
        self.centralwidget = QtWidgets.QWidget(TreeNotaion)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1078, 802))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PlotLayout = QtWidgets.QVBoxLayout()
        self.PlotLayout.setObjectName("PlotLayout")
        self.horizontalLayout_2.addLayout(self.PlotLayout)
        self.verticalLayout.addWidget(self.widget)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 300))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 1677215))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.OmigaDispalyer = QtWidgets.QLineEdit(self.widget_3)
        self.OmigaDispalyer.setText("")
        self.OmigaDispalyer.setObjectName("OmigaDispalyer")
        self.gridLayout_3.addWidget(self.OmigaDispalyer, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.BigDispalyer = QtWidgets.QLineEdit(self.widget_3)
        self.BigDispalyer.setText("")
        self.BigDispalyer.setObjectName("BigDispalyer")
        self.gridLayout_3.addWidget(self.BigDispalyer, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.ThetaDispalyer = QtWidgets.QLineEdit(self.widget_3)
        self.ThetaDispalyer.setObjectName("ThetaDispalyer")
        self.gridLayout_3.addWidget(self.ThetaDispalyer, 2, 1, 1, 1)
        self.horizontalLayout_6.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.ConstantEditor = QtWidgets.QLineEdit(self.widget_4)
        self.ConstantEditor.setObjectName("ConstantEditor")
        self.gridLayout.addWidget(self.ConstantEditor, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.XSlider = QtWidgets.QSlider(self.widget_4)
        self.XSlider.setOrientation(QtCore.Qt.Horizontal)
        self.XSlider.setObjectName("XSlider")
        self.horizontalLayout_3.addWidget(self.XSlider)
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)
        self.ExpEditor = QtWidgets.QLineEdit(self.widget_4)
        self.ExpEditor.setObjectName("ExpEditor")
        self.gridLayout.addWidget(self.ExpEditor, 3, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.YSlider = QtWidgets.QSlider(self.widget_4)
        self.YSlider.setOrientation(QtCore.Qt.Horizontal)
        self.YSlider.setObjectName("YSlider")
        self.horizontalLayout_5.addWidget(self.YSlider)
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 1, 1, 1)
        self.MultEditor = QtWidgets.QLineEdit(self.widget_4)
        self.MultEditor.setObjectName("MultEditor")
        self.gridLayout.addWidget(self.MultEditor, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout)
        self.horizontalLayout_6.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.N = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.N.sizePolicy().hasHeightForWidth())
        self.N.setSizePolicy(sizePolicy)
        self.N.setObjectName("N")
        self.gridLayout_2.addWidget(self.N, 0, 0, 1, 1)
        self.LogN = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LogN.sizePolicy().hasHeightForWidth())
        self.LogN.setSizePolicy(sizePolicy)
        self.LogN.setObjectName("LogN")
        self.gridLayout_2.addWidget(self.LogN, 0, 1, 1, 1)
        self.Nlogn = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Nlogn.sizePolicy().hasHeightForWidth())
        self.Nlogn.setSizePolicy(sizePolicy)
        self.Nlogn.setObjectName("Nlogn")
        self.gridLayout_2.addWidget(self.Nlogn, 0, 2, 1, 1)
        self.N2 = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.N2.sizePolicy().hasHeightForWidth())
        self.N2.setSizePolicy(sizePolicy)
        self.N2.setObjectName("N2")
        self.gridLayout_2.addWidget(self.N2, 1, 0, 1, 1)
        self.N3 = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.N3.sizePolicy().hasHeightForWidth())
        self.N3.setSizePolicy(sizePolicy)
        self.N3.setObjectName("N3")
        self.gridLayout_2.addWidget(self.N3, 1, 1, 1, 1)
        self.NK = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NK.sizePolicy().hasHeightForWidth())
        self.NK.setSizePolicy(sizePolicy)
        self.NK.setMinimumSize(QtCore.QSize(94, 0))
        self.NK.setBaseSize(QtCore.QSize(93, 0))
        self.NK.setObjectName("NK")
        self.gridLayout_2.addWidget(self.NK, 1, 2, 1, 1)
        self.KN = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KN.sizePolicy().hasHeightForWidth())
        self.KN.setSizePolicy(sizePolicy)
        self.KN.setMinimumSize(QtCore.QSize(93, 0))
        self.KN.setBaseSize(QtCore.QSize(93, 0))
        self.KN.setObjectName("KN")
        self.gridLayout_2.addWidget(self.KN, 2, 0, 1, 1)
        self.FN = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FN.sizePolicy().hasHeightForWidth())
        self.FN.setSizePolicy(sizePolicy)
        self.FN.setMinimumSize(QtCore.QSize(94, 0))
        self.FN.setBaseSize(QtCore.QSize(93, 0))
        self.FN.setObjectName("FN")
        self.gridLayout_2.addWidget(self.FN, 2, 1, 1, 1)
        self.TwoN = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TwoN.sizePolicy().hasHeightForWidth())
        self.TwoN.setSizePolicy(sizePolicy)
        self.TwoN.setSizeIncrement(QtCore.QSize(1, 0))
        self.TwoN.setObjectName("TwoN")
        self.gridLayout_2.addWidget(self.TwoN, 2, 2, 1, 1)
        self.Add = QtWidgets.QPushButton(self.widget_5)
        self.Add.setObjectName("Add")
        self.gridLayout_2.addWidget(self.Add, 3, 0, 1, 1)
        self.Plus = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Plus.sizePolicy().hasHeightForWidth())
        self.Plus.setSizePolicy(sizePolicy)
        self.Plus.setSizeIncrement(QtCore.QSize(1, 0))
        self.Plus.setObjectName("Plus")
        self.gridLayout_2.addWidget(self.Plus, 3, 1, 1, 1)
        self.remove = QtWidgets.QPushButton(self.widget_5)
        self.remove.setObjectName("remove")
        self.gridLayout_2.addWidget(self.remove, 3, 2, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_2)
        self.horizontalLayout_6.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        TreeNotaion.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TreeNotaion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        TreeNotaion.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TreeNotaion)
        self.statusbar.setObjectName("statusbar")
        TreeNotaion.setStatusBar(self.statusbar)

        self.retranslateUi(TreeNotaion)
        QtCore.QMetaObject.connectSlotsByName(TreeNotaion)

    def retranslateUi(self, TreeNotaion):
        _translate = QtCore.QCoreApplication.translate
        TreeNotaion.setWindowTitle(_translate("TreeNotaion", "MainWindow"))
        self.label.setText(_translate("TreeNotaion", "BigO:"))
        self.label_2.setText(_translate("TreeNotaion", "Omiga:"))
        self.label_3.setText(_translate("TreeNotaion", "Theta:"))
        self.label_8.setText(_translate("TreeNotaion", "Y轴："))
        self.label_7.setText(_translate("TreeNotaion", "X轴："))
        self.label_6.setText(_translate("TreeNotaion", "指数/底数："))
        self.label_5.setText(_translate("TreeNotaion", "多项式常数："))
        self.label_9.setText(_translate("TreeNotaion", "x轴取值范围"))
        self.label_10.setText(_translate("TreeNotaion", "y轴取值范围"))
        self.label_4.setText(_translate("TreeNotaion", "常数数值："))
        self.N.setText(_translate("TreeNotaion", "N"))
        self.LogN.setText(_translate("TreeNotaion", "LogN"))
        self.Nlogn.setText(_translate("TreeNotaion", "NLogN"))
        self.N2.setText(_translate("TreeNotaion", "N^2"))
        self.N3.setText(_translate("TreeNotaion", "N^3"))
        self.NK.setText(_translate("TreeNotaion", "N^K"))
        self.KN.setText(_translate("TreeNotaion", "K^N"))
        self.FN.setText(_translate("TreeNotaion", "N!"))
        self.TwoN.setText(_translate("TreeNotaion", "2^N"))
        self.Add.setText(_translate("TreeNotaion", "添加"))
        self.Plus.setText(_translate("TreeNotaion", "+"))
        self.remove.setText(_translate("TreeNotaion", "回退"))
