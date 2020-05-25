
from httpSource import HttpSource


import threading



http = HttpSource()


t1 = threading.Thread(target = http.startStreaming())
t1.start()
t1.join()
print('exit')

# while not _queue.empty():
#     item = _queue.get()
#     image = item[0];
#     filename = item[1];
#     print(filename)
#     cv2.imwrite(str(filename) + '.png', image)
    
