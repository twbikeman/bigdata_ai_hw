import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import firebase_init


class task_storage():
    def __init__(self):
        pass
    def upload(self, queue_model):
        bucket = storage.bucket()
        blob = bucket.blob( '/test/' + str(queue_model['timestamp']))
        blob.upload_from_string(queue_model['image'])
        print(blob.public_url)
        
        
