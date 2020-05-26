from PyQt5 import QtWidgets
from consoleEvent import ConsoleEvent
import sys
import test_ui

app = QtWidgets.QApplication([])
ui = test_ui.Ui_MainWindow()
window = ConsoleEvent(ui)
window.show()
sys.exit(app.exec_())
