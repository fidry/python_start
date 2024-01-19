import requests

url = 'https://chainid.network/chains.json'
response = requests.get(url)
data = response.json()

