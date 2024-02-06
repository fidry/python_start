import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import FakeUserAgent


headers = {
    'user-agent': FakeUserAgent().random
}

source_url = 'https://ruprowork.ru/'
url = source_url + 'Курск'
response = requests.get(url, headers=headers)

html = BS(response.content, 'html.parser')
# получаем список карточек
cards = html.select('.h-list')
for card in cards:
    # внутри карточки получаем описание
    worker = card.select('.descr h3.headline')[0].text
    print(worker)

    # получаем src изображения
    img_src = card.select('img.u-img')[0].get('src')
    print(source_url + img_src)
    response = requests.get(source_url + img_src)
    filename = img_src.split('/')[-1]
    # сохраняем изображение в файл
    with open(filename, 'wb') as f:
        f.write(response.content)
