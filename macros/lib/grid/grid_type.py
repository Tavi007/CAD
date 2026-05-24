from enum import Enum
from typing import Any
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
            return np.array([[1.0, 0.0], [0.5, 1.0]])


GRID_TYPES: list[GridType] = [
    GridType.ORTHOGONAL,
    GridType.PACKED,
]
