# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radiobutton_2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.camera_button = QtWidgets.QRadioButton(self.centralwidget)
        self.camera_button.setGeometry(QtCore.QRect(140, 280, 112, 23))
        self.camera_button.setObjectName("camera_button")
        self.rtsp_button = QtWidgets.QRadioButton(self.centralwidget)
        self.rtsp_button.setGeometry(QtCore.QRect(300, 280, 112, 23))
        self.rtsp_button.setObjectName("rtsp_button")
        self.http_button = QtWidgets.QRadioButton(self.centralwidget)
        self.http_button.setGeometry(QtCore.QRect(430, 280, 112, 23))
        self.http_button.setObjectName("http_button")
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
        self.camera_button.setText(_translate("MainWindow", "camera"))
        self.rtsp_button.setText(_translate("MainWindow", "rtsp"))
        self.http_button.setText(_translate("MainWindow", "http"))

