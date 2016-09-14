import requests


r = requests.get('http://0.0.0.0:5000/display')

print(r.text)
