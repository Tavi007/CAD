from dataclasses import dataclass
from typing import Callable
import math

from lib.grid.grid_type import GridType
from lib.shapes.abstract_polygon import AbstractPolygon
from lib.shapes.shape import Shape

MAX_ITER = 100


def get_shapes(grid_type: GridType, unit_length: int, filter: Callable[[Shape], bool],) -> list[AbstractPolygon]:
    shapes = []
    for i in range(-MAX_ITER, MAX_ITER+1):
        for j in range(-MAX_ITER, MAX_ITER+1):
            shape = grid_type.get_shape(i, j, unit_length)
            if filter(shape):
                shapes.append(shape)

    return shapes
