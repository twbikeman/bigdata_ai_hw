# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlertConsoleView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 729)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(100, 130, 481, 171))
        self.groupBox.setTitle("")
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
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(100, 300, 481, 151))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 40, 67, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(30, 70, 67, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(30, 100, 67, 17))
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(100, 30, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(90, 70, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.setFrameButton = QtWidgets.QPushButton(self.groupBox_2)
        self.setFrameButton.setGeometry(QtCore.QRect(230, 70, 89, 25))
        self.setFrameButton.setObjectName("setFrameButton")
        self.videoPathButton = QtWidgets.QPushButton(self.groupBox_2)
        self.videoPathButton.setGeometry(QtCore.QRect(210, 110, 89, 25))
        self.videoPathButton.setObjectName("videoPathButton")
        self.setVideoButton = QtWidgets.QPushButton(self.groupBox_2)
        self.setVideoButton.setGeometry(QtCore.QRect(320, 110, 89, 25))
        self.setVideoButton.setObjectName("setVideoButton")
        self.videoPathLabel = QtWidgets.QLabel(self.groupBox_2)
        self.videoPathLabel.setGeometry(QtCore.QRect(110, 110, 67, 17))
        self.videoPathLabel.setObjectName("videoPathLabel")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(100, 450, 451, 171))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(40, 40, 67, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(40, 70, 67, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(40, 100, 67, 17))
        self.label_12.setObjectName("label_12")
        self.recognitionPathButton = QtWidgets.QPushButton(self.groupBox_3)
        self.recognitionPathButton.setGeometry(QtCore.QRect(200, 30, 89, 25))
        self.recognitionPathButton.setObjectName("recognitionPathButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 30, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 60, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 60, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 120, 89, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.recognitionPathLabel = QtWidgets.QLabel(self.groupBox_3)
        self.recognitionPathLabel.setGeometry(QtCore.QRect(100, 40, 67, 17))
        self.recognitionPathLabel.setObjectName("recognitionPathLabel")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(600, 150, 281, 291))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.videoTableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.videoTableWidget.setGeometry(QtCore.QRect(10, 150, 251, 131))
        self.videoTableWidget.setRowCount(4)
        self.videoTableWidget.setColumnCount(1)
        self.videoTableWidget.setObjectName("videoTableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.videoTableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.videoTableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.videoTableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.videoTableWidget.setItem(3, 0, item)
        self.videoTableWidget.horizontalHeader().setVisible(False)
        self.videoTableWidget.horizontalHeader().setHighlightSections(False)
        self.videoTableWidget.verticalHeader().setVisible(False)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 256, 101))
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 22))
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
        self.label.setText(_translate("MainWindow", "場域"))
        self.setSiteButton.setText(_translate("MainWindow", "新增"))
        self.label_6.setText(_translate("MainWindow", "名稱"))
        self.label_2.setText(_translate("MainWindow", "智能巡邏AlertBot"))
        self.label_3.setText(_translate("MainWindow", "107598064"))
        self.label_4.setText(_translate("MainWindow", "蔡宗哲"))
        self.label_5.setText(_translate("MainWindow", "學生"))
        self.label_7.setText(_translate("MainWindow", "影片"))
        self.label_8.setText(_translate("MainWindow", "名稱"))
        self.label_9.setText(_translate("MainWindow", "路徑"))
        self.setFrameButton.setText(_translate("MainWindow", "新增"))
        self.videoPathButton.setText(_translate("MainWindow", "檔案"))
        self.setVideoButton.setText(_translate("MainWindow", "入庫"))
        self.videoPathLabel.setText(_translate("MainWindow", "none"))
        self.label_10.setText(_translate("MainWindow", "辦識"))
        self.label_11.setText(_translate("MainWindow", "警示"))
        self.label_12.setText(_translate("MainWindow", "統計"))
        self.recognitionPathButton.setText(_translate("MainWindow", "檔案"))
        self.pushButton_2.setText(_translate("MainWindow", "辨識"))
        self.pushButton_3.setText(_translate("MainWindow", "檔案"))
        self.pushButton_4.setText(_translate("MainWindow", "警示"))
        self.pushButton_5.setText(_translate("MainWindow", "報表"))
        self.recognitionPathLabel.setText(_translate("MainWindow", "none"))
        __sortingEnabled = self.videoTableWidget.isSortingEnabled()
        self.videoTableWidget.setSortingEnabled(False)
        item = self.videoTableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "本片"))
        item = self.videoTableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "影像"))
        item = self.videoTableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "正常"))
        item = self.videoTableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "警示"))
        self.videoTableWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "場域"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "影片"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "影像"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

