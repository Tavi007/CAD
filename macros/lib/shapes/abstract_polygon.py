from abc import abstractmethod
from typing import Tuple

from shapely import Polygon

from lib.shapes.shape import Shape


class AbstractPolygon(Shape):
    @abstractmethod
    def get_base_vertices(self) -> list[Tuple[int, int]]:
        pass

    def to_shapely(self) -> Polygon:
        vertices = self.get_base_vertices()
        translated_vertices = []
        translation = self.get_center()
        for vert in vertices:
            translated_vertices.append(translation + vert)
        return Polygon(translated_vertices)
