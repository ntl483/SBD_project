from data_manager import DataManager
from tape import Tape


class Sorter:
    phases: int

    def __init__(self):
        self.phases = 0

    def sortFile(self, fileId):
        dm = DataManager(fileId)
        t1, t2 = self.createBaseTapes(dm)
        t3 = self.mergeTwoTapes(t1, t2)

        while not t3.sorted():
            t1, t2 = self.splitTape(t3)
            t3 = self.mergeTwoTapes(t1, t2)
        print("sorted file:")
        t3.printContent()
        dm.writeSorted(t3)
        print("phases:", self.phases)

    def createBaseTapes(self, dm: DataManager):
        maxAddress = dm.dataSize()
        addr = 0
        val = 0
        t = [Tape(), Tape()]
        i = 0
        while addr < maxAddress:
            mass, specHeat, tempDiff = dm.readRecord(addr)
            Q = mass * specHeat * tempDiff
            if t[i].empty() or Q > val:
                # dopisz do tej samej tasmy
                t[i].addToTape(Q)
            else:
                # dopisz do drugiej
                i = not i
                t[i].addToTape(Q)
            val = Q
            addr += 1
        print("base:")
        t[0].printContent()
        t[1].printContent()
        return t[0], t[1]


    def mergeTwoTapes(self, t1: Tape, t2: Tape) -> Tape:
        t3 = Tape()
        # merge sort t1 and t2
        while not t1.empty() and not t2.empty():
            while not t1.runEnded() and not t2.runEnded():
                if t1.getNext() < t2.getNext():
                    t3.addToTape(t1.getNext())
                    t1.popNext()
                else:
                    t3.addToTape(t2.getNext())
                    t2.popNext()
            while not t1.runEnded():
                t3.addToTape(t1.getNext())
                t1.popNext()
            while not t2.runEnded():
                t3.addToTape(t2.getNext())
                t2.popNext()
            t1.beginRun()
            t2.beginRun()
        while not t1.empty():
            t3.addToTape(t1.getNext())
            t1.popNext()
        while not t2.empty():
            t3.addToTape(t2.getNext())
            t2.popNext()
        print("merged:")
        t3.printContent()
        self.phases+=1
        return t3

    def splitTape(self, t3) -> (Tape, Tape):
        t = [Tape(), Tape()]
        val = 0
        i = 0
        while not t3.empty():
            Q = t3.getNext()
            if t[i].empty() or Q >= val:
                # dopisz do tej samej tasmy
                t[i].addToTape(Q)
            else:
                # dopisz do drugiej
                i = not i
                t[i].addToTape(Q)
            val = Q
            t3.popNext()
        print("splitting:")
        t[0].printContent()
        t[1].printContent()
        return t[0], t[1]
