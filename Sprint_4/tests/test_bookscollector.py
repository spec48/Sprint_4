import pytest
from .data import *


class TestBooksCollector:

    @pytest.mark.parametrize('book_name', [[book_1,], [book_1, book_2]])
    def test_add_new_book_add_two_books_success(self, collector, book_name):
        for book in book_name:
            collector.add_new_book(book)
        assert len(collector.get_books_genre()) == len(book_name)

    @pytest.mark.parametrize('book_name', [[book_1, book_1]])
    def test_add_new_book_two_identical_books_fail(self, collector, book_name):
        for book in book_name:
            collector.add_new_book(book)
            assert len(collector.get_books_genre()) == 1

    def test_add_new_book_41_chars_in_book_fail(self, collector):
        collector.add_new_book(book_3)
        assert collector.get_books_genre() == {}

    def test_set_book_genre_success(self, collector):
        collector.add_new_book(book_1)
        collector.set_book_genre(book_1, genre_1)
        assert collector.get_books_genre()[book_1] == genre_1

    def test_set_book_genre_not_in_genre_fail(self, collector):
        collector.add_new_book(book_2)
        collector.set_book_genre(book_2, genre_2)
        assert collector.get_books_genre()[book_2] == ''

    def test_set_book_genre_name_not_in_books_genre_fail(self, collector):
        collector.add_new_book(book_2)
        collector.set_book_genre(book_1, genre_1)
        assert collector.books_genre.get(book_1) is None

    def test_get_book_genre_success(self, collector):
        collector.add_new_book(book_1)
        collector.set_book_genre(book_1, genre_1)
        assert collector.get_book_genre(book_1) == genre_1

    def test_get_books_with_specific_genre_success(self, collector, name_genre):
        assert collector.get_books_with_specific_genre(genre_1) == [book_1, book_4]

    def test_get_books_with_specific_genre_fail(self, collector, name_genre):
        assert collector.get_books_with_specific_genre(genre_2) == []

    def test_get_books_genre_success(self, collector):
        collector.add_new_book(book_1)
        collector.set_book_genre(book_1, genre_1)
        assert collector.get_books_genre() == {book_1: genre_1}

    def test_get_books_for_children_success(self, collector, name_genre):
        assert collector.get_books_for_children() == [books_data[0][0], books_data[2][0],
                                                      books_data[3][0], books_data[4][0]]

    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book(book_1)
        collector.add_book_in_favorites(book_1)
        assert collector.favorites == [book_1]

    def test_add_book_in_favorites_fail(self, collector):
        collector.add_book_in_favorites(book_1)
        assert collector.favorites == []

    def test_add_book_in_favorites_two_identical_books_fail(self, collector):
        collector.add_new_book(book_1)
        collector.add_book_in_favorites(book_1)
        collector.add_book_in_favorites(book_1)
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_success(self, collector):
        collector.add_new_book(book_1)
        collector.add_book_in_favorites(book_1)
        collector.delete_book_from_favorites(book_1)
        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_fail(self, collector):
        collector.add_new_book(book_1)
        collector.delete_book_from_favorites(book_1)
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_success(self, collector):
        collector.add_new_book(book_1)
        collector.add_book_in_favorites(book_1)
        assert collector.get_list_of_favorites_books() == [book_1]
