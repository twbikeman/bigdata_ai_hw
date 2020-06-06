from PyQt5 import QtWidgets
import os
from alertBotController import AlertBotController

from showMessageBox import showMessageBox

class AlertConsoleEvent(QtWidgets.QMainWindow):
    def __init__(self, ui):
        super(AlertConsoleEvent,  self).__init__()
        self.ui = ui
        self.ui.setupUi(self)
        self.constroller = AlertBotController()
        self.viewModel = {
            'imagePaths': []
        }
        self.cwd = os.getcwd()

        self.ui.pushButton1.clicked.connect(self.setImagepathEvent)
        self.ui.pushButton2.clicked.connect(self.setImagepathEvent)
        self.ui.pushButton3.clicked.connect(self.setImagepathEvent)
        self.ui.pushButtonStart.clicked.connect(self.test)
       
    def setImagepathEvent(self):
        videoFilename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "select picture", self.cwd, "All Files (*)")
        self.viewModel['imagePaths'].append(videoFilename)
        self.__showViewData()

    def __showViewData(self):
        viewModel = self.viewModel
        self.ui.label1.setText(viewModel['imagePaths'][0])
        if len(viewModel['imagePaths']) > 1:
            self.ui.label2.setText(viewModel['imagePaths'][1])
        if len(viewModel['imagePaths']) > 2:
            self.ui.label3.setText(viewModel['imagePaths'][2])
    def test(self):
        showMessageBox('123')
