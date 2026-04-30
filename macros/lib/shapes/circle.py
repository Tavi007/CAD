from dataclasses import dataclass
from shapely import Point
from lib.shapes.shape import Shape

@dataclass
class Circle(Shape):
    mid_x: int
    mid_y: int
    radius: int
    
    def to_shapely(self) -> Point:
        x = self.mid_x
        y = self.mid_y
        r = self.radius
        return Point(x, y).buffer(r)  