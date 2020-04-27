import requests

response = requests.get('https://aibigdata-ntut-107598064.an.r.appspot.com/美國/100')

print(response.content);
#  .status_code
# .content
# gcloud app deploy

#response.encoding = 'utf-8'
#response.text
