class Book:
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute for encapsulation

    def check_out(self):
        """
        Marks the book as checked out if it's currently available.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as available if it's currently checked out.

        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Checks if the book is currently available (not checked out).

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """
        Adds a Book instance to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Error: Only Book objects can be added to the library.")

    def check_out_book(self, title):
        """
        Attempts to check out a book by its title.

        Args:
            title (str): The title of the book to check out.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book.check_out():
                    print(f"'{title}' has been successfully checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        if not found:
            print(f"Book with title '{title}' not found in the library.")

    def return_book(self, title):
        """
        Attempts to return a book by its title.

        Args:
            title (str): The title of the book to return.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book.return_book():
                    print(f"'{title}' has been successfully returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        if not found:
            print(f"Book with title '{title}' not found in the library.")

    def list_available_books(self):
        """
        Lists all books that are currently available in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books currently available in the library.")