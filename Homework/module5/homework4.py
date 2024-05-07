class Building:
    total = 0

    def __init__(self):
        Building.total += 1


while Building.total < 40:
    new_house = Building()
    print(f'Сейчас построено {new_house.total}')
