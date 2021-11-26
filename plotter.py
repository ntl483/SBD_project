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
        log = []
        accesses = []
        for i in range(0, len(self.dataPieces)):
            records.append(self.dataPieces[i].records)
            phases.append(self.dataPieces[i].phases)
            log.append(math.log2(records[i]))
            accesses.append(self.dataPieces[i].acc)

        # how many records vs how many phases + log2 records
        plt.plot(records, phases, 'ro')
        plt.plot(records, log, 'bo')
        plt.axis([0, 1.3*max(records), 0, 1.3*max(max(phases), max(log))])
        plt.show()

        # how many disc accesses
        plt.plot(records, accesses, 'ro')
        # plt.plot(records, log, 'bo')
        plt.axis([0, 1.3 * max(records), 0, 1.3 * max(accesses)])
        plt.show()


    def addData(self, dp: DataPiece):
        self.dataPieces.append(dp)
