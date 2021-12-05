import math

from data_piece import DataPiece
import matplotlib.pyplot as plt


class Plotter:
    dataPieces: list

    def __init__(self):
        self.dataPieces = []

    def plot(self):
        records = []
        phases = []
        phasesT = []
        accesses = []
        accessesT = []
        for i in range(0, len(self.dataPieces)):
            records.append(self.dataPieces[i].records)
            phases.append(self.dataPieces[i].phases)
            phasesT.append(math.ceil(math.log2(self.dataPieces[i].initialRuns)))
            accesses.append(self.dataPieces[i].acc)
            accessesT.append(4 * phasesT[i] * self.dataPieces[i].initialRuns)

        print(phases)
        print(phasesT)
        print(accesses)
        print(accessesT)
        # how many records vs how many phases are and should be
        plt.plot(records, phases, 'ro')
        plt.plot(records, phasesT, 'bo')
        plt.axis([0, 1.3 * max(records), 0, 1.3 * max(max(phases), max(phasesT))])
        #plt.show()

        # how many disc accesses vs how many should be
        plt.plot(records, accesses, 'ro')
        plt.plot(records, accessesT, 'bo')
        plt.axis([0, 1.3 * max(records), 0, 1.3 * max(max(phases), max(accessesT))])
        #plt.show()

    def addData(self, dp: DataPiece):
        self.dataPieces.append(dp)
