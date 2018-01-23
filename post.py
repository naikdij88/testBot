import requests

r = requests.get('https://slbase-567f2.firebaseio.com/second/url.json')

print(r.json()["hello"])

url = r.json()["hello"]
#l = requests.post(url, data="hello")
