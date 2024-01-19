# DRY - don't repeat yourself

# i = 1
#
# print(str(i) + ' hello world!!')  # 1
# i += 1
#
# print(str(i) + ' hello world!!')  # 2
# i += 1
#
# print(str(i) + ' hello world!!')  # 3
# i += 1
#
# print(str(i) + ' hello world!!')  # 4
# i += 1
#
# print(str(i) + ' hello world!!')  # 5
# i += 1  # i = 6

# i = 1
# while i != 6:
#     print(f'{i} hello world!!')
#     i += 1

# answer = int(input('загадайте число: '))
# guess = int(input('попробуйте угадать число: '))
# attempt = 1
#
# while guess != answer:
#     guess = int(input('попробуйте угадать число: '))
#     attempt += 1
#
# print('Поздравляю, вы угадали число с ' + str(attempt) + ' попытки')

# print('hello' + 12)
# print(f'hello {12}')


# i = float(input('введите число: '))
# while i <= 0.3:
#     print(f'{i} hello world!!')
#     i += 0.1

# i = 1
# while i <= 10:
#     if i % 2 == 1:
#         i += 1
#         continue
#     print(f'{i} hello world!!')
#     i += 1
