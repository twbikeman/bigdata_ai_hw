import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate('aibigdata-ntut-107598064-firebase.json')
firebase_admin.initialize_app(cred, {'storageBucket':'aibigdata-ntut-107598064.appspot.com'})

bucket = storage.bucket()
blob = bucket.blob('test/test.py')
blob.upload_from_filename('test_cv.py')
blob.make_public()