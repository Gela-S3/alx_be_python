class Calculator:
    """
    A simple calculator class that contains both a static method and a
    class method to showcase their different behaviors and use cases.
    """
    # A class attribute that can be accessed by class methods.
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        This is a static method. It takes two arguments and returns their sum.
        It does not have access to the class or instance state (no 'self' or 'cls').
        It's essentially a regular function logically grouped within the class.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        This is a class method. It takes the class itself (cls) as its
        first parameter, which allows it to access class-level attributes.
        It prints the calculation type before performing the multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# --------------------
# main.py
# This script is provided for testing the functionality of the
# Calculator class defined in class_static_methods_demo.py.
# --------------------

def main():
    """
    The main function demonstrates how to use the static and class methods
    of the Calculator class.
    """
    # Using the static method. It is called directly on the class.
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method. It is also called directly on the class.
    # It accesses the class attribute 'calculation_type'.
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()