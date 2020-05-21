import base64
import requests

def storageSub(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    queueModel = json.loads(pubsub_message)
    url = ????
    requests.post(url, headers = {'apikey': }, json = queueModel)
    
