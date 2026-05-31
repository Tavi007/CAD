from typing import Callable, Any, Tuple
import numpy as np
import numpy.typing as npt
from lib.grid.grid_type import GridType

MAX_ITER = 100


def get_lattice_points(
    grid_type: GridType,
    unit_length: int,
    filter: Callable[[float, float], bool],
) -> list[Tuple[npt.NDArray[Any], Tuple[int, int]]]:
    unit_vector = grid_type.get_unit_vector()
    points = []
    for i in range(-MAX_ITER, MAX_ITER+1):
        for j in range(-MAX_ITER, MAX_ITER+1):
            steps = np.array([i, j])
            point = unit_vector @ steps * unit_length
            if filter(point[0], point[1]):
                points.append((point, (i, j)))
    return points
