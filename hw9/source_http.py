import cv2
import pafy

class source_http():
    def __init__(self, url):
        self.url = url
    def record(self):
        channel = pafy.new(self.url)
        streamPort = channel.getbest(preftype = 'mp4')
        videoSource = cv2.VideoCapture(streamPort.url)
        while True:
            ret, frame = videoSource.read()
            cv2.imshow('http', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        videoSource.release()
        cv2.destroyAllWindows()
            
        

        

