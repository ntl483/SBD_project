import os
import string


class Tape:
    ended: bool
#    dataManager: DataManager
    path: string

    def __init__(self, dm, id: int):
        self.ended = False
        self.dataManager = dm
        self.initFile(id)

    def addToTape(self, vals):
        self.dataManager.writeRecord(vals[0], vals[1], vals[2], self.path)

    def empty(self) -> bool:
        if os.path.getsize(self.path) == 0:
            return True
        return False

    def printContent(self):
        size = os.path.getsize(self.path)
        records = int(size/12)
        values = []
        #for r in range(records):
            #[m, h, t] = self.dataManager.readRecord(r, self.path)
            #values.append(m*h*t)
        #print(values)

    def getNext(self) -> [int, int, int]:
        vals = self.dataManager.readRecord(0, self.path)

    def getNextVal(self) -> int:
        vals = self.dataManager.readRecord(0, self.path)
        return vals[0]*vals[1]*vals[2]

    def popNext(self):
        vals = self.dataManager.readRecord(0, self.path)
        self.dataManager.removeRecord(self.path)
        #self.printContent()
        if os.path.getsize(self.path) == 0 or vals[0]*vals[1]*vals[2] > self.getNextVal():
            self.ended = True
        return vals

    def sorted(self) -> bool:
        pass

    def runEnded(self) -> bool:
        return self.ended

    def beginRun(self):
        self.ended = False

    def initFile(self, id: int):
        self.path = "tapes_" + str(self.dataManager.fileId)
        if not os.path.isdir(self.path):
            os.mkdir(self.path)
        self.path += "/tape_" + str(id) + ".bin"
        if not os.path.isfile(self.path):
            open(self.path, 'x')
