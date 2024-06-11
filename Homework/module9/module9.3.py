class EvenNumber:

    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            self.start += 2
            if self.start % 2 == 0:
                return self.start - 2
            else:
                self.start += 1
                return self.start -2


en = EvenNumber(10, 25)
for i in en:
    print(i)
