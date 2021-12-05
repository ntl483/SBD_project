from data_producer import DataProducer
from sorter import Sorter
from plotter import Plotter


def main():

    dataProducer = DataProducer()
    plotter = Plotter()
    #dataProducer.createRandom(10)
    #dataProducer.createRandom(50)
    #dataProducer.createRandom(100)
    #dataProducer.createRandom(200)
    #dataProducer.createRandom(400)
    #dataProducer.createFromInput()
    s = Sorter(plotter)
    #s.sortFile(1)
    #s.sortFile(2)
    #s.sortFile(3)
    #s.sortFile(4)
    s.sortFile(7)
    #s.sortFile(6)
    #s.sortFile(7)
    #s.sortFile(8)
    #s.sortFile(9)
    #s.sortFile(10)
    plotter.plot()

if __name__ == '__main__':
    main()
