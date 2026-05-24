from dataclasses import dataclass
from typing import Tuple
from lib.shapes.abstract_polygon import AbstractPolygon


@dataclass
class Rectangle(AbstractPolygon):
    width: int
    height: int

    def get_inner(self, offset_from_border: float) -> "Rectangle":
        return Rectangle(
            self.width - offset_from_border*2,
            self.height - offset_from_border*2,
        )

    def get_vertices(self) -> list[Tuple[int, int]]:
        dx = self.width/2
        dy = self.height/2

        return [
            (dx, dy),  # bottom-left
            (dx, -dy),  # bottom-right
            (-dx, -dy),  # top-right
            (-dx, dy)  # top-left
        ]
