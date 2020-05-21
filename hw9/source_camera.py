import cv2
import time

from task_storage import task_storage

class source_camera():
    def __init__(self):
        self.flowModel = {'image':None, 'timestamp':None }
    def record(self):
        videoSource = cv2.VideoCapture(0)
        while True:
            videoSource.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = videoSource.read()
            cv2.imshow('camera', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            self.flowModel['image'] = cv2.imencode('.jpg', frame)[1].tostring()
            self.flowModel['timestamp'] = int(time.time())
            print(self.flowModel['timestamp'])
            storage = task_storage()
            storage.upload(self.flowModel)
            time.sleep(1)
        videoSource.release()
        cv2.destroyAllWindows()