from dataclasses import dataclass
from typing import Tuple
from lib.shapes.abstract_polygon import AbstractPolygon
import math


@dataclass
class Hexagon(AbstractPolygon):
    side_length: int
    pointy_top: bool = True

    def get_inner(self, offset_from_border: float) -> "Hexagon":
        return Hexagon(
            self.center,
            self.side_length - offset_from_border,
            self.pointy_top,
        )

    def get_base_vertices(self) -> list[Tuple[int, int]]:
        corners = []
        for i in range(6):
            if self.pointy_top:
                angle = math.radians(60 * i - 30)  # pointy-top
            else:
                angle = math.radians(60 * i)  # flat-top
            cx = self.side_length * math.cos(angle)
            cy = self.side_length * math.sin(angle)
            corners.append((cx, cy))
        return corners
