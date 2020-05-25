import firebase_admin
from firebase_admin import credentials
import firebaseConfig

cred = credentials.Certificate(firebaseConfig.keyFile)
firebase_admin.initialize_app(cred, {'storageBucket': firebaseConfig.storageBucket})
