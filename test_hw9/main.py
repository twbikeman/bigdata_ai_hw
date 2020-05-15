from PyQt5 import QtWidgets
import sys

import controller
import radiobutton
app = QtWidgets.QApplication([])
ui = radiobutton.Ui_MainWindow()

window = controller.Event(ui)
window.show()
sys.exit(app.exec_())
