class Car:
    price = 1000000
    horsepower = 0

    def horse_power(self):
        self.horsepower = 100

    def __str__(self):
        return f'Автомобиль {self.__class__.__name__}, стоимостью {self.price}, имеет лошадиных {self.horsepower} сил'


class Nissan(Car):
    price = 1800000

    def horse_power(self):
        self.horsepower = 200


class Kia(Car):
    price = 1400000

    def horse_power(self):
        self.horsepower = 160


car1 = Nissan()
car1.horse_power()
car2 = Kia()
car2.horse_power()
print(car1)
print(car2)
