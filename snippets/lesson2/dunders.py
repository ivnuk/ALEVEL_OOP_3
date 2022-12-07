from datetime import datetime

COMPARE_PROP = 'age'


class Human:
    def __init__(self, name, weight, height, age, sex):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age
        self.sex = sex

    def hello(self):
        print('Hello')

    def __str__(self):
        return f"{self.name}"

    # def __dict__(self):
    #     pass

    # def __repr__(self):
    #     return f"{self.name} {self.age} {self.passport_id}"

    def __del__(self):
        print(self, "removed at", datetime.now())

    def __call__(self, distance, direction):
        return f"{self} moved {distance} meters {direction}."

    # def __add__(self, other):
    #     pass

    def __getattribute__(self, item):
        if item == 'age':
            if self.sex == "f":
                raise AttributeError("This is not a correct question:)")
        return super().__getattribute__(item)

    def __lt__(self, other):
        return getattr(self, COMPARE_PROP) < getattr(other, COMPARE_PROP)

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age


if __name__ == '__main__':
    # Human(**data)

    a = Human("Galya", 55, 175, 25, 'f')
    # c = Human("Galya", 65, 185, 15, 'f')
    b = Human("Edik", 85, 160, 40, 'm')
    # print(a.age)
    # print(b.age)
    print(b(25, "left"))

    # print(a > b)
    print(callable(b.age))
    print(callable(b.__str__))

    some_dict = dict(a=1, b=2)
    print(some_dict.get('c', 50))

    t = 1
    y = 2
    o = t + y
    print(t, y)
