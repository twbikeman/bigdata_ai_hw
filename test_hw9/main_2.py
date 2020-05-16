from PyQt5 import QtWidgets
import sys
import radiobutton_2

class Event(QtWidgets.QMainWindow):
    def __init__(self,  ui):
        super(Event, self).__init__()
        self.ui = ui
        self.ui.setupUi(self)
        self.ui.http_button.toggled.connect(self.radio_button_test)
    def radio_button_test(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(radio_button.text())
            self.ui.camera_button.setChecked(False)
            self.ui.rtsp_button.setChecked(False)

app = QtWidgets.QApplication([])
ui = radiobutton_2.Ui_MainWindow()



window = Event(ui)


window.show()
sys.exit(app.exec_())
