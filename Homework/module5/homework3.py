class Building:

    def __init__(self):
        self.numberOfFloors = 1
        self.buildingType = '1'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


House1 = Building()
House2 = Building()
if House1.__eq__(House2):
    print('Они похожи')
