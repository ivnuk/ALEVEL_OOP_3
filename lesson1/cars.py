class Vehicle:
    def move(self):
        pass


class Train(Vehicle):
    pass


class Car(Vehicle):
    def angle(self, degree):
        pass

    def move(self):
        """direction + angle"""
