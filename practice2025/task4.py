from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def area(self):
        return self.__width * self.__height


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return math.pi * (self.__radius ** 2)


# --- Поліморфізм у дії ---
def print_area(shape_obj):
    print(f"Area: {shape_obj.area():.2f}")

shapes = [
    Rectangle(4, 5),
    Circle(3),
    Rectangle(2, 10),
    Circle(1.5)
]

for s in shapes:
    print_area(s)

