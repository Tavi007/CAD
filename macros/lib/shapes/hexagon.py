from dataclasses import dataclass
from typing import Tuple
from lib.shapes.abstract_polygon import AbstractPolygon
import math


@dataclass
class Hexagon(AbstractPolygon):
    q: int
    r: int
    side_length: int
    pointy_top: bool = True
    side_length_offset: int = 0
    
    def get_vertices(self) -> list[Tuple[int,int]]:
        # Convert axial (q, r) to pixel (x, y)
        x = self.side_length * (math.sqrt(3) * self.q + math.sqrt(3)/2 * self.r)
        y = self.side_length * (3/2 * self.r)

        # Generate 6 corners
        corners = []
        for i in range(6):
            if self.pointy_top:
                angle = math.radians(60 * i - 30)  # pointy-top
            else:
                angle = math.radians(60 * i)  # flat-top
            side_length = self.side_length-self.side_length_offset
            cx = x + side_length * math.cos(angle)
            cy = y + side_length * math.sin(angle)
            corners.append((cx, cy))

        return corners