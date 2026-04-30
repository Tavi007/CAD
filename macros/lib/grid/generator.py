from dataclasses import dataclass
from typing import Callable

from lib.grid.grid_type import GridType, get_shape
from lib.shapes.abstract_polygon import AbstractPolygon
from lib.shapes.shape import Shape

MAX_ITER = 50

def get_shapes(grid_type:GridType, unit_length:int, filter:Callable[[Shape], bool],) -> list[AbstractPolygon]:
    shapes = []
    for i in range(-MAX_ITER, MAX_ITER):
        for j in range(-MAX_ITER, MAX_ITER):
            shape = get_shape(grid_type, i, j, unit_length)
            if filter(shape):
                shapes.append(shape)
                
    return shapes