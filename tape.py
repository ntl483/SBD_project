class Tape:
    content: list

    def __init__(self):
        self.content = []

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
        self.content.pop(0)

    def sorted(self) -> bool:
        a = True
        for i in range(1,len(self.content)):
            if self.content[i-1] > self.content[i]:
                a = False
                break
        return a
