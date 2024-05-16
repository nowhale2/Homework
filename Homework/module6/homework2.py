class Vehicle:

    def __init__(self):
        self.vehicle_type = None


class Car:

    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.price = 1000000

    def horse_powers(self):
        self.horsepower = 150
        return self.horsepower


class Nissan(Vehicle, Car):

    def __init__(self):
        super().__init__()
        self.vehicle_type = 'Passenger car'
        self.price = 2000000

    def horse_powers(self):
        super().horse_powers()
        self.horsepower = 180
        return self.horsepower


nissan_gtr = Nissan()
print(nissan_gtr.vehicle_type)
print(nissan_gtr.price)
print(nissan_gtr.horse_powers())
