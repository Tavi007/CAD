from itertools import product
import math
from pathlib import Path
from typing import Tuple

from lib.grid.generator import get_invariant_power_set, get_lattice_points
from lib.grid.grid_type import GridType
from lib.io.lattice_points_io import write_lattice_indices
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
    # print_stencil()
    print_all_boards()


def print_stencil():
    stencil_shape = "triangle"

    if stencil_shape == "hexagon":
        shape_type = ShapeType.HEXAGON_FLAT
        grid_type = GridType.PACKED
        shape = shape_type.get_board_shape(UNIT_LENGTH*3, UNIT_LENGTH*3)
    elif stencil_shape == "triangle":
        shape_type = ShapeType.TRIANGLE
        grid_type = GridType.PACKED
        shape = shape_type.get_board_shape(UNIT_LENGTH*3, UNIT_LENGTH*3)
        shape.translate(0.0, UNIT_LENGTH)

    lattice_points = get_lattice_points(
        grid_type,
        UNIT_LENGTH,
        shape.is_inside,
    )
    path = Path(f"output/stencil/{stencil_shape}")

    # the base stencil shape consist of multiple smaller shapes merged together
    stencil_base_shapes = []
    stencil_base_indices = []
    for point, index in lattice_points:
        stencil_base_shapes.append(
            Hexagon((point[0], point[1]), UNIT_LENGTH/SQRT3 + 0.01))
        stencil_base_indices.append(index)
    save_shapes({"blue": stencil_base_shapes}, path / f"base.png")
    write_lattice_indices(path/"base.txt", stencil_base_indices)

    # for the holes, iterate over the power set.
    # but only add symmetric and translative invariants
    coords_subsets, indices_subsets = get_invariant_power_set(
        grid_type, lattice_points, 3, 5)
    for i, (coords_subset, indices_subset) in enumerate(zip(coords_subsets, indices_subsets)):
        hole_shapes = []
        for coords in coords_subset:
            hole_shapes.append(
                Hexagon((coords[0], coords[1]), UNIT_LENGTH/SQRT3-1))
        save_shapes(
            {
                "blue": stencil_base_shapes,
                "green": hole_shapes,
            },
            path / f"{i}.png")

        write_lattice_indices(path/f"{i}.txt", indices_subset)


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
        indices = []
        for point, index in lattice_points:
            shapes.append(Circle((point[0], point[1]), shape_radius))
            indices.append(index)

        path = Path(
            f"output/board/{board_shape_type.value}/{grid_type.value}/{width}x{height}")
        if shapes:
            save_shapes({
                "blue": shapes,
                "green": [board_shape],
            },
                path.with_suffix(".png")
            )
            write_lattice_indices(path.with_suffix(".txt"), indices)
            print(" - saved")
        else:
            print(f" - no shapes found")


if __name__ == "__main__":
    main()
