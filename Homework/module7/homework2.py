file_name = 'something.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line, end='')
print('\n')
print(file.closed)
