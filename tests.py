import random
import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self,books_collector):
        # создаем экземпляр (объект) класса BooksCollector


        # добавляем две книги
        books_collector.add_new_book('Гордость и предубеждение и зомби')
        books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(list(books_collector.books_genre)) == 2

    @pytest.mark.parametrize('name, genre', [
        ['Снеговик', 'Детективы'],
        ['Питер Пэн', 'Фантастика']
    ])
    def test_set_book_genre_valid_name(self, books_collector, name, genre):

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.books_genre[name] == genre

    def test_get_book_genre_return_valid_name(self, books_collector):

        books_collector.add_new_book('Смешарики снимают кино')
        books_collector.set_book_genre('Смешарики снимают кино', 'Мультфильмы')
        assert books_collector.get_book_genre('Смешарики снимают кино') == 'Мультфильмы'

    def test_get_books_with_specific_genre_when_valid_genre(self, books_collector):

        books_collector.add_new_book('Чебурашка')
        books_collector.set_book_genre('Чебурашка', 'Мультфильмы')

        assert books_collector.get_books_with_specific_genre('Мультфильмы')== ['Чебурашка']


    def test_get_books_genre_filled_dict(self, books_collector):

        books = ['Бесы', 'Другой дом', 'Двадцать тысяч лье под водой', 'Понаехавшая']
        for name in books:
            books_collector.add_new_book(name)

        random_book = random.choice(books)
        assert random_book in books_collector.get_books_genre() \
               and type(books_collector.get_books_genre()) == dict

    def test_get_books_for_children_correct_genre(self, books_collector):

        books = ['Витя Малеев в школе и дома', 'Путешествие Алисы']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre[x])
            x += 1
        assert books_collector.get_books_for_children()



    def test_add_book_in_favorites_when_books_in_list(self, books_collector):

        books = ['Семь способов засолки душ', 'Пожиратели призраков', 'Книга несчастных случаев', 'Лес']
        for name in books:
            books_collector.add_new_book(name)
        books_collector.add_book_in_favorites('Книга несчастных случаев')

        assert 'Книга несчастных случаев' in books_collector.favorites

    def test_delete_book_from_favorites(self, books_collector):

        books = ['Море сновидений', 'Через пески', 'Старплекс']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        books_collector.delete_book_from_favorites('Через пески')
        assert 'Через пески' not in books_collector.favorites

    def test_get_list_of_favorites_books_not_empty(self, books_collector):

        books = ['1984', 'Игра Эндера', 'Вегетация']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert books_collector.get_list_of_favorites_books()== ['1984', 'Игра Эндера', 'Вегетация']

        # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()