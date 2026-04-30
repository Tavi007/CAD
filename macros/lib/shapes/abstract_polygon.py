from abc import abstractmethod
from typing import Tuple

from shapely import Polygon

from lib.shapes.shape import Shape

class AbstractPolygon(Shape):
    @abstractmethod
    def get_vertices(self) -> list[Tuple[int,int]]:
        pass
    
    
    def to_shapely(self) -> Polygon:
        return Polygon(self.get_vertices())