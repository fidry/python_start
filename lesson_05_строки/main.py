# print('yes' > 'no')
# print('yes' ==

# print('A' > 'a')
# print(ord('A'), ord('a'))
# print(65 > 97)

# print('yyyes' > 'yyyOgbujvuhbjbjhbj')
# print('qq' > 'q')
# print(len('q\0'))

# print('abc' < 'ac')
# print('abc' > 'ab')
# print(420 > 5 and '420' > '5')

'''
print('hello\nw\n\n\norld')
print('hello world')
print('hello\tworld')
print('hello\t\t\t\tworld')
print('12\t\t4345')
print('1234\t\t4')

print('Hello')
print("World world")
'''

"""
print('''
Helo 
    world''')
"""

# s4 = 'He\'s a doctor'
# print(s4)

# Имеется коробка со сторонами A x B x C. Определить, войдет ли она в дверь размером M x K
# A = int(input())
# B = int(input())
# C = int(input())
# M = int(input())
# K = int(input())
# if (A < M and B < K or
#         A < M and C < K or
#         B < M and A < K or
#         B < M and C < K or
#         C < M and A < K or
#         C < M and B < K):
#     print('проходит')
# else:
#     print('не проходит')

a = 123

# s1 = 'какая-то строка ' + str(a)
# print(s1)

# s = f'какая-то строка {a}'
# print(s)

# s = 'rtqwerty'
# print(s.index('dsfsdfsd', 1))

# s = 'Hello, world!!'
# s = s.replace(',', '').replace('!', '??')
# print(s)

# s = 'qwerty@mail.ru'
# lst = s.split('@')
# name = lst[0]
# domain = lst[1].split('.')[0]
# print(name, domain)

# print('qWeRty'.lower())
# print('qwerty'.startswith('wer'))
# print('qwerty'.endswith('qwety'))

# lst = ['C', 'home', 'desctop', 'folder']
# print('\\'.join(lst))

# print(ord('a'))
# print(chr(97))

# for i in range(500, 1000):
#     print(i, chr(i))

# print('hello world'.capitalize())
# print('\t\t\t\n\nhello world    '.strip())

# print('hello world'.count('lldsf'))

s = 'agTtcAGtc'
print(
    s.upper().count('gt'.upper())  # 2
)
