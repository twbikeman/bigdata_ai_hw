from PyQt5 import QtWidgets
import sys
import importlib
import consoleConfig

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ui = importlib.import_module(consoleConfig.ui).Ui_MainWindow()
    window = importlib.import_module(consoleConfig.event).AlertConsoleEvent(ui)
    window.show()
    sys.exit(app.exec_())
