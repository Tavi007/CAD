from enum import Enum
from math import sqrt

from lib.shapes.circle import Circle
from lib.shapes.hexagon import Hexagon
from lib.shapes.rectangle import Rectangle
from lib.shapes.shape import Shape
from lib.shapes.square import Square
from lib.shapes.equilateral_triangle import EquilateralTriangle


class ShapeType(Enum):
    HEXAGON_POINTY = "hexagon_pointy"
    HEXAGON_FLAT = "hexagon_flat"
    SQUARE = "square"
    RECTANGLE = "rectangle"
    TRIANGLE = "triangle"
    CIRCLE = "circle"

    def get_board_shape(self, width: float, height: float) -> Shape:
        if self == ShapeType.HEXAGON_POINTY:
            side_length = min(width, height)/2
            return Hexagon((0.0, 0.0), side_length)
        if self == ShapeType.HEXAGON_FLAT:
            side_length = min(width, height)/2
            return Hexagon((0.0, 0.0), side_length, False)
        if self == ShapeType.SQUARE:
            side_length = min(width, height)
            return Square((0.0, 0.0), side_length)
        if self == ShapeType.RECTANGLE:
            return Rectangle((0.0, 0.0), width, height)
        if self == ShapeType.TRIANGLE:
            height = min(width/(3/sqrt(3)/2), height)
            return EquilateralTriangle((0.0, 0.0), height, True)
        if self == ShapeType.CIRCLE:
            radius = min(width, height)/2
            return Circle((0.0, 0.0), radius)


SHAPE_TYPES: list[ShapeType] = [
    ShapeType.HEXAGON_POINTY,
    ShapeType.HEXAGON_FLAT,
    ShapeType.SQUARE,
    ShapeType.RECTANGLE,
    ShapeType.TRIANGLE,
    ShapeType.CIRCLE,
]
