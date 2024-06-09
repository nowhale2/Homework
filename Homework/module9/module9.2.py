# Задача 1: Фабрика функций
def create_operation(operation):
    if operation == "div":
        def division(x, y):
            return x / y
        return division
    elif operation == "mul":
        def mul(x, y):
            return x * y
        return mul


my_func_add = create_operation("mul")
print(f'Результат функции : {my_func_add(4, 2)}')


# Задача 2: Лямбда-функции
mult = lambda x: x ** 2
print(mult(2))


def multiply_def(x):
    return x ** 2


print(multiply_def(2))


# Задача 3: Вызываемые объекты
class Rect:
    def __init__(self, width):
        self.width = width

    def __call__(self, height):
        return f'Площадь прямоугольника, со сторонами {self.width} и {height}, равна: {self.width * height}'


repeat_five = Rect(5)
print(repeat_five(3))
