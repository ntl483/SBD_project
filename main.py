from data_producer import DataProducer
from data_manager import DataManager
from sorter import Sorter


def main():
    dataProducer = DataProducer()
    dataProducer.createFromInput()
    s = Sorter()
    s.sortFile(5)


if __name__ == '__main__':
    main()
