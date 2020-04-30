from PyQt5 import QtWidgets
import requests
import sys
import client_ui
import env_config


model = {
    'country': None,
    'candiate': None,
    'votes': None
}


app = QtWidgets.QApplication([])
ui = client_ui.Ui_MainWindow()

class ConsoleEvent(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConsoleEvent, self).__init__()
        self.ui = ui
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.send_req)
        self.ui.comboBox.activated.connect(self.show_Region)

    def send_req(self):
        result = requests.get(env_config.url)
        #model[votes] = self.ui.textEdit.text()
        print(model)
        print(result.content)

    def show_Region(self):
        model['country'] = self.ui.comboBox.currentText();
        print(model)


window = ConsoleEvent()
window.ui.comboBox.clear()
for country in env_config.countries:
    window.ui.comboBox.addItem(country)

window.ui.comboBox_2.clear()
for candidate in env_config.candidates:
    window.ui.comboBox_2.addItem(candidate)







window.show()
sys.exit(app.exec_())
