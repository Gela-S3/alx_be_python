import math

class Shape:
    """
    A base class for different shapes.
    It defines a common interface with an 'area' method that must be
    overridden by its subclasses.
    """
    def area(self):
        """
        Calculates the area of the shape.
        Raises an error to ensure this method is implemented in derived classes.
        """
        raise NotImplementedError("Subclass must implement abstract method 'area'")

class Rectangle(Shape):
    """
    A derived class representing a rectangle.
    It inherits from Shape and overrides the area method.
    """
    def __init__(self, length: float, width: float):
        """
        Initializes a Rectangle instance with its length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.
        This method overrides the area() method from the parent Shape class.
        """
        return self.length * self.width

class Square(Rectangle):
    """
    A derived class representing a square.
    It inherits from Rectangle and uses its area() method,
    showcasing a simple use of inheritance.
    """
    def __init__(self, side: float):
        """
        Initializes a Square instance by calling the parent Rectangle
        constructor with length and width set to the same side value.
        """
        super().__init__(side, side)

class Circle(Shape):
    """
    A derived class representing a circle.
    It inherits from Shape and overrides the area method.
    """
    def __init__(self, radius: float):
        """
        Initializes a Circle instance with its radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle using math.pi.
        This method overrides the area() method from the parent Shape class.
        """
        return math.pi * (self.radius ** 2)

# --------------------
# main.py
# This script is provided for testing the functionality of the classes
# defined in polymorphism_demo.py.
# --------------------

def main():
    """
    The main function demonstrates polymorphism by iterating through a list
    of different shape objects and calling their respective area() methods.
    """
    # Create a list of different shape objects
    shapes = [
        Rectangle(10, 5),
        Circle(7),
        Square(4)
    ]

    # Iterate over the list and call the area() method on each object
    # This demonstrates polymorphism: the same method call results in
    # different behavior depending on the object's class.
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()