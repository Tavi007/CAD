from itertools import chain, combinations
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


def get_invariant_power_set(
    grid_type: GridType,
    points: list[Tuple[npt.NDArray[Any], Tuple[int, int]]],
    min_holes: int,
    max_holes: int,
) -> set[list[Tuple[npt.NDArray[Any], Tuple[int, int]]]]:
    invariant_coord_subsets = list()
    all_subsets = list()
    for subset in _power_set(points):
        if min_holes <= len(subset) <= max_holes:
            continue

        # unpack
        coords = []
        indices = []
        for entry in subset:
            coord, index = entry
            coords.append(coord)
            indices.append(index)

        # get and analyse symmetries
        symmetries = grid_type.get_symmetries(indices)
        found = False
        for symmetry in symmetries:
            if symmetry in all_subsets:
                found = True
                break

        if not found:
            invariant_coord_subsets.append(coords)
            all_subsets.extend(symmetries)
    return invariant_coord_subsets


def _power_set(iterable):
    "_power_set([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))
