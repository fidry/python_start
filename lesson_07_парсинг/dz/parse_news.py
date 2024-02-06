import csv
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import FakeUserAgent


csv_path = 'table.csv'
url = 'https://www.benzinga.com/markets'

while True:
    links = []
    rows = [
        ['время', 'заголовок новости', 'текст новости', 'ссылка']
    ]
    with open(csv_path) as f:
        reader = csv.reader(f)
        for row in reader:
            links.append(row[3])
            rows.append(row)

    headers = {
        'user-agent': FakeUserAgent().random
    }
    response = requests.get(url, headers=headers)
    html = BS(response.content, 'html.parser')
    news_lst = html.select('a.newsfeed-card.text-black')
    for i, news in enumerate(news_lst, start=1):
        header = news.select('span div span')[0].text.strip()
        text = news.select('span.post-teaser')[0].text.strip().replace('\n', ' ').replace('\t', '')
        link = news.get('href')

        if link in links:
            continue

        rows.append([
            str(datetime.now()),
            header,
            text,
            link
        ])

    with open(csv_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    time.sleep(30)
