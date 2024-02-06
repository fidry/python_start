import requests

url = 'https://ruprowork.ru/Курск'
url = 'https://ruprowork.ru/%D0%9A%D1%83%D1%80%D1%81%D0%BA/'
response = requests.get(url)

# print(response.status_code)
# print(response.content)
# print(response.text)
# print(type(response.content))
# print(type(response.text))

with open('test.html', 'w') as f:
    f.write(response.text)
