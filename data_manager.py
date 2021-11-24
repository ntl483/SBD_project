# odczyt blokowy
# sorter: czytanie pojedynczego rekordu
# sorter: wpisanie pojedynczego rekordu
# data manager odczytuje blok 4kB
import os.path
import string


class DataManager:
    filePath: string
    blockSize: int
    discOps: int

    def __init__(self, fileId):
        self.blockSize = 4000
        self.discOps = 0
        try:
            path = 'data/data_' + str(fileId) + '.bin'
            if os.path.isfile(path):
                self.filePath = 'data/data_' + str(fileId) + '.bin'
            else:
                raise ValueError('file doesnt exist')
        except ValueError as exp:
            print(exp)

    def readBlock(self, address):
        # address is which byte to read
        # sector is which block it is
        sector = int(address / 4000)
        file = open(self.filePath, 'rb')
        file.seek(int(sector*4000))
        block = file.read(4000)     # read 4 000 bytes = 4kB        TODO what if file is shorter
        self.discOps += 1
        file.close()
        return block

    def writeBlock(self, mass, specHeat, tempDiff):
        self.readBlock(os.path.getsize(self.filePath)/4000)
        file = open(self.filePath, 'wb')
        file.write(mass.to_bytes(4, 'big'))
        file.write(specHeat.to_bytes(4, 'big'))
        file.write(tempDiff.to_bytes(4, 'big'))
        self.discOps += 1
        file.close()

    def readRecord(self, address):
        # address is which record to start from
        address *= 12
        block = self.readBlock(address)                     # TODO what if block is in memory already
        address %= 4000
        mass = int.from_bytes(block[address:address+4], "big")
        address += 4
        specHeat = int.from_bytes(block[address:address+4], "big")
        address += 4
        tempDiff = int.from_bytes(block[address:address+4], "big")
        return mass, specHeat, tempDiff

    def writeRecord(self, mass, specHeat, tempDiff):
        size = os.path.getsize(self.filePath)  # size is in bytes
        if size % 4000 == 0:
            # full page - make a new one
            file = open(self.filePath, 'wb')
            file.write(mass.to_bytes(4, 'big'))
            file.write(specHeat.to_bytes(4, 'big'))
            file.write(tempDiff.to_bytes(4, 'big'))
            self.discOps += 1
            file.close()
        else:
            self.writeBlock(mass, specHeat, tempDiff)

    def dataSize(self) -> int:
        size = os.path.getsize(self.filePath)   # size in bytes
        size /= 12
        return size
