import cv2
import time

# print(time.time())

import pafy

channel = pafy.new('https://www.youtube.com/watch?v=XxJKnDLYZz4')
streamPort = channel.getbest(preftype = 'mp4')
videoSource = cv2.VideoCapture(streamPort.url)
# fps = videoSource.get(cv2.CAP_PROP_FPS)
# timestamp = 0
while True:
    ret, frame = videoSource.read()
    if ret != True:
        break
    cv2.imshow('camera',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(1)
  #  videoSource.set(1, (timestamp + 1) * fps)
  #  timestamp += 1
videoSource.release()
cv2.destroyAllWindows()


