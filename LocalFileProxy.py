import importlib
import LocalProxyConfig
import cv2
import os
import time

class FileProxy():
    def __init__(self):
        self.__storageBucket = LocalProxyConfig.StorageBucket
        if not os.path.exists(self.__storageBucket):
            os.mkdir(self.__storageBucket)
    def storeVideo(self, target):
        dir = target['siteId']
        if not os.path.exists(self.__storageBucket + '/' + dir):
            os.mkdir(self.__storageBucket + '/' + dir)
        dir = target['siteId'] + '/' + target['videoId']
        if not os.path.exists(self.__storageBucket + '/' + dir):
            os.mkdir(self.__storageBucket + '/' + dir)
        videoCapture = cv2.VideoCapture(target['videoFile'])
        fps = videoCapture.get(cv2.CAP_PROP_FPS)

        siteId = target['siteId']
        videoId = target['videoId']
        timestamp = 0
        frames = []

        print('cutting the film ...')
        
        while True:
            ret, frame = videoCapture.read()
            if ret != True:
                break;
            print('cut ' + str(timestamp + 1) + ' image')
            filename = str(timestamp) + '.png'
            cv2.imwrite(self.__storageBucket + '/' + dir + '/' + filename, frame)
            videoCapture.set(1, (timestamp + 1) * fps)
            frame = {
                'id': videoId,
                'frameUrl': self.__storageBucket + '/' + dir + '/' + filename,
                'timestamp': int(time.time())
            }
            print(frame['timestamp'])
            frames.append(frame)
            timestamp += 1
        videoCapture.release()
        return frames
            
            

if __name__ == '__main__':
    fileProxy_test = FileProxy()
    target = {'siteId': 's01', 'videoId': 'v01', 'videoFile': '0_貴重儀器實驗室.mp4'}
    fileProxy_test.storeVideo(target)
    
    
    
    
