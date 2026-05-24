from abc import ABC, abstractmethod
from typing import Any
import numpy as np
from shapely.geometry import Point, Polygon
import numpy.typing as npt


class Shape(ABC):
    @abstractmethod
    def to_shapely(self) -> Polygon | Point:
        pass

    @abstractmethod
    def get_inner(self, offset_from_border: float) -> "Shape":
        pass

    def is_inside(self, x: float, y: float) -> bool:
        shapely_point = Point(x, y)
        geometry = self.to_shapely()
        return geometry.covers(shapely_point)
