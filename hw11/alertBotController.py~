import queue
from httpSource import HttpSource
import threading
import time


class AlertBotController():
    def __init__(self):
        self.dataModel = {}
        self.frameQueue = queue.Queue()

    def test(self):
        while True:
            time.sleep(1)
            print('test')

    def handleVideos(self):
        source = HttpSource()
        t1 = threading.Thread(target = self.test, daemon = True)
        t1.start()
        source.startStreaming()
        

        
        



   

