from dataclasses import dataclass
from typing import Tuple
from shapely import Point
from lib.shapes.shape import Shape


@dataclass
class Circle(Shape):
    radius: float

    def get_inner(self, offset_from_border: float) -> "Circle":
        return Circle(
            self.center,
            self.radius - offset_from_border*2,
        )

    def to_shapely(self) -> Point:
        x = self.center[0]
        y = self.center[1]
        r = self.radius
        return Point(x, y).buffer(r)
