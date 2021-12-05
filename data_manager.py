# odczyt blokowy
# sorter: czytanie pojedynczego rekordu
# sorter: wpisanie pojedynczego rekordu
# data manager odczytuje blok 4kB
import os.path
import shutil
import string

from tape import Tape
from data_piece import DataPiece


class DataManager:
    filePath: string
    blockSize: int
    fileId: int
    dataPiece: DataPiece
    dataSize: int
    fileInMemory: string

    def __init__(self, fileId, dataPiece: DataPiece):
        self.fileInMemory = None
        self.fileId = fileId
        self.blockSize = 4020
        try:
            path = 'data/data_' + str(fileId) + '.bin'
            if os.path.isfile(path):
                self.filePath = 'data/data_' + str(fileId) + '.bin'
                self.dataPiece = dataPiece
                size = os.path.getsize(self.filePath)
                self.dataPiece.setRecords(size / 12)
                self.inMemory = None
                self.dataSize = int(size / 12)
            else:
                raise ValueError('file doesnt exist')
        except ValueError as exp:
            print(exp)

    def readBlock(self, record, path=""):
        if path == "":
            path = self.filePath
        # record is which record to read
        # sector is which block it is
        sector = int(record*12 / self.blockSize)
        file = open(path, 'rb')
        file.seek(int(sector * self.blockSize))
        block = file.read(max(self.blockSize, os.path.getsize(self.filePath)))     # read 4 000 bytes = 4kB
        file.close()
        if self.inMemory == block and self.fileInMemory == path:
            return
        self.dataPiece.addAcc(1)
        self.inMemory = block
        self.fileInMemory = path

    def readRecord(self, record: int, path=""):
        if path == "":
            path = self.filePath
        address = record*12
        if address % self.blockSize == 0 or address == 0 or self.fileInMemory != path:
            self.readBlock(record, path)
        address %= self.blockSize
        mass = int.from_bytes(self.inMemory[address:address+4], "big")
        address += 4
        specHeat = int.from_bytes(self.inMemory[address:address+4], "big")
        address += 4
        tempDiff = int.from_bytes(self.inMemory[address:address+4], "big")
        return mass, specHeat, tempDiff

    def writeRecord(self, mass, specHeat, tempDiff, path=""):
        if path == "":
            path = self.filePath
        size = os.path.getsize(path)  # size is in bytes
        if size % self.blockSize == 0:
            # full pages - make a new one
            file = open(path, 'ab')
            file.write(mass.to_bytes(4, 'big'))
            file.write(specHeat.to_bytes(4, 'big'))
            file.write(tempDiff.to_bytes(4, 'big'))
            self.dataPiece.addAcc(1)
            file.close()
        else:
            self.writeBlock(mass, specHeat, tempDiff, path)

    def writeBlock(self, mass, specHeat, tempDiff, path=""):
        if path == "":
            path = self.filePath
        self.readBlock(os.path.getsize(path)/self.blockSize, path)
        file = open(path, 'ab')
        file.write(mass.to_bytes(4, 'big'))
        file.write(specHeat.to_bytes(4, 'big'))
        file.write(tempDiff.to_bytes(4, 'big'))
        self.dataPiece.addAcc(1)
        file.close()

    def writeSorted(self, t: Tape):
        path = "data/sorted_"+str(self.fileId)+".bin"
        open(path, 'x')
        file = open(path, 'wb')
        while not t.empty():
            file.write(t.getNext().to_bytes(4, 'big'))
            t.popNext()
        file.close()

    def finishedReadFile(self, record: int):
        if record < self.dataSize:
            return False
        return True

    def removeRecord(self, path):
        size = os.path.getsize(path)
        file = open(path, "r+b")
        toDel = file.read(12)
        rest = file.read()
        file.seek(0)
        file.write(rest)
        file.truncate()

    def deleteTapes(self):
        path = "tapes_" + str(self.fileId)
        if os.path.isdir(path):
            shutil.rmtree(path)
