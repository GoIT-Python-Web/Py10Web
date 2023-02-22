from math import pi
from enum import Enum


class ShapeType(str, Enum):
    CIRCLE = "circle"
    SQUARE = "square"


class Square:
    def __init__(self, side):
        self.side = side

    def area_of(self):
        return self.side ** 2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_of(self):
        return self.radius ** 2 * pi


class FacadeShape:
    def __init__(self, size):
        self.square = Square(size)
        self.circle = Circle(size)

    def area_of(self, type_figure: ShapeType):
        figure = {
            ShapeType.CIRCLE: self.circle.area_of(),
            ShapeType.SQUARE: self.square.area_of()
        }
        return figure.get(type_figure, None)


if __name__ == '__main__':
    shape = FacadeShape(42)
    print(shape.area_of(ShapeType.CIRCLE))
    print(shape.area_of(ShapeType.SQUARE))
