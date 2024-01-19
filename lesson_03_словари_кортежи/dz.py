"""
1) Есть 2 словаря. Объединить их без помощи функции update

2) Есть словарь с числовыми значениями. Посчитать среднюю по значениям

3) Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.

4) Когда Антон прочитал «Войну и мир», ему стало интересно,
сколько слов и в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы,
которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и
выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра)
в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово  должно выводиться только один раз

5) Получить json словарь с сайта https://chainid.network/chains.json (с помощью requests) и вывести информацию о всех сетях в формате:
"name | первое rpc | есть ли поддержка EIP1559 | название нативной монеты | decimals нативной монеты | chain id | ссылка на експлорер"

6) Пользователь вводит chain_id и нужно вывести coin symbol (название нативной монеты в этой сети). Для получения информации использовать json словарь с сайта https://chainid.network/chains.json (с помощью requests)

"""
import requests

# 1) Есть 2 словаря. Объединить их без помощи функции update
# d1 = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
# }
#
# d2 = {
#     4: 'four',
#     5: 'five',
#     6: 'six',
# }
#
# print(d1)
# print(d2)
# print('-----------------')
# # d1.update(d2)
#
# for key, val in d2.items():
#     d1[key] = val
#
# print(d1)
# print(d2)

# 2) Есть словарь с числовыми значениями. Посчитать среднюю по значениям
# d = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5,
# }
#
# values_summ = 0
# for val in d.values():
#     values_summ += val
# print(values_summ / len(d))
# print(sum(d.values()) / len(d))

# 3) Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
#   чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.

# lst_1 = [1, 2, 3, 5645, 645, 64]
# lst_2 = [4]
# min_len = len(lst_1)
# if len(lst_2) < min_len:
#     min_len = len(lst_2)
# d = {}
# for i in range(min_len):
#     d[lst_1[i]] = lst_2[i]
# print(d)

# for key, val in zip(lst_1, lst_2):
#     d[key] = val
# print(d)

"""
4) которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и
выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра)
в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово  должно выводиться только один раз
"""

# text = '''На краю дороги стоял дуб. Вероятно, в десять раз старше берез, составлявших лес, он был в десять раз толще, и в два раза выше каждой березы. Это был огромный, в два обхвата дуб, с обломанными, давно, видно, суками и с обломанной корой, заросшей старыми болячками. С огромными своими неуклюже, несимметрично растопыренными корявыми руками и пальцами, он старым, сердитым и презрительным уродом стоял между улыбающимися березами. Только он один не хотел подчиняться обаянию весны и не хотел видеть ни весны, ни солнца.'''
# text = (
#     text.lower()
# )
# # words_lst = text.split()
# words_lst = []
# word = ''
# for ch in text:
#     if ch == '.' or ch == ',' or ch == '?' or ch == '!':
#         continue
#     if ch == ' ':
#         words_lst.append(word)
#         word = ''
#         continue
#     word += ch
#
# print(words_lst)
#
# words_dict = {}
# for word in words_lst:
#     if word not in words_dict:
#         words_dict[word] = 1
#     else:
#         words_dict[word] += 1
#
# words_dict = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))
# for word, amount in words_dict.items():
#     print(word, amount)

# 5) Получить json словарь с сайта https://chainid.network/chains.json
# (с помощью requests) и вывести информацию о всех сетях в формате:
# "| ссылка на експлорер"

# url = 'https://chainid.network/chains.json'
# response = requests.get(url)
# data = response.json()
# for info_dict in data:
#     rpc = None
#     if len(info_dict['rpc']):
#         rpc = info_dict['rpc'][0]
#
#     eip_1559 = False
#     if 'features' in info_dict and len(info_dict['features']):
#         for elem in info_dict['features']:
#             if elem['name'] == 'EIP1559':
#                 eip_1559 = True
#                 break
#
#     explorer = None
#     if 'explorers' in info_dict and len(info_dict['explorers']):
#         explorer = info_dict['explorers'][0]['url']
#
#     print(f"{info_dict['name']} |\t"
#           f"{rpc} |\t"
#           f"eip-1559: {eip_1559} |\t"
#           f"{info_dict['nativeCurrency']['symbol']} |\t"
#           f"decimals: {info_dict['nativeCurrency']['decimals']} |\t"
#           f"chain_id: {info_dict['chainId']} |\t"
#           f"explorer: {explorer}"
#           )

# 6) Пользователь вводит chain_id и нужно вывести coin symbol (название нативной монеты в этой сети).
# Для получения информации использовать json словарь с сайта https://chainid.network/chains.json
# (с помощью requests)

url = 'https://chainid.network/chains.json'
response = requests.get(url)
data = response.json()
chain_id = int(input('введите chain id: '))
for info_dict in data:
    if info_dict['chainId'] == chain_id:
        print(info_dict['nativeCurrency']['symbol'])
        break
