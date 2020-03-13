from PyQt5 import QtWidgets, QtGui, QtCore
import ConsoleConfig

import importlib


class EventControler:
    def __init__(self, ui, viewModel):
        self.ui = ui
        self.viewModel = viewModel
        self.dataProxy = importlib.import_module(ConsoleConfig.dataProxy).dataProxy()

    def addSite(self):
        siteId = 's' + str(len(self.viewModel['siteComboBox']))
        self.setTarget({'siteId': siteId })
        site = {
            'id' : siteId,
            'name' : self.ui.siteNameLineEdit.text()
        }
        self.dataProxy.setSite(site)
        self.showView()
        
        
    def showView(self):
        self.ui.siteComboBox.clear()
        self.viewModel['siteComboBox'] = list(map(lambda x: x['name'],self.dataProxy.getSites()))
        self.ui.siteComboBox.addItems(['請選擇'] + self.viewModel['siteComboBox'])
        self.ui.siteComboBox.setCurrentIndex(self.viewModel['selectSiteIndex'])
        
        
        
