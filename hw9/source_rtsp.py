import cv2

class source_rtsp():
    def __init__(self, url):
        self.url = url
    def record(self):
        videoSource = cv2.VideoCapture(self.url)
        
        while True:
            videoSource.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = videoSource.read()
            cv2.imshow('rtsp', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        videoSource.release()
        cv2.destroyAllWindows()
            
