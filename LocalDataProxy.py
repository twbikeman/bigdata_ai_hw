import PythonStorage

class DataProxy():         
    def __init__(self):
        
        self.__pythonStorage = PythonStorage.PythonStorage
        self.__mapFunction = lambda x: {'id': x['id'], 'name': x['name']}

    def setTarget(self, target):
        self.__target = target
        
    def __getSiteData(self):
        return self.__pythonStorage[self.__target['siteId']]

    def getSite(self):
        site = {}
        for (key, value) in filter(lambda x: x[0] != 'videos', self.__pythonStorage[self.__target['siteId']].items()):
            site[key] = value
        return site
  
    def getSites(self):
        return list(map(self.__mapFunction, list(self.__pythonStorage.values())))

    def setSite(self, site):
        site['videos'] = {}
        self.__pythonStorage[site['id']] = site





    def __getVideoData(self):
        return self.__getSiteData()['videos'][self.__target['videoId']]

    def getVideo(self):
        video = {} 
        for (key, value) in self.__getVideoData().items():
            video[key] = value
        return video
        
    def getVideos(self):
        return list(map(self.__mapFunction, list(self.__getSiteData()['videos'].values())))
    
    def setVideo(self, video):
        site = self.__getSiteData()
        site['videos'][video['id']] = video

        
        
# if __name__ == '__main__':
#     test = DataProxy()
#     test.setSite({'id': '200', 'name': 'test1'})
#     test.setSite({'id': '201', 'name': 'test2'})
#     test.setSite({'id': '202', 'name': 'test3'})
#     test.setTarget({'siteId': '200', 'videoId': 'v01'})
#     video = {'id' : 'v01', 'name' : 'video1' }
#     test.setVideo(video)
#     video = {'id' : 'v02', 'name' : 'video2' }
#     test.setVideo(video)
    
#     print(test.getVideo())
    
    
    
    
    
        
