from PyQt5 import QtWidgets
import requests
import sys

import client_ui
import env_config
import consoleEvent



model = env_config.model


app = QtWidgets.QApplication([])
ui = client_ui.Ui_MainWindow()



window = consoleEvent.localConsoleEvent(ui, model)


window.show()
sys.exit(app.exec_())
