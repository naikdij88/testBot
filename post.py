import requests

def url_send():
    r = requests.get('https://slbase-567f2.firebaseio.com/second/url.json')
    url = r.json()["hello"]
    return url