from abc import abstractmethod
from dataclasses import dataclass
from typing import Tuple

from lib.shapes.abstract_polygon import AbstractPolygon
from lib.shapes.shape import Shape


@dataclass
class Polygon(AbstractPolygon):
    vertices: list[Tuple[int, int]]

    def get_vertices(self) -> list[Tuple[int, int]]:
        return self.vertices
