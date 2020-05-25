import firebaseInit
from firebase_admin import firestore
import firebaseConfig

class DataProxy:
    def __init__(self):
        self.dataBase = firestore.client()
        self.alertBotDatabase = self.dataBase.collection(firebaseConfig.myDatabase).document(firebaseConfig.alertBotDatabase)
    def setBot(self, dataModel):
        dataModel['id'] = self.alertBotDatabase.collection('bots').add(dataModel)[1].id

