from enum import Enum
from typing import Any, Tuple
import numpy.typing as npt
import numpy as np
from math import pi, sin, cos

PI3 = pi / 3.0


class GridType(Enum):
    ORTHOGONAL = "orthogonal"
    PACKED = "packed"

    def get_unit_vector(self) -> npt.NDArray[Any]:
        if self == GridType.ORTHOGONAL:
            return np.array([[1.0, 0.0], [0.0, 1.0]])
        elif self == GridType.PACKED:
            return np.array([[1.0, cos(PI3)], [0.0, sin(PI3)]])

    def in_symmetric_group(self, group, entry) -> bool:
        if self == GridType.ORTHOGONAL:
            return False
        elif self == GridType.PACKED:
            return False

    def get_symmetric_image(self, entry: Tuple[int, int]) -> set[Tuple[int, int]]:
        return set()


GRID_TYPES: list[GridType] = [
    GridType.ORTHOGONAL,
    GridType.PACKED,
]
