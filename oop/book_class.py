class Book:
    """
    A class to represent a book with its title, author, and publication year.
    This class demonstrates the use of Python's magic methods.
    """
    def __init__(self, title, author, year):
        """
        Initializes a Book instance with a title, author, and year.
        This is the constructor method.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"A new book has been created: {self.title}")

    def __del__(self):
        """
        Handles the deletion of a Book instance.
        This is the destructor method.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a human-readable string representation of the book.
        This is used by the built-in str() function and print().
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an unambiguous, developer-friendly string that can be
        used to recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

# --------------------
# main.py
# The following code is provided to test the Book class.
# --------------------

# from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)

    # Demonstrating the __repr__ method
    print(repr(my_book))

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()