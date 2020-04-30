import requests
url = 'https://bikeman-eval-prod.apigee.net/35_tsai'
key = 'I79pFngD170XrUw4dnyCEqEso9ltu0oA'


post_data = {'region': '天堂', 'key':'天使', 'value':9999}

result = requests.post(url = url + '/my/post', headers = {'apikey': key}, data = post_data)
print(result)
