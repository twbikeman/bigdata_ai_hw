import firebase_init
from firebase_init import storage_proxy

_storage_proxy = storage_proxy()

model = {
'image': '123456789'
}

_storage_proxy.upload(model)
