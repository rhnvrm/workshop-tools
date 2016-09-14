import requests

name = input('name: ')
level = input('level: ')

r = requests.post('http://0.0.0.0:5000/insert', {'name': name, 'level': level})

print(r.text)
