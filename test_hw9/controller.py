from PyQt5 import QtWidgets

class Event(QtWidgets.QMainWindow):
    def __init__(self,  ui):
        super(Event, self).__init__()
        self.ui = ui
        self.ui.setupUi(self)
