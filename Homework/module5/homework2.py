# from random import randint


class House:
    def __init__(self):
        self.numberOfFloors = 0

    def set_new_number_of_floors(self, floors):
        self.numberOfFloors = floors
        print('Вы находитесь на этаже под номером', self.numberOfFloors)


# floor = randint(1, 10)
# House2 = House()
# House2.set_new_number_of_floors(floor)
