class Tape:
    content: list
    ended: bool

    def __init__(self):
        self.content = []
        self.ended = False

    def addToTape(self, val):
        self.content.append(val)

    def empty(self) -> bool:
        if len(self.content) == 0:
            return True
        return False

    def printContent(self):
        print(self.content)

    def getNext(self) -> int:
        return self.content[0]

    def popNext(self):
        if len(self.content) == 1 or self.content[0] > self.content[1]:
            self.ended = True
            #print("run ended")
        #print("popped:", self.content[0])
        self.content.pop(0)

    def sorted(self) -> bool:
        a = True
        for i in range(1, len(self.content)):
            if self.content[i-1] > self.content[i]:
                a = False
                break
        return a

    def runEnded(self) -> bool:
        return self.ended

    def beginRun(self):
        self.ended = False
