d1 = {
    'first': 1,
    'two': 2,
}

d2 = {
    1: [1, 2, 3],
    342.54: 2,
    'four': 'rrr',
}

# print(d2)
# print(d2[1])
# print(d2[342.54])
# print(d2['four'])
# print(d2['english_words']['dog'])
# print()
# print(d2['english_words']['list'][0])
# print(d2['english_words']['list'][1])

# print(d2)
# d2[1] = 555
# print(d2)
# # del d2[1]
# # print(d2)
#
# if 1 in d2:
#     print('удалили ключ 1')
#     del d2[1]
# else:
#     print('ключа 1 в словаре нет')
# print(d2)
# d2 = {}
# print(d2)

# print(d1)
# print(d2)
# d1.update(d2)
# print()
# print(d1)
# print(d2)

d = {
    'a': 10,
    'b': 2,
    'c': 6,
}
print(d)

# for key in d:
#     print(key, d[key])

# for key in d.keys():
#     print(key, d[key])

# for val in d.values():
#     print(val)

# for item in d.items():
#     print(item)

# my_list = [1, 2, 3]
# my_list[0] = 999
# my_tuple = 1, [4, 65], 'sdjfhb', True, (89, 'dsf'), 8
# if 'sdjfhb' in my_tuple:
#     print('lalalla')

# print(len(my_tuple))

# print(my_tuple)
# print(my_tuple[0])
# # my_tuple[0] = 999

# a, b, c, d = my_list
# print(a, b)

# a = 1
# b = 2
# print(a, b)  # 1 2
# # c = a
# # a = b
# # b = c
# a, b = b, a
# print(a, b)  # 2 1

# print('lalala' + 'lololo')
# print([1, 2, 3] + [4, 5, 6])
# print((1, 2, 3) + (4, 5, 6))
#
# print([1] * 3)
# print((1, ) * 3)

my_tuple = 1, [4, 65], 'sdjfhb', True, (89, 'dsf'), 8
# for i in my_tuple:
#     print(i)

# i = 0
# while i < len(my_tuple):
#     print(my_tuple[i])
#     i += 1

d = {1: 'one', 2: 'two'}
for key, val in d.items():
    print(key, val)
