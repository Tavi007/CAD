from itertools import product
import math
from typing import Tuple

from lib.grid.generator import get_invariant_power_set, get_lattice_points
from lib.grid.grid_type import GridType
from lib.io.plotter import save_shapes
from lib.shapes.circle import Circle
from lib.shapes.hexagon import Hexagon
from lib.shapes.shape_type import ShapeType

SHAPE_TYPES: list[ShapeType] = [
    # ShapeType.HEXAGON_POINTY,
    # ShapeType.HEXAGON_FLAT,
    # ShapeType.SQUARE,
    # ShapeType.RECTANGLE,
    ShapeType.TRIANGLE,
    # ShapeType.CIRCLE,
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
GAP_SIZE = 2.0


SQRT3 = math.sqrt(3)


def main():
    print_stencil()
    # print_all_boards()


def print_stencil():
    shape_type = ShapeType.HEXAGON_FLAT
    grid_type = GridType.PACKED
    shape = shape_type.get_board_shape(UNIT_LENGTH*3, UNIT_LENGTH*3)
    lattice_points = get_lattice_points(
        grid_type,
        UNIT_LENGTH,
        shape.is_inside,
    )

    # the base stencil shape consist of multiple smaller shapes merged together
    stencil_base_shapes = []
    for point, _ in lattice_points:
        stencil_base_shapes.append(
            Hexagon((point[0], point[1]), UNIT_LENGTH/SQRT3 + 0.01))
    save_shapes({"blue": stencil_base_shapes}, f"output/base.png")

    # for the holes, iterate over the power set.
    # but only add symmetric and translative invariants
    power = get_invariant_power_set(grid_type, lattice_points, 3, 5)
    for i, subset in enumerate(power):
        hole_shapes = []
        for coords in subset:
            hole_shapes.append(
                Hexagon((coords[0], coords[1]), UNIT_LENGTH/SQRT3-1))
        name = f"stencil/{shape_type.value}/{i}"
        save_shapes({
            "blue": stencil_base_shapes,
            "green": hole_shapes,
        },
            f"output/{name}.png")


def print_all_boards():
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

        shape_radius = (UNIT_LENGTH-GAP_SIZE)/2
        shapes = []
        for point, _ in lattice_points:
            shapes.append(Circle((point[0], point[1]), shape_radius))

        name = f"{board_shape_type.value}_board__{grid_type.value}_grid__{width}x{height}"
        if shapes:
            save_shapes({
                "blue": shapes,
                "green": [board_shape],
            },
                f"output/{name}.png")
            print(" - saved")
        else:
            print(f" - no shapes found")


if __name__ == "__main__":
    main()
