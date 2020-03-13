import PythonStorage

class DataProxy():         
    def __init__(self):
        
        self.__pythonStorage = PythonStorage.PythonStorage

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
            
    

        
    def setSite(self, site):
        self.__pythonStorage[site['id']] = site


if __name__ == '__main__':
    test = DataProxy()
    test.setSite({'id': '200', 'name': 'test'})   
    test.setTarget({'siteid': '200'})
    print(test.getSite())
    
    
    
        
