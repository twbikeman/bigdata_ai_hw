# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1005, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 30, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 140, 461, 311))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(160, 170, 191, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(180, 240, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(160, 50, 191, 25))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 67, 17))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 110, 191, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 67, 17))
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(540, 120, 371, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableView = QtWidgets.QTableView(self.groupBox_2)
        self.tableView.setGeometry(QtCore.QRect(50, 40, 256, 192))
        self.tableView.setObjectName("tableView")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(540, 50, 91, 17))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1005, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "雲端計票系統"))
        self.label.setText(_translate("MainWindow", "雲端計票系統"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton.setText(_translate("MainWindow", "更新"))
        self.label_2.setText(_translate("MainWindow", "縣市"))
        self.label_3.setText(_translate("MainWindow", "票數"))
        self.label_4.setText(_translate("MainWindow", "參選人"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_5.setText(_translate("MainWindow", "version 1.0"))
