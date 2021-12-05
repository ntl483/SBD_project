
class DataPiece:
    phases: int
    time: int
    acc: int
    records: int
    initialRuns: int

    def __init__(self):
        self.phases = 0
        self.time = 0
        self.acc = 0
        self.records = 0
        self.initialRuns = 0

    def addAcc(self, val):
        self.acc += val

    def addPh(self, val):
        self.phases += val

    def setRecords(self, val):
        self.records = val

    def addInitialRun(self, val):
        self.initialRuns += val
