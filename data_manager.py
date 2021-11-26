# odczyt blokowy
# sorter: czytanie pojedynczego rekordu
# sorter: wpisanie pojedynczego rekordu
# data manager odczytuje blok 4kB
import os.path
import string
from tape import Tape
from data_piece import DataPiece


class DataManager:
    filePath: string
    blockSize: int
    fileId: int
    dataPiece: DataPiece

    def __init__(self, fileId, dataPiece: DataPiece):
        self.fileId = fileId
        self.blockSize = 4000
        try:
            path = 'data/data_' + str(fileId) + '.bin'
            if os.path.isfile(path):
                self.filePath = 'data/data_' + str(fileId) + '.bin'
                self.dataPiece = dataPiece
                size = os.path.getsize(self.filePath)
                self.dataPiece.setRecords(size / 12)
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
        self.dataPiece.addAcc(1)
        file.close()
        return block

    def writeBlock(self, mass, specHeat, tempDiff):
        self.readBlock(os.path.getsize(self.filePath)/4000)
        file = open(self.filePath, 'wb')
        file.write(mass.to_bytes(4, 'big'))
        file.write(specHeat.to_bytes(4, 'big'))
        file.write(tempDiff.to_bytes(4, 'big'))
        self.dataPiece.addAcc(1)
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
            self.dataPiece.addAcc(1)
            file.close()
        else:
            self.writeBlock(mass, specHeat, tempDiff)

    def dataSize(self) -> int:
        size = os.path.getsize(self.filePath)   # size in bytes
        size /= 12
        return size

    def writeSorted(self, t: Tape):
        path = "data/sorted_"+str(self.fileId)+".bin"
        open(path, 'x')
        file = open(path, 'wb')
        while not t.empty():
            file.write(t.getNext().to_bytes(4, 'big'))
            t.popNext()
        file.close()
