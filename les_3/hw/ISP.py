from abc import ABC, abstractmethod
from math import pi


# Принцип ISP

class Shape(ABC):

    @abstractmethod
    def area():
        ...

    @abstractmethod
    def perimeter():
        ...


class Shape3D(ABC):

    @abstractmethod
    def volume():
        ...


class Circle(Shape):

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * pi * self.radius


class Cube(Shape, Shape3D):

    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return 6 * self.side ** 2

    def perimeter(self) -> float:
        return self.side * 12

    def volume(self) -> float:
        return self.side ** 3


if __name__ == '__main__':

    # К принципу ISP
    circle = Circle(5)
    print(circle.area(), circle.perimeter())
    cube = Cube(5)
    print(cube.area(), cube.perimeter(), cube.volume())
