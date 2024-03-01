from datetime import datetime
from datetime import timedelta


class Book:
    # Default constructor
    def __init__(self, title, author, synopsis, publisher, publish_date, page_count, tags):
        # Class properties
        self.title = title
        self.author = author
        self.synopsis = synopsis
        self.publisher = publisher
        self.publish_date = publish_date
        self.page_count = page_count
        self.tags = tags

    # Method to return a string representation of the book
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publish_date.year})"
    
    # Method to return a string representation of the book in detail
    def __repr__(self):
        return f"{self.title} by {self.author} ({self.publish_date.year}), {self.page_count} pages"

    def days_hours_minutes(td):
        return td.days, td.seconds//3600, (td.seconds//60)%60

    # Method to return a reading time by page count
    def get_reading_time(self):
        if self.page_count <= 0:
            raise Exception("Unable to determine reading time from page count.")
        minutes = self.page_count * 2
        return timedelta(minutes=minutes)

    def get_published_age(self):
        if self.publish_date is None or self.publish_date == datetime.min:
            raise Exception("PublishDate not defined")
        return datetime.now() - self.publish_date

from typing import List

class BookList:
    # Static property to hold the list of books
    #books = []
    books: List[Book] = []

    # Static method to initialize the list of books. Called in the other
    # static methods to avoid needing to explicit initialize the value.
    @staticmethod
    def initialize(force=False):
        if len(BookList.books) > 0 and not force:
            return False
        return True
    
    # Ensure a book is valid for the list.
    @staticmethod
    def validate(book):
        prefix = "Book validation failed: Book must be defined with the Title, Author, and PublishDate properties, but"
        if book is None:
            raise Exception(f"{prefix} was null")
        if book.title is None or book.title == "":
            raise Exception(f"{prefix} Title wasn't defined")
        if book.author is None or book.author == "":
            raise Exception(f"{prefix} Author wasn't defined")
        if book.publish_date is None or book.publish_date == datetime.min:
            raise Exception(f"{prefix} PublishDate wasn't defined")
    
    # Static methods to manage the list of books.
    # Add a book if it's not already in the list.
    @staticmethod
    def add(book):
        BookList.initialize()
        BookList.validate(book)
        if book in BookList.books:
            raise Exception(f"Book '{book}' already in list")
        if BookList.find(lambda b: b.title == book.title and b.author == book.author and b.publish_date == book.publish_date):
            raise Exception(f"Book '{book}' already in list")
        BookList.books.append(book)
    
    # Clear the list of books.
    @staticmethod
    def clear():
        BookList.initialize()
        BookList.books.clear()
    
    # Find a specific book using a filtering scriptblock.
    @staticmethod
    def find(predicate):
        BookList.initialize()
        return list(filter(predicate, BookList.books))
    
    # Find every book matching the filtering scriptblock.
    @staticmethod
    def find_all(predicate):
        BookList.initialize()
        return list(filter(predicate, BookList.books))
    
    # Remove a specific book.
    @staticmethod
    def remove(book):
        BookList.initialize()
        BookList.books.remove(book)
    
    # Remove a book by property value.
    @staticmethod
    def remove_by(property, value):
        BookList.initialize()
        index = BookList.books.findindex(lambda b: b.property == value)
        if index >= 0:
            BookList.books.removeat(index)