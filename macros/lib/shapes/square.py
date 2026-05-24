from dataclasses import dataclass
from typing import Tuple
from lib.shapes.abstract_polygon import AbstractPolygon


@dataclass
class Square(AbstractPolygon):
    length: int

    def get_inner(self, offset_from_border: float) -> "Square":
        return Square(
            self.length - offset_from_border*2,
        )

    def get_vertices(self) -> list[Tuple[int, int]]:
        dx = self.length/2

        return [
            (dx, dx),   # bottom-left
            (dx, -dx),  # bottom-right
            (-dx, -dx),  # top-right
            (-dx, dx)  # top-left
        ]
