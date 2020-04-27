from PyQt5 import QtWidgets
import sys
import vote
app = QtWidgets.QApplication([])
ui = vote.Ui_MainWindow()

class ConsoleEvent(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConsoleEvent, self).__init__()
        self.ui = ui
        self.ui.setupUi(self)

window = ConsoleEvent()
window.show()
sys.exit(app.exec_())
