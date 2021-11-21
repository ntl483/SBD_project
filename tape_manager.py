# odczyt blokowy
# sorter: czytanie pojedynczego rekordu
# sorter: wpisanie pojedynczego rekordu
# data manager odczytuje blok 4kB
import os.path


class TapeManager:
    fileId: int
    blockSize: int

    def __init__(self, fileId):
        self.blockSize = 4000
        try:
            path = 'data/tape_'+str(fileId)+'.bin'
            if os.path.isfile(path):
                self.fileId = fileId
            else:
                raise ValueError('file doesnt exist')
        except ValueError as exp:
            print(exp)

    def readBlock(self):
        pass

    def writeBlock(self):
        pass

    def readRecord(self):
        pass

    def writeRecord(self):
        pass
