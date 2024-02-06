import csv

path = './test.csv'

row1 = ['name', 'age']
row2 = ['Bob', 17]
row3 = ['John', 71]

# rows = [
#     row1,
#     row2,
#     row3,
# ]

# with open(path, 'w') as f:
#     writer = csv.writer(f, delimiter=',')
#     writer.writerows(rows)

# with open(path) as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

'''
прочитать файл и все числа в нём увеличить на 1
'''

rows = []
with open(path) as f:
    reader = csv.reader(f)
    for row in reader:
        for col in range(len(row)):
            if row[col].isdigit():
                row[col] = int(row[col]) + 1
        rows.append(row)

with open(path, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
