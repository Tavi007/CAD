from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Tuple
from shapely.geometry import Point, Polygon
import numpy as np


@dataclass
class Shape(ABC):
    center: Tuple[float, float]

    @abstractmethod
    def to_shapely(self) -> Polygon | Point:
        pass

    @abstractmethod
    def get_inner(self, offset_from_border: float) -> "Shape":
        pass

    def get_center(self):
        return np.array([self.center[0], self.center[1]])

    def translate(self, dx: float, dy: float):
        self.center = (self.center[0] + dx, self.center[1] + dy)

    def is_inside(self, x: float, y: float) -> bool:
        shapely_point = Point(x, y)
        geometry = self.to_shapely()
        return geometry.covers(shapely_point)
