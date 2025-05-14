from abc import ABC, abstractmethod

class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'
    

class LibraryInterface(ABC):
    @abstractmethod
    def add(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove(self, title: str) -> None:
        pass

    @abstractmethod
    def list_books(self) -> list[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self._books: list[Book] = []

    def add(self, book: Book) -> None:
        self._books.append(book)

    def remove(self, title: str) -> None:
        self._books = [b for b in self._books if b.title != title]

    def list_books(self) -> list[Book]:
        return list(self._books)


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self._library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self._library.add(book)

    def remove_book(self, title: str) -> None:
        self._library.remove(title)

    def show_books(self) -> None:
        books = self._library.list_books()
        if not books:
            print("Library is empty.")
        for book in books:
            print(book)


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
