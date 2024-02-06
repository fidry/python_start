path = './test.txt'

# f = open(path, 'r')
# for line in f:
#     print(line.strip())
# f.close()

# f = open(path, 'w')
# f.write('new line3\n')
# f.write('new line4\n')
# f.close()

# f = open(path)
with open(path) as f:
    print(f.read())
print('lalala')
