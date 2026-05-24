from itertools import product
from typing import Tuple

from lib.grid.generator import get_lattice_points
from lib.grid.grid_type import GridType
from lib.io.plotter import save_shapes
from lib.shapes.circle import Circle
from lib.shapes.shape_type import ShapeType

SHAPE_TYPES: list[ShapeType] = [
    ShapeType.HEXAGON_POINTY,
    ShapeType.HEXAGON_FLAT,
    ShapeType.SQUARE,
    ShapeType.RECTANGLE,
    ShapeType.TRIANGLE,
    ShapeType.CIRCLE,
]

GRID_TYPES: list[GridType] = [
    GridType.ORTHOGONAL,
    GridType.PACKED,
]

SIZES: list[Tuple[float, float]] = [
    (125, 90),
    #    (220, 150),
    #    (220, 220)
]

UNIT_LENGTH = 10.0
OFFSET_FROM_BORDER = 5.0


def main():
    for board_shape_type, grid_type, (width, height) in product(SHAPE_TYPES, GRID_TYPES, SIZES):
        print(
            f"building {grid_type.value} grid for {board_shape_type.value} board of size {width}x{height}")

        board_shape = board_shape_type.get_board_shape(width, height)
        inner_shape = board_shape.get_inner(OFFSET_FROM_BORDER + UNIT_LENGTH/2)
        lattice_points = get_lattice_points(
            grid_type,
            UNIT_LENGTH,
            inner_shape.is_inside,
        )

        shape_radius = UNIT_LENGTH/2 - 0.5
        shapes = []
        for point in lattice_points:
            shapes.append(Circle(point[0], point[1], shape_radius))

        name = f"{board_shape_type.value}_board__{grid_type.value}_grid__{width}x{height}"
        if shapes:
            save_shapes(shapes, board_shape,
                        f"output/{name}.png")
            print(" - saved")
        else:
            print(f" - no shapes found")


if __name__ == "__main__":
    main()
