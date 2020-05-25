import cv2
import time
import pafy
import queue


class HttpSource():
    def __init__(self):
        pass
        
    def startStreaming(self):
        
        timestamp = 0;
        channel = pafy.new('https://youtube.com/watch?v=w4ZCXBeeR5M')
        streamPort = channel.getbest(preftype = 'mp4')

        while True:
            videoSource = cv2.VideoCapture(streamPort.url)
            if videoSource.isOpened():
                ret, frame = videoSource.read()
            if ret == False:
                continue
            cv2.imshow('http', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            frameTime = int(time.time())
            if timestamp != frameTime:
                timestamp = frameTime
        videoSource.release()
        cv2.destroyAllWindows()
        