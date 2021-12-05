from data_manager import DataManager
from tape import Tape
from data_piece import DataPiece
from plotter import Plotter


class Sorter:
    plotter: Plotter
    phases: int
    accesses: int

    def __init__(self, plotter: Plotter):
        self.phases = 0
        self.accesses = 0
        self.plotter = plotter

    def sortFile(self, fileId):
        self.phases = 0
        dp = DataPiece()
        dm = DataManager(fileId, dp)
        dm.deleteTapes()
        t1, t2 = self.createBaseTapes(dm)
        t1.printContent()
        t2.printContent()
        t3 = self.mergeTwoTapes(t1, t2, dm)
        t1.printContent()
        t2.printContent()
        t3.printContent()
        t1, t2 = self.splitTape(t3, dm)
        t1.printContent()
        t2.printContent()
        t3.printContent()
        while not t1.empty() and not t2.empty():
            t3 = self.mergeTwoTapes(t1, t2, dm)
            t1, t2 = self.splitTape(t3, dm)
        print("sorted file:")
        if not t1.empty():
            t1.printContent()
        else:
            t2.printContent()
        # dm.writeSorted(t3)
        dp.addPh(self.phases)
        dp.addAcc(self.accesses)
        self.plotter.addData(dp)

    def createBaseTapes(self, dm: DataManager):
        val = 0
        t = [Tape(dm, 1), Tape(dm, 2)]
        i = 0
        record = 0
        while not dm.finishedReadFile(record):
            mass, specHeat, tempDiff = dm.readRecord(record)
            Q = mass * specHeat * tempDiff
            if t[i].empty() or Q > val:
                # dopisz do tej samej tasmy
                t[i].addToTape([mass, specHeat, tempDiff])
            else:
                # dopisz do drugiej
                i = not i
                t[i].addToTape([mass, specHeat, tempDiff])
                dm.dataPiece.addInitialRun(1)
            val = Q
            record += 1
        # print("base:")
        # t[0].printContent()
        # t[1].printContent()
        return t[0], t[1]

    def mergeTwoTapes(self, t1: Tape, t2: Tape, dm: DataManager) -> Tape:
        t3 = Tape(dm, 3)
        # merge sort t1 and t2
        while not t1.empty() and not t2.empty():
            while not t1.runEnded() and not t2.runEnded():
                if t1.getNextVal() < t2.getNextVal():
                    t3.addToTape(t1.popNext())
                else:
                    t3.addToTape(t2.popNext())
            while not t1.runEnded():
                t3.addToTape(t1.popNext())
            while not t2.runEnded():
                t3.addToTape(t2.popNext())
            t1.beginRun()
            t2.beginRun()
        while not t1.empty():
            t3.addToTape(t1.popNext())
        while not t2.empty():
            t3.addToTape(t2.popNext())
        #print("merged:")
        #t3.printContent()
        self.phases += 1
        return t3

    def splitTape(self, t3, dm: DataManager) -> (Tape, Tape):
        t = [Tape(dm, 1), Tape(dm, 2)]
        val = 0
        i = 0
        while not t3.empty():
            Q = t3.getNextVal()
            if t[i].empty() or Q >= val:
                # dopisz do tej samej tasmy
                t[i].addToTape(t3.popNext())
            else:
                # dopisz do drugiej
                i = not i
                t[i].addToTape(t3.popNext())
            val = Q
        #print("splitting:")
        #t[0].printContent()
        #t[1].printContent()
        return t[0], t[1]
