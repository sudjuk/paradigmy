import math
from .figure import Figure
from .color import Color

class Circle(Figure):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)

    def area(self):
        return math.pi * (self.radius ** 2)
