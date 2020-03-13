import PythonStorage

class DataProxy():         
    def __init__(self):
        
        self.__pythonStorage = PythonStorage.PythonStorage
        self.__mapFunction = lambda x: {'id': x['id'], 'name': x['name']}

    def setTarget(self, target):
        self.__target = target
        
    def getSite(self):
        site = {}
        try:
            for (key, value) in self.__pythonStorage[self.__target['siteid']].items():
                site[key] = value
            return site
        except:
            return {}
    def getSites(self):
        return list(map(self.__mapFunction, list(self.__pythonStorage.values())))
            
    def setSite(self, site):
        self.__pythonStorage[site['id']] = site


# if __name__ == '__main__':
#     test = DataProxy()
#     test.setSite({'id': '200', 'name': 'test1'})
#     test.setSite({'id': '201', 'name': 'test2'})
#     test.setSite({'id': '202', 'name': 'test3'})
#     test.setTarget({'siteid': '200'})
#     print(test.getSite())
#     print(test.getSites())
    
    
    
    
        
