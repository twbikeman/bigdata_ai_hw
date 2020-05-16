import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from PyQt5 import QtWidgets
import sys
import test_ui_1





class Event(QtWidgets.QMainWindow):
    def __init__(self,  ui):
        super(Event, self).__init__()
        self.ui = ui
        self.ui.setupUi(self)
        print(sites)
        self.ui.comboBox.addItems(sites)
        self.ui.pushButton.clicked.connect(self.click)
    def click(self):
        print(self.ui.lineEdit.text())
        dataBase_sites.add({'id':self.ui.lineEdit.text()})
        refresh()
        
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(sites)
        print(sites)
        

def refresh():
    sites.clear()
    for document in dataBase_sites.stream():
        site = document.to_dict()       
        sites.append(site['id'])


cred = credentials.Certificate('aibigdata-ntut-107598064-firebase.json')
firebase_admin.initialize_app(cred)
dataBase = firestore.client().collection('test')
dataBase_sites = dataBase.document('myfirestore').collection('sites')
sites = []
refresh()



        
app = QtWidgets.QApplication([])
ui = test_ui_1.Ui_MainWindow()



window = Event(ui)


window.show()
sys.exit(app.exec_())
