import pytest

from main import BooksCollector


class TestBooksCollector:
    @pytest.mark.parametrize('name_book, expected_result', [
        ('Невероятная и печальная история о простодушной Эрендире и её бессердечной бабушке', False),
        ('Гордость и предубеждение и зомби', True),
        ('Что делать, если ваш кот хочет вас убить', True)])
    def test_add_new_book_correct_and_incorrect_books(self, name_book, expected_result):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        if name_book in collector.books_genre:
            result = True
        else:
            result = False
        assert expected_result == result

    @pytest.fixture(autouse=True)
    def add_books(self):
        self.collector = BooksCollector()
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        self.collector.add_new_book('Человек-амфибия')
        self.collector.add_new_book('Веселые мультфильмы')

    def test_set_book_genre_add_genre(self, add_books):
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        # assert 'Гордость и предубеждение и зомби' in self.collector.books_genre
        assert self.collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_set_book_genre_incorrect_genre(self, add_books):
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Роман')
        assert self.collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_book_genre(self):
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert self.collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_books_with_specific_genre_get_name_book(self):
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        self.collector.set_book_genre('Человек-амфибия', 'Фантастика')
        self.collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        self.collector.set_book_genre('Веселые мультфильмы', 'Мультфильмы')
        name_book = self.collector.get_books_with_specific_genre('Мультфильмы')
        assert name_book == ['Веселые мультфильмы']

    def test_get_books_genre_get_dictionary_book(self):
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        self.collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert self.collector.get_books_genre() == {'Веселые мультфильмы': '',
                                                    'Гордость и предубеждение и зомби': 'Фантастика',
                                                    'Человек-амфибия': '',
                                                    'Что делать, если ваш кот хочет вас убить': 'Ужасы'}

    def test_get_books_for_children_get_cartoon(self):
        self.collector.set_book_genre('Человек-амфибия', 'Детективы')
        self.collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        self.collector.set_book_genre('Веселые мультфильмы', 'Мультфильмы')
        assert self.collector.get_books_for_children() == ['Веселые мультфильмы']

    def test_add_book_in_favorites_add_book(self):
        self.collector.add_book_in_favorites('Человек-амфибия')
        assert 'Человек-амфибия' in self.collector.favorites

    def test_delete_book_from_favorites_delete_one_book(self):
        self.collector.add_book_in_favorites('Человек-амфибия')
        self.collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        self.collector.delete_book_from_favorites('Человек-амфибия')
        assert len(self.collector.favorites) == 1

    def test_get_list_of_favorites_books_an_empty_list(self):
        assert self.collector.get_list_of_favorites_books() == []
