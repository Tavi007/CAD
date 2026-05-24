from dataclasses import dataclass
from shapely import Point
from lib.shapes.shape import Shape


@dataclass
class Circle(Shape):
    mid_x: float
    mid_y: float
    radius: float

    def get_inner(self, offset_from_border: float) -> "Circle":
        return Circle(
            self.mid_x,
            self.mid_y,
            self.radius - offset_from_border*2,
        )

    def to_shapely(self) -> Point:
        x = self.mid_x
        y = self.mid_y
        r = self.radius
        return Point(x, y).buffer(r)
