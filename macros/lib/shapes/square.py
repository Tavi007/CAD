from dataclasses import dataclass
from typing import Tuple
from lib.shapes.abstract_polygon import AbstractPolygon


@dataclass
class Square(AbstractPolygon):
    corner_x: int
    corner_y: int
    length: int
    side_length_offset: int = 0

    def get_inner(self, offset_from_border: float) -> "Square":
        return Square(
            self.corner_x + offset_from_border/2,
            self.corner_y + offset_from_border/2,
            self.length - offset_from_border/2,
            0,
        )

    def get_vertices(self) -> list[Tuple[int, int]]:
        x = self.corner_x
        y = self.corner_y
        h = self.length-self.side_length_offset

        return [
            (x, y),           # bottom-left
            (x + h, y),       # bottom-right
            (x + h, y + h),   # top-right
            (x, y + h)        # top-left
        ]
