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

    def get_symmetries(self, indices: list[Tuple[int, int]]) -> set[set[Tuple[int, int]]]:
        if self == GridType.ORTHOGONAL:
            x, y = indices
            return []
        if self == GridType.PACKED:
            symmetries = set()
            for sym_fn in [
                lambda x, y:  (x, y),
                lambda x, y:  (x, -x-y),
                lambda x, y:  (-x, -y),
                lambda x, y:  (-x, x+y),

                lambda x, y:  (y, x),
                lambda x, y:  (y, -x-y),
                lambda x, y:  (-y, -x),
                lambda x, y:  (-y, x+y),

                lambda x, y:  (x+y, -x),
                lambda x, y:  (x+y, -y),
                lambda x, y:  (-x-y, x),
                lambda x, y:  (-x-y, y),
            ]:
                symmetries.add(frozenset([sym_fn(x, y) for x, y in indices]))
            return symmetries


GRID_TYPES: list[GridType] = [
    GridType.ORTHOGONAL,
    GridType.PACKED,
]
