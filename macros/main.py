from lib.grid.generator import get_shapes
from lib.grid.grid_type import GridType
from lib.io.plotter import save_shapes
from lib.shapes.circle import Circle
from lib.shapes.hexagon import Hexagon
from lib.shapes.rectangle import Rectangle
from lib.shapes.shape import Shape
from lib.shapes.square import Square

BOARD_SHAPES: dict[str, Shape] = {
    #"big_square": Square(0, 0, 200),
    #"big_rect": Rectangle(0, 0, 200, 150),
    #"big_pointy_hex": Hexagon(0, 0, 110, True),
    #"big_flat_hex": Hexagon(0, 0, 110, False),
    #"big_circle": Circle(0, 0, 110),
    "small_square": Square(0, 0, 50),
    "small_rect": Rectangle(0, 0, 50, 20),
    "small_pointy_hex": Hexagon(0, 0, 40, True),
    "small_flat_hex": Hexagon(0, 0, 40, False),
    "small_circle": Circle(0, 0, 40),
}

UNIT_LENGTH = 9

def main():
    
    for name, board_shape in BOARD_SHAPES.items():
        for grid_type in GridType:
            print(f"building {grid_type} grid for board {name}")
            shapes = get_shapes(grid_type, UNIT_LENGTH, board_shape.is_inside)
            if shapes:
                print("save")
                save_shapes(shapes, board_shape, f"output/{name}__{grid_type.value}.png")
            else:
                print(f"no shapes found for {name} and {grid_type.value}")


if __name__ == "__main__":
    main()