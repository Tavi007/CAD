from dataclasses import dataclass, field
from typing import Any, Tuple
from lib.shapes.abstract_polygon import AbstractPolygon
import math
import numpy as np
import numpy.typing as npt

SQRT3 = math.sqrt(3)
BASE_TRIANGLE_UP = np.array(
    [[0, 2/3], [1/SQRT3, -1/3], [-1/SQRT3, -1/3]])
BASE_TRIANGLE_DOWN = np.array(
    [[0, -2/3], [1/SQRT3, 1/3], [-1/SQRT3, 1/3]])


@dataclass
class EquilateralTriangle(AbstractPolygon):
    height: int  # aka the scale
    points_up: bool

    def get_inner(self, offset_from_border: float) -> "EquilateralTriangle":
        new_height = self.height - 3*offset_from_border
        if new_height <= 0:
            raise ValueError(
                "offset_from_border is too large for this triangle"
            )

        return EquilateralTriangle(
            self.center,
            height=new_height,
            points_up=self.points_up,
        )

    def get_base_vertices(self) -> list[Tuple[int, int]]:
        if self.points_up:
            return BASE_TRIANGLE_UP*self.height + self.center
        else:
            return BASE_TRIANGLE_DOWN*self.height + self.center
