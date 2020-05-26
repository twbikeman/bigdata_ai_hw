
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from PyQt5.QtGui import QPixmap


class ConsoleEvent(QtWidgets.QMainWindow):
    def __init__(self, ui):
        super(ConsoleEvent, self).__init__()
        self.ui = ui
        self.ui.setupUi(self)
        self.ui.label.setPixmap(QPixmap('Test.png'))
        self.ui.label.setGeometry(50,50,600,600)
        self.ui.tableWidget.setItem(1,1, QTableWidgetItem('123'))
