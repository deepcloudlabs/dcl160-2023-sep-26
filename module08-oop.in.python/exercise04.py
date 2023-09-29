import math
from functools import reduce
from random import randint


class shape:  # abstract class/interface
    def area(self) -> float:
        pass

    def circumference(self) -> float:
        pass


class square(shape):
    def __init__(self, edge: float):
        self.edge = edge
        self.dimension = 2

    def area(self) -> float:
        return self.edge * self.edge

    def circumference(self) -> float:
        return 4. * self.edge

    def __str__(self):
        return f"square[ edge: {self.edge}]"


class cube(shape):
    def __init__(self, edge: float):
        self.edge = edge
        self.dimension = 3

    def area(self) -> float:
        return 6. * self.edge * self.edge

    def circumference(self) -> float:
        return 12. * self.edge

    def __str__(self):
        return f"cube[ edge: {self.edge}]"


class circle(shape):
    def __init__(self, radius: float):
        self.radius = radius
        self.dimension = 2

    def area(self) -> float:
        return math.pi * self.radius * self.radius

    def circumference(self) -> float:
        return 2. * math.pi * self.radius

    def __str__(self):
        return f"circle[ radius: {self.radius}]"


class sphere(shape):
    def __init__(self, radius: float):
        self.radius = radius
        self.dimension = 3

    def area(self) -> float:
        return math.pi * self.radius * self.radius

    def circumference(self) -> float:
        return 2. * math.pi * self.radius

    def __str__(self):
        return f"circle[ radius: {self.radius}]"


def get_area_planar_shapes(shapes: list[shape]) -> float:
    return reduce(lambda acc, area: acc + area, map(lambda s: s.area(), filter(lambda s: s.dimension == 2, shapes)))


shapes = [circle(10), square(20), cube(30), square(40), circle(50), sphere(60)]
total_area = get_area_planar_shapes(shapes)
print(f"total area is {total_area}")
shape1: shape = None
dice = randint(0, 3)
if dice == 0:
    shape = square(10)
elif dice == 1:
    shape = cube(20)
elif dice == 2:
    shape = circle(30)
elif dice == 3:
    shape = sphere(40)

print(type(shape))
if isinstance(shape, square):
    print("This is a square")
elif isinstance(shape, cube):
    print("This is a cube")
elif isinstance(shape, circle):
    print("This is a circle")
elif isinstance(shape, sphere):
    print("This is a sphere")

match shape:
    case square():
        print("This is a square")
    case cube():
        print("This is a cube")
    case circle():
        print("This is a circle")
    case sphere():
        print("This is a sphere")
    case _:
        print("This is another shape")
