# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alertBotUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(647, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(260, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(160, 70, 371, 17))
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 70, 67, 17))
        self.label.setObjectName("label")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(540, 70, 89, 25))
        self.pushButton1.setObjectName("pushButton1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(160, 120, 361, 17))
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 120, 67, 17))
        self.label_4.setObjectName("label_4")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(540, 120, 89, 25))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(540, 170, 89, 25))
        self.pushButton3.setObjectName("pushButton3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 170, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(160, 170, 361, 17))
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 230, 67, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 270, 67, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(80, 310, 121, 17))
        self.label_9.setObjectName("label_9")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(260, 310, 89, 25))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 230, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 270, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(290, 230, 67, 17))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(290, 270, 67, 17))
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "智能巡邏"))
        self.label_11.setText(_translate("MainWindow", "警示通報"))
        self.label.setText(_translate("MainWindow", "影像1："))
        self.pushButton1.setText(_translate("MainWindow", "路徑"))
        self.label_4.setText(_translate("MainWindow", "影像1："))
        self.pushButton2.setText(_translate("MainWindow", "路徑"))
        self.pushButton3.setText(_translate("MainWindow", "路徑"))
        self.label_5.setText(_translate("MainWindow", "影像1："))
        self.label_7.setText(_translate("MainWindow", "閥值："))
        self.label_8.setText(_translate("MainWindow", "差異："))
        self.label_9.setText(_translate("MainWindow", "alertbotflow："))
        self.pushButtonStart.setText(_translate("MainWindow", "啟動"))
        self.label_10.setText(_translate("MainWindow", "人"))
        self.label_12.setText(_translate("MainWindow", "人"))
