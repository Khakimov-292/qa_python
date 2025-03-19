import pytest

from main import BooksCollector


class TestBooksCollector:
    @pytest.mark.parametrize('name_book', ['Гордость и предубеждение и зомби',
                                           'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_correct_books(self, name_book):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        assert name_book in collector.get_books_genre()

    def test_set_book_genre_add_genre(self, add_books):
        collector = add_books
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_set_book_genre_incorrect_genre(self, add_books):
        collector = add_books
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Роман')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_book_genre(self, add_books):
        collector = add_books
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_books_with_specific_genre_get_name_book(self, add_books):
        collector = add_books
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Человек-амфибия', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Веселые мультфильмы', 'Мультфильмы')
        name_book = collector.get_books_with_specific_genre('Мультфильмы')
        assert name_book == ['Веселые мультфильмы']

    def test_get_books_genre_get_dictionary_book(self, add_books):
        collector = add_books
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_books_genre() == {'Веселые мультфильмы': '',
                                               'Гордость и предубеждение и зомби': 'Фантастика',
                                               'Человек-амфибия': '',
                                               'Что делать, если ваш кот хочет вас убить': 'Ужасы'}

    def test_get_books_for_children_get_cartoon(self, add_books):
        collector = add_books
        collector.set_book_genre('Человек-амфибия', 'Детективы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Веселые мультфильмы', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Веселые мультфильмы']

    def test_add_book_in_favorites_add_book(self, add_books):
        collector = add_books
        collector.add_book_in_favorites('Человек-амфибия')
        assert 'Человек-амфибия' in collector.favorites

    def test_delete_book_from_favorites_delete_one_book(self, add_books):
        collector = add_books
        collector.add_book_in_favorites('Человек-амфибия')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Человек-амфибия')
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_get_one_book(self, add_books):
        collector = add_books
        collector.add_book_in_favorites('Человек-амфибия')
        assert collector.get_list_of_favorites_books() == ['Человек-амфибия']
