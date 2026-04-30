from matplotlib.axes import Axes
import matplotlib.pyplot as plt

from lib.shapes.shape import Shape

def save_shapes(shapes: list[Shape], board_shape: Shape, filename="output.png"):
    fig, ax = plt.subplots()

    for shape in shapes:
        draw_shape(shape, ax)
    draw_shape(board_shape, ax, color="green")
    
    ax.set_aspect('equal')
    ax.autoscale()
    plt.savefig(filename)
    plt.close()

def draw_shape(shape: Shape, ax: Axes, color="blue"):
    poly = shape.to_shapely()
    x, y = poly.exterior.xy
    ax.fill(x, y, alpha=0.5, fc=color, ec="black")