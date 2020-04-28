import requests

post_data = {'region': '地獄', 'key':'死亡天使', 'value':55100}

result = requests.post(url = 'http://127.0.0.1:5000/my/post', data = post_data)
print(result.text)
