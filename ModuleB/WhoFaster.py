# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WhoFaster.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from ModuleB.CustomObject import CustomTreeItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 798)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1180, 736))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Inventory = CustomTreeItem(self.scrollAreaWidgetContents)
        self.Inventory.setMaximumSize(QtCore.QSize(300, 16777215))
        self.Inventory.setAnimated(True)
        self.Inventory.setAllColumnsShowFocus(False)
        self.Inventory.setObjectName("Inventory")
        self.Inventory.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.Inventory.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        item_0 = QtWidgets.QTreeWidgetItem(self.Inventory)
        item_0 = QtWidgets.QTreeWidgetItem(self.Inventory)
        self.horizontalLayout_5.addWidget(self.Inventory)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setMinimumSize(QtCore.QSize(0, 400))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.VisualLayout = QtWidgets.QVBoxLayout()
        self.VisualLayout.setSpacing(0)
        self.VisualLayout.setObjectName("VisualLayout")
        self.horizontalLayout_7.addLayout(self.VisualLayout)
        self.verticalLayout.addWidget(self.widget)
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(200, 250))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.algWidget = QtWidgets.QWidget(self.tab_3)
        self.algWidget.setObjectName("algWidget")
        self.AlgTask = QtWidgets.QLabel(self.algWidget)
        self.AlgTask.setGeometry(QtCore.QRect(30, 50, 91, 111))
        self.AlgTask.setObjectName("AlgTask")
        self.task_2 = QtWidgets.QLabel(self.algWidget)
        self.task_2.setGeometry(QtCore.QRect(250, 50, 91, 111))
        self.task_2.setObjectName("task_2")
        self.horizontalLayout_4.addWidget(self.algWidget)
        self.line_2 = QtWidgets.QFrame(self.tab_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.ComWidget = QtWidgets.QWidget(self.tab_3)
        self.ComWidget.setObjectName("ComWidget")
        self.ComCPU = QtWidgets.QLabel(self.ComWidget)
        self.ComCPU.setGeometry(QtCore.QRect(250, 50, 91, 111))
        self.ComCPU.setObjectName("ComCPU")
        self.ComTask = QtWidgets.QLabel(self.ComWidget)
        self.ComTask.setGeometry(QtCore.QRect(30, 50, 91, 111))
        self.ComTask.setObjectName("ComTask")
        self.horizontalLayout_4.addWidget(self.ComWidget)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edit_Computer = QtWidgets.QWidget(self.tab_4)
        self.edit_Computer.setObjectName("edit_Computer")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.edit_Computer)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.cpu_pic = QtWidgets.QLabel(self.edit_Computer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpu_pic.sizePolicy().hasHeightForWidth())
        self.cpu_pic.setSizePolicy(sizePolicy)
        self.cpu_pic.setMinimumSize(QtCore.QSize(200, 200))
        self.cpu_pic.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.cpu_pic.setText("")
        self.cpu_pic.setObjectName("cpu_pic")
        self.horizontalLayout_8.addWidget(self.cpu_pic)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.iconBox = QtWidgets.QComboBox(self.edit_Computer)
        self.iconBox.setObjectName("iconBox")
        self.gridLayout.addWidget(self.iconBox, 2, 1, 1, 1)
        self.del_cpu = QtWidgets.QPushButton(self.edit_Computer)
        self.del_cpu.setObjectName("del_cpu")
        self.gridLayout.addWidget(self.del_cpu, 2, 2, 1, 1)
        self.name_edit = QtWidgets.QLineEdit(self.edit_Computer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_edit.sizePolicy().hasHeightForWidth())
        self.name_edit.setSizePolicy(sizePolicy)
        self.name_edit.setObjectName("name_edit")
        self.gridLayout.addWidget(self.name_edit, 0, 1, 1, 1)
        self.ipx_edit = QtWidgets.QLineEdit(self.edit_Computer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ipx_edit.sizePolicy().hasHeightForWidth())
        self.ipx_edit.setSizePolicy(sizePolicy)
        self.ipx_edit.setObjectName("ipx_edit")
        self.gridLayout.addWidget(self.ipx_edit, 1, 1, 1, 1)
        self.add_cpu = QtWidgets.QPushButton(self.edit_Computer)
        self.add_cpu.setObjectName("add_cpu")
        self.gridLayout.addWidget(self.add_cpu, 1, 2, 1, 1)
        self.icone = QtWidgets.QLabel(self.edit_Computer)
        self.icone.setAlignment(QtCore.Qt.AlignCenter)
        self.icone.setObjectName("icone")
        self.gridLayout.addWidget(self.icone, 2, 0, 1, 1)
        self.ipx = QtWidgets.QLabel(self.edit_Computer)
        self.ipx.setObjectName("ipx")
        self.gridLayout.addWidget(self.ipx, 1, 0, 1, 1)
        self.name = QtWidgets.QLabel(self.edit_Computer)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)
        self.horizontalLayout_8.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3.addWidget(self.edit_Computer)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TaskTitle = QtWidgets.QLabel(self.widget_2)
        self.TaskTitle.setObjectName("TaskTitle")
        self.gridLayout_2.addWidget(self.TaskTitle, 0, 0, 1, 1)
        self.TimeComplex = QtWidgets.QLabel(self.widget_2)
        self.TimeComplex.setObjectName("TimeComplex")
        self.gridLayout_2.addWidget(self.TimeComplex, 3, 0, 1, 1)
        self.In_Size = QtWidgets.QLineEdit(self.widget_2)
        self.In_Size.setObjectName("In_Size")
        self.gridLayout_2.addWidget(self.In_Size, 1, 1, 1, 1)
        self.InputSize = QtWidgets.QLabel(self.widget_2)
        self.InputSize.setObjectName("InputSize")
        self.gridLayout_2.addWidget(self.InputSize, 1, 0, 1, 1)
        self.Desc = QtWidgets.QLabel(self.widget_2)
        self.Desc.setObjectName("Desc")
        self.gridLayout_2.addWidget(self.Desc, 2, 0, 1, 1)
        self.In_Complex = QtWidgets.QLineEdit(self.widget_2)
        self.In_Complex.setObjectName("In_Complex")
        self.gridLayout_2.addWidget(self.In_Complex, 3, 1, 1, 1)
        self.In_title = QtWidgets.QLineEdit(self.widget_2)
        self.In_title.setObjectName("In_title")
        self.gridLayout_2.addWidget(self.In_title, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 2, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.add_task_btn = QtWidgets.QPushButton(self.widget_2)
        self.add_task_btn.setObjectName("add_task_btn")
        self.horizontalLayout_2.addWidget(self.add_task_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.del_task_btn = QtWidgets.QPushButton(self.widget_2)
        self.del_task_btn.setObjectName("del_task_btn")
        self.horizontalLayout_2.addWidget(self.del_task_btn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11.addWidget(self.widget_2)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Inventory.setSortingEnabled(True)
        self.Inventory.headerItem().setText(0, _translate("MainWindow", "类型"))
        self.Inventory.headerItem().setText(1, _translate("MainWindow", "性能/任务"))
        __sortingEnabled = self.Inventory.isSortingEnabled()
        self.Inventory.setSortingEnabled(False)
        self.Inventory.topLevelItem(0).setText(0, _translate("MainWindow", "任务"))
        self.Inventory.topLevelItem(1).setText(0, _translate("MainWindow", "电脑"))
        self.Inventory.setSortingEnabled(__sortingEnabled)
        self.AlgTask.setText(_translate("MainWindow", "a"))
        self.task_2.setText(_translate("MainWindow", "a"))
        self.ComCPU.setText(_translate("MainWindow", "a"))
        self.ComTask.setText(_translate("MainWindow", "a"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "操作台"))
        self.del_cpu.setText(_translate("MainWindow", "删除"))
        self.add_cpu.setText(_translate("MainWindow", "添加"))
        self.icone.setText(_translate("MainWindow", "ICON"))
        self.ipx.setText(_translate("MainWindow", "IPX"))
        self.name.setText(_translate("MainWindow", "名称"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "添加电脑组件"))
        self.TaskTitle.setText(_translate("MainWindow", "Task主题"))
        self.TimeComplex.setText(_translate("MainWindow", "时间复杂度"))
        self.InputSize.setText(_translate("MainWindow", "输入规模"))
        self.Desc.setText(_translate("MainWindow", "描述"))
        self.add_task_btn.setText(_translate("MainWindow", "添加"))
        self.del_task_btn.setText(_translate("MainWindow", "删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "添加计算型任务"))
        self.menu.setTitle(_translate("MainWindow", "工具栏"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())