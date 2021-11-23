from data_producer import DataProducer
from tape_manager import TapeManager


def main():
    dataProducer = DataProducer()
    dataProducer.createRandom(3)
    a = TapeManager(4)
    a.readRecord(0)


if __name__ == '__main__':
    main()
