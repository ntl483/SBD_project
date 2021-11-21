import os.path
import random


# masa, ciepło właściwe oraz różnica temperatur
# masa -> 0.1;1000, dokladnosc do 0.1 kg
# cieplo wlasciwe -> 0.1; 2500 J/kg*K dokladnosc do 0.1
# roznica temperatur -> 0.0; 1000 K dokladnosc do 0.1


class DataProducer:
    pageOccupancy: int
    accesses: int

    def __init__(self):
        pass

    def getNextFileName(self):
        path = 'data'
        if os.path.isdir(path):
            files = os.listdir(path)
            name = 'tape_' + str(len(files) + 1) + '.bin'
        else:
            os.mkdir(path)
            name = 'tape_1.bin'
        path += '/'
        f = open(path + name, 'x')
        retPath = path + name
        return retPath

    def createRandom(self, size) -> int:
        path = self.getNextFileName()
        file = open(path, 'wb')
        self.pageOccupancy = 0
        self.accesses = 0
        for i in range(size):
            mass = random.randint(1, 10000)
            specHeat = random.randint(1, 25000)
            tempDiff = random.randint(1, 10000)
            print(mass, specHeat, tempDiff)
            file.write(mass.to_bytes(4, 'big'))
            file.write(specHeat.to_bytes(4, 'big'))
            file.write(tempDiff.to_bytes(4, 'big'))
            self.access()
        file.close()
        return self.accesses

    def createFromInput(self):
        path = self.getNextFileName()
        file = open(path, 'wb')
        size = input('how many records: ')
        size = int(size)
        self.accesses = 0
        self.pageOccupancy = 0
        for _ in range(size):
            mass = int(input('mass: '))
            specHeat = int(input('specific heat: '))
            tempDiff = int(input('temperature difference: '))
            file.write(mass.to_bytes(4, 'big'))
            file.write(specHeat.to_bytes(4, 'big'))
            file.write(tempDiff.to_bytes(4, 'big'))
            self.access()
        file.close()
        return self.accesses

    def access(self):
        if self.pageOccupancy >= 4000 or self.pageOccupancy == 0:
            # new page -> one access
            self.accesses += 1
            self.pageOccupancy = 1
        else:
            # same page -> 2 acc
            self.pageOccupancy += 3*4
            self.accesses += 2
