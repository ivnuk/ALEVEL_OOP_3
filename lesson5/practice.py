class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def from_json(cls, data):
        """
        cls(arg, arg2) -> Rectangle(arg, arg2)
        """
        ret_list = [cls(x[0], x[1]) for x in data]
        return ret_list

    def __str__(self):
        return f"Rectangle {self.width}x{self.height}"

    @property
    def perimeter(self):
        return (self.width + self.height) * 2

    @property
    def area(self):
        return self.width * self.height


class Candidate:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


if __name__ == '__main__':
    c1 = Candidate('John', 'Doe')
    print(c1.full_name)
    rect = Rectangle(24.5, 96.8)

    rect_data = [
        (1, 4),
        (4, 7),
        (42, 17),
        (124, 907),
        (2, 2),
    ]

    list_of_rects = [Rectangle(x[0], x[1]) for x in rect_data]

    res = Rectangle.from_json(rect_data)
    print(res)

    print(rect.area)
    print(rect.perimeter)
