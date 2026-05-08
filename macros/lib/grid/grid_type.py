from enum import Enum

from lib.shapes.hexagon import Hexagon
from lib.shapes.shape import Shape
from lib.shapes.square import Square
from lib.shapes.triangle import Triangle


class GridType(Enum):
    HEX = "hex"
    SQUARE = "square"
    TRIANGLE = "triangle"

    def get_shape(self, i: int, j: int, unit_length: int) -> Shape:
        if self == GridType.SQUARE:
            return Square(i*unit_length, j*unit_length, unit_length, 1)
        if self == GridType.HEX:
            return Hexagon(i, j, unit_length/2, side_length_offset=0.5)
        if self == GridType.TRIANGLE:
            return Triangle(i, j, unit_length, side_length_offset=1)
