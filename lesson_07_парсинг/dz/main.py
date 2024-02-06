import os

import requests
from fake_useragent import FakeUserAgent


main_dir = 'images'
main_page_dir = os.path.join(main_dir, 'main_page')
episodes_dir = os.path.join(main_dir, 'episodes')


def download_img(url: str, path: str):
    response_data = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response_data.content)


headers = {
    'authority': 'rickandmortyapi.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://rickandmortyapi.com',
    'referer': 'https://rickandmortyapi.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': FakeUserAgent().random,
}

json_data = {
    'query': '\n    query randomCharacters($ids: [ID!]!) {\n      charactersByIds(ids: $ids) {\n        id\n        name\n        status\n        species\n        image\n        episode {\n          name\n          id\n        }\n        location {\n          name\n          id\n        }\n      }\n    }\n  ',
    'variables': {
        'ids': [
            748,
            793,
            268,
            97,
            345,
            255,
        ],
    },
}

response = requests.post('https://rickandmortyapi.com/graphql', headers=headers, json=json_data)
json_data = response.json().get('data', {}).get('charactersByIds', {})


# задача 1
# for elem in json_data:
#     img_src = elem['image']
#     filename = os.path.join(main_page_dir, img_src.split('/')[-1])
#     response = requests.get(img_src)
#
#     with open(filename, 'wb') as f:
#         f.write(response.content)

# задача 2
'''
Определить в каких эпизодах появлялся персонаж с главной страницы.
Выгрузить все фотографии персонажей из данного эпизода в папку,
которая называется episode_N (N - номер эпизода)
Для создания папок используйте модуль os
'''

episodes_ids = []
# выгружаем все эпизоды с главной страницы
for elem in json_data:
    episodes_lst = elem['episode']
    for episode in episodes_lst:
        episodes_ids.append(episode['id'])
episodes_ids = list(set(episodes_ids))

episode_url = 'https://rickandmortyapi.com/api/episode/'

for episode_id in episodes_ids:
    character_urls = []

    # создание директории
    episodes_temp_dir = os.path.join(episodes_dir, episode_id)
    os.mkdir(episodes_temp_dir)

    response = requests.get(f'{episode_url}{episode_id}')
    json_episode_data = response.json()
    for character_url in json_episode_data['characters']:
        character_urls.append(character_url)

    character_urls = list(set(character_urls))
    for character_url in character_urls:
        # выгрузка картинок
        response = requests.get(character_url)
        print(response.json())
        image_src = response.json()['image']
        filename = os.path.join(episodes_temp_dir, image_src.split('/')[-1])
        download_img(url=image_src, path=filename)
