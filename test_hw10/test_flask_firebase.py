from flask import Flask, request

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('aibigdata-ntut-107598064-firebase.json')
firebase_admin.initialize_app(cred)


dataBase = firestore.client()
testDatabase = dataBase.collection('test')




app = Flask(__name__)






@app.route('/<string:name>', methods = ['GET','POST'])
def home(name):
    if name != 'favicon.ico':
        testDatabase.add({'name': name})
    return 'success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

    
    
    
