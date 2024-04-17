def test(a, b, c):
    print(a, b, c)


def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


test(1, 'строка', True)

n = int(input('Введите число >>> '))
print(f'Факториал числа {n} равен: {factorial(n)}')
