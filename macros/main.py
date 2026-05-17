from itertools import product
from typing import Tuple

from lib.grid.generator import get_shapes
from lib.grid.grid_type import GridType
from lib.io.plotter import save_shapes
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
    GridType.HEX,
    GridType.SQUARE,
    GridType.TRIANGLE,
]

SIZES: list[Tuple[float, float]] = [
    (125, 90),
    (220, 150)
]

UNIT_LENGTH = 10
OFFSET_FROM_BORDER = 5


def main():
    for board_shape_type, grid_type, (width, height) in product(SHAPE_TYPES, GRID_TYPES, SIZES):
        print(
            f"building {grid_type.value} grid for {board_shape_type.value} board of size {width}x{height}")

        board_shape = board_shape_type.get_board_shape(width, height)
        inner_shape = board_shape.get_inner(OFFSET_FROM_BORDER)
        shapes = get_shapes(grid_type, UNIT_LENGTH, inner_shape.is_inside)

        name = f"{board_shape_type.value}_board__{grid_type.value}_grid__{width}x{height}"
        if shapes:
            save_shapes(shapes, board_shape,
                        f"output/{name}.png")
            print(" - saved")
        else:
            print(f" - no shapes found")


if __name__ == "__main__":
    main()
