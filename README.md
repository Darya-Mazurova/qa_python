1.Добавление 2х книг.
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector

        books_collector = BooksCollector()

        # добавляем две книги
        books_collector.add_new_book('Гордость и предубеждение и зомби')
        books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(list(books_collector.books_genre)) == 2

2.Тест с параметризацией добавляет новые книги и проверяет задавание книгам жанров

        #создаем параметризацию
    @pytest.mark.parametrize('name, genre', [
        ['Снеговик', 'Детективы'],
        ['Питер Пэн', 'Фантастика']
    ])
        
    def test_set_book_genre_valid_name(self, name, genre):
        books_collector = BooksCollector()
        
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.books_genre[name] == genre

3.Тест проверяет возвращение жанра книги по названию
Добавляется книга, задается жанр. Проверяется что по названию возвращается жанр.

    def test_get_book_genre_return_valid_name(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Смешарики снимают кино')
        books_collector.set_book_genre('Смешарики снимают кино', 'Мультфильмы')
        assert books_collector.get_book_genre('Смешарики снимают кино') == 'Мультфильмы'

4.Тест проверяет что нельзя получить список по определенному жанру, если список пустой или жанр невалидный.
Через параметризацию добавляем книги и пробуем получить по жанру список
#####
    Тест проверяет, что можно получить название книг по жанру.
@pytest.mark.parametrize('name, genre', [['', 'Ужасы'], ['Снеговик', 'Детектив']])
def test_get_books_with_specific_genre_title_of_the_book_by_genre(self, books_collector, name, genre):
    books_collector.add_new_book(name)
    assert books_collector.get_books_with_specific_genre('Детектив')== 'Снеговик'

@pytest.mark.parametrize('name, genre', [['Дракула', 'Ужасы'], ['Снеговик', 'Детектив']])
    def test_get_books_with_specific_genre_empty_list_book_false_genre(self, name, genre):
        
        books_collector.add_new_book(name)
        assert not books_collector.get_books_with_specific_genre('Детектив')

5.Тест проверяет что в список добавились все книги и что все они помещаются в словарь.
Циклом добавляем книги, в переменную кладем рандомное название книги и проверяем.

    def test_get_books_genre_filled_dict(self):
        books_collector = BooksCollector()
        books = ['Бесы', 'Другой дом', 'Двадцать тысяч лье под водой', 'Понаехавшая']
        for name in books:
            books_collector.add_new_book(name)

        random_book = random.choice(books)
        assert random_book in books_collector.get_books_genre() \
               and type(books_collector.get_books_genre()) == dict

6.Книги с возрастным рейтингом отсутствуют в списке книг для детей. Тест проверяет что книги с рейтингом жанров 18+ не попадают в список книг для детей. Циклом добавляем книги и задаем им жанры 18+, далее ассертим.
#####
    def test_get_books_for_children_adult_rating(self):
        books_collector = BooksCollector()
        books = ['Витя Малеев в школе и дома', 'Путешествие Алисы']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre_age_rating[x])
            x += 1

7.Тест проверяет что книга добавленная в избранное есть в избранном. Циклом добавляем книги в список, затем добавляем одну книгу по названию в избранное

    def test_add_book_in_favorites_when_books_in_list(self):
        books_collector = BooksCollector()
        books = ['Семь способов засолки душ', 'Пожиратели призраков', 'Книга несчастных случаев', 'Лес']
        for name in books:
            books_collector.add_new_book(name)
        books_collector.add_book_in_favorites('Книга несчастных случаев')

        assert 'Книга несчастных случаев' in books_collector.favorites

8.Удаление книги из избранного, если она там есть. Тест проверяет удаление книги из избранного.
Циклом добавляем книги в список, затем добавляем всех в избранное и удаляем книгу по названию.
В заключении ассертим удаление книги из списка избранного
```
    def test_delete_book_from_favorites(self):
        books_collector = BooksCollector()
        books = ['Море сновидений', 'Через пески', 'Старплекс']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        books_collector.delete_book_from_favorites('Через пески')
        assert 'Через пески' not in books_collector.favorites

9.Тест проверяет метод который возвращает список избранных книг.
Циклом добавляем книги в список, затем добавляем  всех в избранное.
Ассертим получение списка.
 #####   
    def test_get_list_of_favorites_books_not_empty(self, books_collector):
        
        books = ['1984', 'Игра Эндера', 'Вегетация']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert books_collector.get_list_of_favorites_books()== books
