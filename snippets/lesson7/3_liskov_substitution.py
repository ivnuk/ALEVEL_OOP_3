"""
3. Принцип підстановки Лісков

Якщо об’єкт базового класу замінити об’єктом його похідного класу, то програма має продовжувати працювати коректно.
"""


class Vehicle:
    def accelerate(self):
        pass

    def slow_down(self):
        pass


class FreeDirectionalVehicle(Vehicle):
    def turn(self, angle):
        pass


class BidirectionalVehicle(Vehicle):
    pass


class Car(FreeDirectionalVehicle):
    pass


class Bus(FreeDirectionalVehicle):
    pass


class Train(BidirectionalVehicle):
    def turn(self, angle):
        """
        ????
        """


class Logger:
    def log(self, message):
        raise NotImplementedError


class ConsoleLogger(Logger):
    def log(self, message):
        print(message)


class FileLogger(Logger):
    def __init__(self, file_path):
        self.file_path = file_path

    def log(self, message):
        with open(self.file_path, 'a+') as fp:
            fp.write(message)


class DBLogger(Logger):
    def __init__(self, db_url):
        self.db_url = db_url

    def _connect(self):
        pass

    def _close_connection(self):
        pass

    def log(self, message):
        self._connect()
        # logging here
        self._close_connection()


def main(logger):
    # some code
    logger.log('qweqweqwe')
    # some other code


if __name__ == '__main__':
    logger_ = ConsoleLogger()
    main(logger_)
