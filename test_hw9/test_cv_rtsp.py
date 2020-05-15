import cv2

videoSource = cv2.VideoCapture('rtsp://192.168.43.147:5540/ch0')

while True:
    videoSource.set(cv2.CAP_PROP_POS_FRAMES, 0)
    ret, frame = videoSource.read()
    cv2.imshow('camera',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
videoSource.release()
cv2.destroyAllWindows()
