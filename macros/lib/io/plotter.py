from pathlib import Path
from matplotlib.axes import Axes
import matplotlib.pyplot as plt

from lib.shapes.shape import Shape


def save_shapes(shapes_dict: dict[str, list[Shape]], filename: Path):
    path = Path(filename)
    if not path.parent.exists():
        path.parent.mkdir(parents=True)

    fig, ax = plt.subplots()

    for color, shapes in shapes_dict.items():
        for shape in shapes:
            draw_shape(shape, ax, color=color)

    ax.set_aspect('equal')
    ax.autoscale()
    plt.savefig(str(filename))
    plt.close()


def draw_shape(shape: Shape, ax: Axes, color="blue"):
    poly = shape.to_shapely()
    x, y = poly.exterior.xy
    ax.fill(x, y, alpha=0.5, fc=color, ec="black")
