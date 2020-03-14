from PyQt5 import QtWidgets, QtGui, QtCore
import importlib
import ConsoleConfig



class AlertConsoleEvent(QtWidgets.QMainWindow):

    def __init__(self):
        super(AlertConsoleEvent, self).__init__()


        self.viewModel = {
            'siteComboBox': ['請選擇'],
            'selectedSiteIndex': 0,
            'videoComboBox': ['請選擇'],
            'selectedVideoIndex': 0,
        }


        
        self.ui = importlib.import_module(ConsoleConfig.ui).Ui_MainWindow()
        self.ui.setupUi(self)

        self.eventController = importlib.import_module(ConsoleConfig.eventController).EventController(self.ui, self.viewModel)

        self.eventController.showView()

        self.ui.setSiteButton.clicked.connect(self.eventController.addSite)
        self.ui.siteComboBox.activated.connect(self.eventController.selectSite)
