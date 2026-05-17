from abc import ABC, abstractmethod
from shapely.geometry import Point, Polygon


class Shape(ABC):
    @abstractmethod
    def to_shapely(self) -> Polygon | Point:
        pass

    @abstractmethod
    def get_inner(self, offset_from_border: float) -> "Shape":
        pass

    def is_inside(self, other: "Shape") -> bool:
        self_shape = self.to_shapely()
        other_shape = other.to_shapely()
        return self_shape.contains(other_shape)
