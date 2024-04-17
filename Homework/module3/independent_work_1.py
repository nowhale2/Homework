def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a=1, b=2, c=3)     # имя параметров переопределено
print_params(4, 5)      # параметры a и b переопределены, а параметр с остался значением по умолчанию
print_params('new string')      # переопределён только параметр а, b и c остались без изменений

# print_params(2, 'new string', False, 4)
# функция не сработает, так как передано больше параметров, чем определено

print_params(b = 25)        # 1 25 True
print_params(c = [1,2,3])   # 1 строка [1, 2, 3]

values_list = ['что-нибудь', (1, 2, 3), False]
values_dict = {'a': 14, 'b': False, 'c': 'string'}

print_params(*values_list)      # a = 'что-нибудь', b = (1, 2, 3), c = False
print_params(**values_dict)     # a = 14, b = False, c = 'string'

values_list_2 = [(2, 2, 2), 'string']
print_params(*values_list_2, 42)    # функция исправна
