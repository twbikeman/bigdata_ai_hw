import requests


response = requests.get('https://aibigdata-ntut-107598064.an.r.appspot.com/美國')

print(response.content.decode('utf-8'));
#  .status_code
# .content
# gcloud app deploy

#response.encoding = 'utf-8'
#response.text
