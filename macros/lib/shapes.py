from dataclasses import dataclass

@dataclass
class Hexagon:
    def is_point_inside(self, x, y, tol):
        return False
        
@dataclass
class Rectangle:
    corner_x: int
    corner_y: int
    width: int
    height: int
    
    def print_me(self):
        print(self)
        print(self.corner_x)
        print(self.corner_y)
        print(self.width)
        print(self.height)
        
    
    def is_point_inside(self, x, y, tol):
        return self.corner_x+tol <= x and x <= self.corner_x + self.width-tol and self.corner_y+tol <= y and y <= self.corner_y + self.height-tol