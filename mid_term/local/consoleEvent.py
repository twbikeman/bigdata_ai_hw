from PyQt5 import QtWidgets
import requests


import env_config



class localConsoleEvent(QtWidgets.QMainWindow):
    def __init__(self, ui, model):
        super(localConsoleEvent, self).__init__()
        self.model = model
        self.url = env_config.url
        self.key = env_config.key
        self.ui = ui
        self.ui.setupUi(self)
        self.ui.update_button.clicked.connect(self.send_req)

        self.ui.country_input.clear()
        for country in env_config.countries:
            self.ui.country_input.addItem(country)
        self.ui.candidate_input.clear()
        for candidate in env_config.candidates:
            self.ui.candidate_input.addItem(candidate)


    def send_req(self):
        self.model['country'] = self.ui.country_input.currentText();
        self.model['candidate'] = self.ui.candidate_input.currentText();
        self.model['votes'] = int(self.ui.votes_input.text())

        print(self.model)

        
        url = self.url + '/president2020/patch'
        result = requests.post(url = url ,headers = {'apikey': self.key},  data = self.model)
        # result = requests.post(url = url + '/president2020_test/patch', headers = {'apikey': key} , data = self.model)


        print(result.content.decode('utf-8'))
