# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlertConsoleView.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(170, 260, 401, 171))
        self.groupBox.setObjectName("groupBox")
        self.siteComboBox = QtWidgets.QComboBox(self.groupBox)
        self.siteComboBox.setGeometry(QtCore.QRect(130, 30, 86, 25))
        self.siteComboBox.setObjectName("siteComboBox")
        self.siteNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.siteNameLineEdit.setGeometry(QtCore.QRect(130, 70, 113, 25))
        self.siteNameLineEdit.setObjectName("siteNameLineEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 20, 67, 41))
        self.label.setObjectName("label")
        self.setSiteButton = QtWidgets.QPushButton(self.groupBox)
        self.setSiteButton.setGeometry(QtCore.QRect(250, 70, 89, 25))
        self.setSiteButton.setObjectName("setSiteButton")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(50, 70, 67, 17))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(206, 100, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 100, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 100, 67, 17))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "場域"))
        self.setSiteButton.setText(_translate("MainWindow", "新增"))
        self.label_6.setText(_translate("MainWindow", "名稱"))
        self.label_2.setText(_translate("MainWindow", "智能巡邏AlertBot"))
        self.label_3.setText(_translate("MainWindow", "107598064"))
        self.label_4.setText(_translate("MainWindow", "蔡宗哲"))
        self.label_5.setText(_translate("MainWindow", "學生"))
