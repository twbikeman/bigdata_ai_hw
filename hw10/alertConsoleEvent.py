from PyQt5 import QtWidgets

from httpSource import HttpSource

import threading

from alertBotController import AlertBotController

class AlertConsoleEvent(QtWidgets.QMainWindow):
    def __init__(self, ui):
        super(AlertConsoleEvent,  self).__init__()
        self.ui = ui
        self.ui.setupUi(self)
        self.constroller = AlertBotController()

        self.ui.setFrameButton.clicked.connect(self.setVideoToStorageEvent)
        self.ui.stopFrameButton.clicked.connect(self.stopVideoEvent)

        self.viewModel = {}
        
    def setVideoToStorageEvent(self):
        self.constroller.handleVideos()
    def stopVideoEvent(self):
        source = HttpSource()
        source.startStreaming()
        # viewModel = self.viewModel
        # viewModel['streaming'] = False
        # print('stop')
        
