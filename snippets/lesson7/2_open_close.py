"""
2. Принцип відкритості/закритості.
Класи мають бути відкриті до розширення, але закриті для змін.
"""
import math
from typing import List


class Figure:
    def calculate_area(self):
        raise NotImplementedError


class Rectangle(Figure):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.width * self.height


class Square(Figure):
    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width ** 2


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * math.pi


class Triangle(Figure):
    def __init__(self, a_side, b_side, c_side):
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    @property
    def perimeter(self):
        return (self.a_side + self.b_side + self.c_side) / 2

    def calculate_area(self):
        return math.sqrt(
            self.perimeter * (self.perimeter - self.a_side) *
            (self.perimeter - self.b_side) *
            (self.perimeter - self.c_side))


class FigureManager:
    @staticmethod
    def get_min_area(figures: List[Figure]):
        return min(*[x.calculate_area() for x in figures])
