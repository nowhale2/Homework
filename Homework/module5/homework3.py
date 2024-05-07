class Building:

    def __init__(self):
        self.numberOfFloors = 1
        self.buildingType = '1'

    def __eq__(self, other):
        return self.numberOfFloors == other.buildingType


House = Building()

if Building.__eq__(self=House, other=House):
    print("Строка успеха")
# Код, написанный на 14 строчке не выполнится,
# так как результат сравнения равен False
