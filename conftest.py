import pytest

from main import BooksCollector


@pytest.fixture(autouse=True)
def add_books():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    collector.add_new_book('Человек-амфибия')
    collector.add_new_book('Веселые мультфильмы')
    return collector
