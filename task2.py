class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"

    def __str__(self):
        return self.name

class Book:
    total_books = 0  # Class variable to hold the total number of books

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)  # Add this book to the author's list of books
        Book.total_books += 1

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author={self.author})"

    def __str__(self):
        return self.name

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}')"

    def __str__(self):
        return self.name
