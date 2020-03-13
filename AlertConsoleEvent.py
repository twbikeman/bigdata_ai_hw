from PyQt5 import QtWidgets, QtGui, QtCore
import importlib
import ConsoleConfig



class AlertConsoleEvent(QtWidgets.QMainWindow):

    def __init__(self):
        super(AlertConsoleEvent, self).__init__()


        self.viewModel = {
            'siteCombbox': ['請選擇'],
        }


        
        self.ui = importlib.import_module(ConsoleConfig.ui).Ui_MainWindow()
        self.ui.setupUi(self)

        self.eventController = importlib.import_module(ConsoleConfig.eventController).eventController(self.ui, self.viewModel)
        
