#testtesttest

from PyQt5 import QtWidgets, QtGui, QtCore
import ConsoleConfig
import importlib


class EventController:
    def __init__(self, ui, viewModel):
        self.ui = ui
        self.viewModel = viewModel
        self.dataProxy = importlib.import_module(ConsoleConfig.dataProxy).DataProxy()    

    def addSite(self):
        siteId = 's' + str(len(self.viewModel['siteComboBox']))
        self.dataProxy.setTarget({'siteId': siteId})
        site = {
            'id': siteId,
            'name': self.ui.siteNameLineEdit.text()
        }
        self.dataProxy.setSite(site)
        self.showView()

    def selectSite(self):
        self.viewModel['selectedSiteIndex'] = self.ui.siteComboBox.currentIndex()
        if self.viewModel['selectedSiteIndex'] != 0:
           self.selectedSiteId = 's' + str(self.ui.siteComboBox.currentIndex() - 1)
           self.showView()
        

    def addVideo(self):
        videoId = 'v' + str(len(self.viewModel['videoComboBox']))
        self.DataProxy.setTarget({'siteId': self.selectedSiteId, 'videoId': videoId})
        video = {
            'id': videoId,
            'name': self.ui.videoNameLineEdit.text()
        }
        self.dataProxy.setVideo(Video)
        self.showView()
        
        
    def showView(self):
        self.ui.siteComboBox.clear()
        self.viewModel['siteComboBox'] = list(map(lambda x: x['name'],self.dataProxy.getSites()))
        self.ui.siteComboBox.addItems(['請選擇'] + self.viewModel['siteComboBox'])
        self.ui.siteComboBox.setCurrentIndex(self.viewModel['selectedSiteIndex'])

        self.showVideoData()




    def showVideoData(self):
        self.ui.videoTableWidget.setItem(1, -1, QtWidgets.QTableWidgetItem(str(self.viewModel['videoData']['videoName'])))
        self.ui.videoTableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem(str(self.viewModel['videoData']['frameCount'])))
        self.ui.videoTableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(str(self.viewModel['videoData']['normalCount'])))
        self.ui.videoTableWidget.setItem(1, 2, QtWidgets.QTableWidgetItem(str(self.viewModel['videoData']['abnormalCount'])))





    #        self.ui.videoComboBox.clear()

    # def showVideoComboBox(self):
    #     if self.viewModel['selectSiteIndex'] != 0:
    #         self.dataProxy.setTarget({'siteId': self.selectedSiteId})
    #         self.veiwModel['videoComboBox'] = list(map(lambda x : x['name'], self.dataProxy.getVideos))
    #         self.ui.videoComboBox.addItemsche
