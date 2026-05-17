from dataclasses import dataclass
from typing import Tuple
from lib.shapes.abstract_polygon import AbstractPolygon
import math
import numpy as np

SQRT3 = math.sqrt(3)
BASE_TRIANGLE_UP = np.array([[0, 3/SQRT3/2], [-1/2, 0], [1/2, 0]])
BASE_TRIANGLE_DOWN = np.array([[-1/2, 3/SQRT3/2], [1/2, 3/SQRT3/2], [0, 0]])


@dataclass
class Triangle(AbstractPolygon):
    row: int
    col: int
    side_length: int
    side_length_offset: int = 0

    def get_inner(self, offset_from_border: float) -> "Triangle":
        return Triangle(
            self.row,
            self.col,
            self.side_length - offset_from_border,
            0
        )

    def points_up(self) -> bool:
        return (self.row + self.col) % 2 == 0

    def get_vertices(self) -> list[Tuple[int, int]]:
        real_side_length = self.side_length - self.side_length_offset
        delta_row = (self.side_length + self.side_length_offset) / 2
        if self.points_up():
            corners = BASE_TRIANGLE_UP.copy()
            corners *= real_side_length
            if self.col % 2 == 0:
                translation = np.array([
                    self.row*delta_row,
                    self.col*self.side_length*3/2/SQRT3,
                ])
            else:
                translation = np.array([
                    self.row*delta_row,
                    self.col*self.side_length*3/2/SQRT3,
                ])
        else:
            corners = BASE_TRIANGLE_DOWN.copy()
            corners *= real_side_length
            if self.col % 2 == 0:
                translation = np.array([
                    self.row*delta_row,
                    self.col*self.side_length*3/2/SQRT3,
                ])
            else:
                translation = np.array([
                    self.row*delta_row,
                    self.col*self.side_length*3/2/SQRT3,
                ])

        tria = []
        for i in range(3):
            tria.append(corners[i] + translation)
        return tria
