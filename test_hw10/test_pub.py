from google.cloud import pubsub_v1
from google.oauth2 import service_account
# aibigdata-ntut-107598064-pubsub.json

credentials = service_account.Credentials.from_service_account_file('aibigdata-ntut-107598064-pubsub.json')

publisher = pubsub_v1.PublisherClient(credentials = credentials)
projectId = 'aibigdata-ntut-107598064'
publisher.publish(publisher.topic_path(projectId,  'test_pub_sub'), data = bytes('蔡', encoding = "utf-8"))

