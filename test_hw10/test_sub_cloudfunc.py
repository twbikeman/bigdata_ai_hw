import base64
import requests

def storageSub(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    # queueModel = json.loads("'name':" + pubsub_message") 
    requests.get('https://aibigdata-ntut-107598064.an.r.appspot.com/' + pubsub_message)
    