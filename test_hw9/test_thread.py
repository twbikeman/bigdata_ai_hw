import threading
import time

def thread_job():
    print("threading job is working")
    time.sleep(1)

my_thread = threading.Thread(target = thread_job)
my_thread.start()
my_thread.join()
print("done")
