import os.path
import random

# masa, ciepło właściwe oraz różnica temperatur
# masa -> 0.1;1000, dokladnosc do 0.1 kg
# cieplo wlasciwe -> 0.1; 2500 J/kg*K dokladnosc do 0.1
# roznica temperatur -> 0.0; 1000 K dokladnosc do 0.1

class DataProducer:

    def __init__(self):
        pass

    def getNextFileName(self):
        path = 'data'
        if os.path.isdir(path):
            files = os.listdir(path)
            name = 'data_' + str(len(files) + 1) + '.txt'
        else:
            os.mkdir(path)
            name = 'data_1.txt'
        path += '/'
        f = open(path+name, 'x')
        retPath = path+name
        return retPath

    def createRandom(self, size):
        path = self.getNextFileName()
        file = open(path, 'w')
        for i in range(size):
            mass = random.randint(1, 10000)
            mass /= 10
            specHeat = random.randint(1, 25000)
            specHeat /= 10
            tempDiff = random.randint(1, 10000)
            tempDiff /= 10
            toWrite = str(mass)+"/"+str(specHeat)+"/"+str(tempDiff)+"\n"
            file.write(toWrite)
        file.close()

    def createFromInput(self):
        path = self.getNextFileName()
        file = open(path, 'w')
        size = input('how many records: ')
        size = int(size)
        for _ in range(size):
            mass = float(input('mass: '))
            specHeat = float(input('specific heat: '))
            tempDiff = float(input('temperature difference: '))
            toWrite = str(mass) + "/" + str(specHeat) + "/" + str(tempDiff) + "\n"
            file.write(toWrite)
        file.close()


