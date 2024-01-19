# wallet_1 = '0xsdiufniuhsdf7667gds7fgsd67fsd'
# wallet_2 = '0xjnby8b7b76sdbf76sdbf7bds7bbsd'
# wallet_3 = '0xuifdngiudfng8df78dfngundfg8uh'

# print(wallet_1)
# print(wallet_2)
# print(wallet_3)

# wallets = [
#     '0xsdiufniuhsdf7667gds7fgsd67fsd',
#     '0xuifdngiudfng8df78dfngundfg8uh',
#     '0xjnby8b7b76sdbf76sdbf7bds7bbsd',
# ]
#
# for wallet in wallets:
#     print(wallet)

# game_x_0 = [
#     [0, 0, 'O'],
#     [0, 'X', 0],
#     [0, 0, 0],
# ]

lst = [88, 'hi', True, 57, 9]
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])
# print(lst[5])
print(lst[-1])
print(lst[-2])

a = 'hello'
print(a[0])

print(lst[0:3])
print(lst[1:3])
print(lst[0:4:2])
print(lst[0:5:2])
print(lst[:5:2])

print('---------------------------')

lst = [12, 5, 76, 123, 8, 98, 3, 65]
print(lst)

print(len(lst))

lst.append(99999)
print(lst)

del lst[0]
print(lst)

x = 65
if x in lst:
    lst.remove(x)
else:
    print(f'Элемента {x} нет в списке')
print(lst)

print(lst.index(98))

lst.pop()
print(lst)

lst.sort()
print(lst)

print('----------------')

lst = [12, 5, 76, 123, 8, 98, 3, 65]

# s = 0
# for i in lst:
#     s += i
#     print(i)
# print(s)

i = 0
s = 0
while i < len(lst):
    s += lst[i]
    print(lst[i])
    i += 1
print(s)
