from PyQt5 import QtWidgets, QtGui, QtCore
import importlib
import ConsoleConfig
import os


class AlertConsoleEvent(QtWidgets.QMainWindow):

    def __init__(self):
        super(AlertConsoleEvent, self).__init__()


        self.viewModel = {
            'siteComboBox': ['請選擇'],
            'videoComboBox': ['請選擇'],
            'alerBotCounts': {'siteCount':0, 'videoCount':0, 'frameCount':0},
            'videoData': {'videoName':'wait', 'frameCount':0, 'normalCount':0, 'abnormalCount':0},
            'selectedSiteIndex': 0,
            'selectedVideoIndex': 0,
        }

        self.cwd = os.getcwd()
        
        self.ui = importlib.import_module(ConsoleConfig.ui).Ui_MainWindow()
        self.ui.setupUi(self)

        self.eventController = importlib.import_module(ConsoleConfig.eventController).EventController(self.ui, self.viewModel)

        self.eventController.showView()

        self.ui.setSiteButton.clicked.connect(self.eventController.addSite)
        self.ui.siteComboBox.activated.connect(self.eventController.selectSite)

        self.ui.videoPathButton.clicked.connect(self.selectVideoFile)

        self.ui.recognitionPathButton.clicked.connect(self.selectRecognitionFile)

        
    def selectVideoFile(self):
        videoFile, filetype = QtWidgets.QFileDialog.getOpenFileName(self,"選取影片",self.cwd,"All Files (*);;Text Files (*.txt)")
        if videoFile == "":
            print('none')
            return
        self.ui.videoPathLabel.setText(videoFile)


    def selectRecognitionFile(self):
        recognitionFile, filetype = QtWidgets.QFileDialog.getOpenFileName(self, 'select file', self.cwd, "All Files (*);;Text files (*.txt)")
        if recognitionFile == '':
            print('none')
            return
        self.ui.recognitionPathLabel.setText(recognitionFile)
