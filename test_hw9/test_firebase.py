import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


cred = credentials.Certificate('aibigdata-ntut-107598064-firebase.json')
firebase_admin.initialize_app(cred)
dataBase = firestore.client().collection('test')
dataBase_sites = dataBase.document('myfirestore').collection('sites')
sites = []
for document in dataBase_sites.stream():
    site = document.to_dict()
    sites.append(site['id'])
print(sites)



