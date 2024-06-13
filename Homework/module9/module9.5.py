def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        count = 0
        for d in range(1, res+1):
            if res % d == 0:
                count += 1
        type_ = 'Простое' if count <= 2 else 'Составное'
        print(type_)
        return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
