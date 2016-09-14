import requests

name = input('name: ')
level = input('level: ')

r = requests.post('http://10.6.11.53:5000/insert', {'name': name, 'level': level})

print(r.text)
