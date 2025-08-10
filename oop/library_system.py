class Book:
    """
    A base class to represent a generic book.
    This class demonstrates the core attributes and methods
    common to all book types.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a Book instance with a title and author.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Provides a string representation for the Book class.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    A derived class representing an electronic book.
    It inherits from the Book class and adds a unique attribute.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes an EBook instance.
        Calls the parent class constructor using super() and
        then initializes its own unique attribute.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Provides a string representation for the EBook class.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    A derived class representing a physical print book.
    It inherits from the Book class and adds a unique attribute.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a PrintBook instance.
        Calls the parent class constructor using super() and
        then initializes its own unique attribute.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Provides a string representation for the PrintBook class.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    A class that demonstrates composition.
    It contains a collection of Book objects (including derived types).
    """
    def __init__(self):
        """
        Initializes a Library instance with an empty list to store books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a book (of any type) to the library's collection.
        This method showcases composition, as a Library is composed of Book objects.
        """
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: The item is not a valid book type.")

    def list_books(self):
        """
        Prints the details of each book in the library's collection.
        This method leverages the __str__ methods of each book type.
        """
        for book in self.books:
            print(book)

# --------------------
# main.py
# This script is provided for testing the functionality of the classes
# defined in library_system.py.
# --------------------

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()