from enum import Enum

from lib.shapes.hexagon import Hexagon
from lib.shapes.shape import Shape
from lib.shapes.square import Square

class GridType(Enum):
    HEX = "hex"
    SQUARE = "square"
    
def get_shape(grid_type:GridType, i:int, j:int, unit_length:int)-> Shape:
    if grid_type == GridType.SQUARE:
        return Square(i*unit_length, j*unit_length, unit_length, 1)
    if grid_type == GridType.HEX:
        return Hexagon(i, j, unit_length/2, side_length_offset=0.5)