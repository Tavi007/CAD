from pathlib import Path


def write_lattice_indices(filename: Path, lattice_points: list[tuple[int, int]]):
    with open(filename, "w") as f:
        for point in lattice_points:
            f.write(f"{point[0]},{point[1]}\n")


def read_lattice_indices(filename: Path) -> list[tuple[int, int]]:
    lattice_points = []
    with open(filename, "r") as f:
        for line in f:
            x_str, y_str = line.strip().split(",")
            lattice_points.append((int(x_str), int(y_str)))
    return lattice_points
