from data_producer import DataProducer
from sorter import Sorter
import sys


def main():

    dataProducer = DataProducer()
    # dataProducer.createRandom(1000)
    dataProducer.createRandom(100)
    dataProducer.createRandom(500)
    dataProducer.createRandom(900)
    dataProducer.createRandom(1300)
    s = Sorter()
    s.sortFile(1)
    s.sortFile(2)
    s.sortFile(3)
    s.sortFile(4)
    #s.sortFile(5)
    #s.sortFile(6)
    #s.sortFile(7)
    #s.sortFile(8)
    #s.sortFile(9)
    #s.sortFile(10)

if __name__ == '__main__':
    main()
