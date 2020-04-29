import requests
# url = 'https://bikeman-eval-prod.apigee.net/35_tsai'
# key = 'I79pFngD170XrUw4dnyCEqEso9ltu0oA'
# result = requests.get(url = url, headers = {'apikey': key})
# print(result.text)

result = requests.post('http://127.0.0.1/')
print(result.text)
