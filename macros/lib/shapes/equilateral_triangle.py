from dataclasses import dataclass, field
from typing import Any, Tuple
from lib.shapes.abstract_polygon import AbstractPolygon
import math
import numpy as np
import numpy.typing as npt

SQRT3 = math.sqrt(3)
BASE_TRIANGLE_UP = np.array(
    [[0, 0], [1, 0], [1/2, SQRT3/2]])
BASE_TRIANGLE_DOWN = np.array(
    [[0, 0], [1, 0], [1/2, -SQRT3/2]])


@dataclass
class EquilateralTriangle(AbstractPolygon):
    height: int  # aka the scale
    points_up: bool
    translation: npt.NDArray[np.float64] = field(
        default_factory=lambda: np.array([0.0, 0.0], dtype=np.float64)
    )

    def get_inner(self, offset_from_border: float) -> "EquilateralTriangle":
        new_height = self.height - 3.0 * offset_from_border
        if new_height <= 0:
            raise ValueError(
                "offset_from_border is too large for this triangle"
            )

        # Move the inner triangle toward the centroid so it stays concentric.
        direction = -1.0 if self.points_up else 1.0
        new_translation = self.translation + np.array(
            [0.0, direction * offset_from_border],
            dtype=np.float64,
        )
        return EquilateralTriangle(
            height=new_height,
            points_up=self.points_up,
            translation=new_translation,
        )

    def get_vertices(self) -> list[Tuple[int, int]]:
        if self.points_up:
            return BASE_TRIANGLE_UP*self.height + self.translation
        else:
            return BASE_TRIANGLE_DOWN*self.height + self.translation
