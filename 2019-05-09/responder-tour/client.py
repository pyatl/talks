import requests

data = {'stuff': 'things'}
r = requests.post('http://127.0.0.1:5042/incoming', data=data)

print(r.text)

