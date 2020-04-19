import firebase_admin

from firebase_admin import firestore
from firebase_admin import credentials

from firebase_admin import storage


cred = credentials.Certificate('aibigdata-274614.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'aibigdata-274614.appspot.com'})

# dataBase = firestore.client().collection('myFirestore')
# for i in dataBase.stream():
#     print(i.id)


bucket = storage.bucket()
blob = bucket.blob('test/test.txt')
blob.upload_from_filename('test.txt')

blob.make_public()

print(blob.public_url)
