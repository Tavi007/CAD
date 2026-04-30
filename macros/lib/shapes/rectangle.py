from dataclasses import dataclass
from typing import Tuple
from lib.shapes.abstract_polygon import AbstractPolygon

@dataclass
class Rectangle(AbstractPolygon):
    corner_x: int
    corner_y: int
    width: int
    height: int
    side_length_offset: int = 0
    
    def get_vertices(self) -> list[Tuple[int,int]]:
        x = self.corner_x
        y = self.corner_y
        dx = self.width-self.side_length_offset
        dy = self.height-self.side_length_offset

        return [
            (x, y),           # bottom-left
            (x + dx, y),       # bottom-right
            (x + dx, y + dy),   # top-right
            (x, y + dy)        # top-left
        ]