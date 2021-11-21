from data_producer import DataProducer
from tape_manager import TapeManager


def main():
    dataProducer = DataProducer()
    dataProducer.createRandom(6)
    # a = TapeManager(1)


if __name__ == '__main__':
    main()
