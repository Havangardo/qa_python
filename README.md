# qa_python

### Unit tests for BooksCollector class.

---

All methods are covered with positive tests. The following checks are currently implemented:

- **test_add_new_book_add_two_books:** test add_new_book method successfully adding multiple books (2).

- **test_set_book_rating_rating_between_1_and_10:** test set_book_rating method successfully setting existing rating (between 1 and 10, integer).

- **test_set_book_rating_set_rating_more_than_10:** test set_book_rating method unsuccessfully trying to set rating more than 10.

- **test_get_book_rating_book_in_list:** test get_book_rating method successfully getting rating of a book from the list.

- **test_get_books_with_specific_rating_two_books:** test get_books_with_specific_rating method successfully getting two books with the same rating from the list.

- **test_get_books_rating_three_books:** test get_books_rating method successfully getting dictionary with three added books.

- **test_add_book_in_favorites_add_new_book:** test add_book_in_favorites method successfully adding a book to favorites.

- **test_add_book_in_favorites_book_already_in_favorites:** test add_book_in_favorites method unsuccessfully trying to add a book which is already in favorites.

- **test_delete_book_from_favorites_book_in_favorites:** test delete_book_from_favorites method successfully deleting a book from favorites.

- **test_get_list_of_favorites_books_list_of_two_books:** test get_list_of_favorites_books method successfully getting a list of two books in favorites.

- **test_get_list_of_favorites_books_empty_list:** test get_list_of_favorites_books method unsuccessfully trying to get an empty list of favorites.