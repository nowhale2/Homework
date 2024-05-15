from random import randint
from colorama import Fore


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return Fore.RESET + f'Я - {self.name}, сытость {self.fullness}'

    def eat(self):
        if self.house.food >= 10:
            print(Fore.YELLOW + f'{self.name} поел')
            self.fullness += 10
            self.house.food -= 10
        else:
            print(f'{self.name} не  имеет еды')

    def work(self):
        print(Fore.BLUE + f'{self.name} ходил на работу')
        self.house.money += 50
        self.fullness -= 10

    def watch_mtv(self):
        print(Fore.GREEN + f'{self.name} смотрел мтв целый день')
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            print(Fore.RED + f'{self.name} умер...')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_mtv()

    def shopping(self):
        if self.house.money >= 50:
            print(Fore.MAGENTA + f'{self.name} сходил в магазин за едой')
            self.house.money -= 50
            self.house.food += 50
        else:
            print(Fore.RED + f'У {self.name} закончились деньги')

    def go_into_house(self, house):
        self.house = house
        print(Fore.CYAN + f'{self.name} заехал в дом!!!')
        self.fullness -= 10


class House:
    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return Fore.RESET + f'В доме осталось еды{self.food}, денег осталось {self.money}'


citizens = [
    Man(name='Beavis'),
    Man(name='Butthead'),
    Man(name='Kenny')
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_into_house(house=my_sweet_home)

for day in range(1, 366):
    print(f'=============== день {day} ===============')
    for citizen in citizens:
        citizen.act()
    print('--------------- в конце дня ---------------')
    for citizen in citizens:
        print(citizen)
    print(my_sweet_home)
