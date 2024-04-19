def test(*args):
    print(*args)


def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


test(1, 'строка', True)

n = int(input('Введите число >>> '))
print(f'Факториал числа {n} равен: {factorial(n)}')
