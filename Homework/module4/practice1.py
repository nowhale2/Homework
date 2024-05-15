from nim_engine import get_bunches, put_stones, is_game_over, take_from_bunch


put_stones()
user_number = 1
while True:
    print('Текущая позиция')
    print(get_bunches())
    print(f'Ход игрока {user_number}')
    pos = input('Откуда берём? >>> ')
    qua = input('Сколько берём? >>> ')
    step_success = take_from_bunch(position=int(pos), quantity=int(qua))
    if step_success:
        user_number = 2 if user_number == 1 else 1
    else:
        print('Невозможный ход')
    if is_game_over():
        break
    user_number = 2 if user_number == 1 else 1

print('Выиграл игрок под номером', user_number)
