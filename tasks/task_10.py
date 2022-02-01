from dataclasses import dataclass
from sources import Point


@dataclass
class Rectangle:
    width: int
    height: int
    coords: Point

    def get_coordinates(self):
        return self.coords

    def get_square(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*(self.width+self.height)



if __name__ == '__main__':
    rectangle = Rectangle(width=10, height=5, coords=Point(0, 5))
    print(rectangle.get_coordinates())
    print(rectangle.get_perimeter())
    print(rectangle.get_square())



