from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_rating_rating_between_1_and_10(self, collector):
        collector.add_new_book('Harry Potter And The Prisoner Of Azkaban')
        collector.set_book_rating('Harry Potter And The Prisoner Of Azkaban', 9)
        assert collector.books_rating['Harry Potter And The Prisoner Of Azkaban'] == 9

    def test_set_book_rating_set_rating_more_than_10(self, collector):
        collector.add_new_book('Harry Potter And The Chamber Of Secrets')
        collector.set_book_rating('Harry Potter And The Chamber Of Secrets', 11)
        assert collector.books_rating['Harry Potter And The Chamber Of Secrets'] == 1

    def test_get_book_rating_book_in_list(self, collector):
        collector.add_new_book('All Of Us Villains')
        collector.set_book_rating('All Of Us Villains', 7)
        assert collector.get_book_rating('All Of Us Villains') == 7

    def test_get_books_with_specific_rating_two_books(self, collector):
        collector.add_new_book('The Love Hypothesis')
        collector.set_book_rating('The Love Hypothesis', 7)
        collector.add_new_book('November 9')
        collector.set_book_rating('November 9', 6)
        collector.add_new_book('Sky In The Deep')
        collector.set_book_rating('Sky In The Deep', 6)
        assert len(collector.get_books_with_specific_rating(6)) == 2

    def test_get_books_rating_three_books(self, collector):
        collector.add_new_book('These Violent Delights')
        collector.set_book_rating('These Violent Delights', 4)
        collector.add_new_book('Serpent Dove')
        collector.set_book_rating('Serpent Dove', 6)
        collector.add_new_book('The Tiger At Midnight')
        collector.set_book_rating('The Tiger At Midnight', 7)
        assert collector.get_books_rating() == {'These Violent Delights': 4,
                                                'Serpent Dove': 6,
                                                'The Tiger At Midnight': 7}

    def test_add_book_in_favorites_add_new_book(self, collector):
        collector.add_new_book('Harry Potter And The Philosopher Stone')
        collector.add_book_in_favorites('Harry Potter And The Philosopher Stone')
        assert collector.favorites == ['Harry Potter And The Philosopher Stone']

    def test_add_book_in_favorites_book_already_in_favorites(self, collector):
        collector.add_new_book('Bridge Kingdom')
        collector.add_book_in_favorites('Bridge Kingdom')
        collector.add_book_in_favorites('Bridge_kingdom')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_book_in_favorites(self, collector):
        collector.add_new_book('To Kill A Kingdom')
        collector.add_book_in_favorites('To Kill A Kingdom')
        collector.delete_book_from_favorites('To Kill A Kingdom')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_list_of_two_books(self, collector):
        collector.add_new_book('White Hot Kiss')
        collector.add_new_book('Corrupt')
        collector.add_book_in_favorites('White Hot Kiss')
        collector.add_book_in_favorites('Corrupt')
        assert collector.get_list_of_favorites_books() == ['White Hot Kiss', 'Corrupt']

    def test_get_list_of_favorites_books_empty_list(self, collector):
        collector.add_new_book('Harry Potter And The Half-Blood Prince')
        assert collector.get_list_of_favorites_books() == []
