import pytest
from .main import BooksCollector
from .data import books_data

@pytest.fixture(scope="function")
def collector():
    books_collector = BooksCollector()
    return books_collector

@pytest.fixture(scope="function")
def name_genre(collector):
    for book, genre in books_data:
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)