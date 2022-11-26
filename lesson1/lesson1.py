from lesson2.dunders import Human
from lesson4.myexc import ThirdPartyServerException

class Figure:
    pass


class Rectangle:
    width = 0
    height = 0

    def area(self):
        return self.height * self.width


class Square(Rectangle):
    def area(self):
        return self.height ** 2


def func():
    pass


if __name__ == '__main__':
    rect1 = Rectangle()
    rect1.width = 1
    rect1.height = 4
    print("w", rect1.width)
    print("h", rect1.height)
    rect2 = Rectangle()
    rect2.height = 3
    rect2.width = 3
    print("w", rect2.width)
    print("h", rect2.height)
    rect1.something = "something"
    print(rect1.something)
    # print(rect2.something)
    print(rect1.area())
    print(rect2.area())

    sq = Square()
    print("Sq", sq.area())
