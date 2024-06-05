class CustomError(Exception):
    pass


class InvalidDataException(CustomError):
    def __init__(self, message):
        self.message = message


class ProcessingException(CustomError):
    def __init__(self, message):
        self.message = message


def processing(arg):
    if len(arg) < 5:
        raise InvalidDataException(f'Пароль, содержащий {len(arg)} символов, слишком короткий')
    else:
        raise ProcessingException(f'Пароль с {len(arg)} символами подходит')


password = 'zx68xv'

try:
    result = processing(password)
except InvalidDataException as exc:
    print(f'Ошибка: {exc}')
except ProcessingException as exc:
    print(f'Супер! {exc}')
