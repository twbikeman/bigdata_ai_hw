from PyQt5 import QtWidgets
import sys

import alertbot_ui
from camera import camera
import film_source

class Event(QtWidgets.QMainWindow):
    def __init__(self, ui):
        super(Event, self).__init__()
        self.ui = ui
        self.ui.setupUi(self)

        self.source = object()
        self.ui.pushButton_add_student.clicked.connect(self.__addStudent)
        self.ui.pushButton_add_channel.clicked.connect(self.__addChannel)
        self.ui.pushButton_start.clicked.connect(self.__record)


    def __addStudent(self):
        view_model['student'].append(self.ui.lineEdit_student.text())
        self.ui.comboBox_student.clear()
        self.ui.comboBox_student.addItems(view_model['student'])
    def __addChannel(self):
        view_model['channel'].append(self.ui.lineEdit_channel.text())
        self.ui.comboBox_channel.clear()
        self.ui.comboBox_channel.addItems(view_model['channel'])
        type = ''
        if self.ui.radioButton_camera.isChecked() == True:
            type = 'camera'
        elif self.ui.radioButton_rtsp.isChecked() == True:
            type = 'rtsp'
        elif self.ui.radioButton_http.isChecked() == True:
            type = 'http'
        else:
            type = 'null'
        url = self.ui.lineEdit_source.text()
        view_model['source_type'].append(type)
        view_model['source_url'].append(url)

        if type == 'camera':
            self.source = camera()
        
        print(view_model)
    def __record(self):
        if isinstance(self.source, camera) :
            self.source.record()
        else:
            pass

        
                
view_model = {
    'student':[],
    'channel':[],
    'source_type':[],
    'source_url':[]
}




        

app = QtWidgets.QApplication([])
ui = alertbot_ui.Ui_MainWindow()

window = Event(ui)

window.show()
sys.exit(app.exec_())
