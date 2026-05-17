from enum import Enum
from math import sqrt

from lib.shapes.circle import Circle
from lib.shapes.hexagon import Hexagon
from lib.shapes.rectangle import Rectangle
from lib.shapes.shape import Shape
from lib.shapes.square import Square
from lib.shapes.triangle import Triangle


class ShapeType(Enum):
    HEXAGON_POINTY = "hexagon_pointy"
    HEXAGON_FLAT = "hexagon_flat"
    SQUARE = "square"
    RECTANGLE = "rectangle"
    TRIANGLE = "triangle"
    CIRCLE = "circle"

    def get_board_shape(self, width: float, height: float):
        if self == ShapeType.HEXAGON_POINTY:
            side_length = min(width, height)/2
            return Hexagon(0, 0, side_length)
        if self == ShapeType.HEXAGON_FLAT:
            side_length = min(width, height)/2
            return Hexagon(0, 0, side_length, False)
        if self == ShapeType.SQUARE:
            side_length = min(width, height)
            return Square(-side_length/2, -side_length/2, side_length)
        if self == ShapeType.RECTANGLE:
            return Rectangle(-width/2, -height/2, width, height)
        if self == ShapeType.TRIANGLE:
            side_length = min(width, height*2/sqrt(3))
            return Triangle(0, 0, side_length)
        if self == ShapeType.CIRCLE:
            radius = min(width, height)/2
            return Circle(0, 0, radius)
