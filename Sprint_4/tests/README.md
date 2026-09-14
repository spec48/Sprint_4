# qa_python Sprint_4
| Название теста | Что проверяет                                                                                     |
|-|---------------------------------------------------------------------------------------------------|
|test_add_new_book_add_two_books_success| Успешное добавление одной и двух книг с разным названием длиной до 40 символов включительно       |
|test_add_new_book_two_identical_books_fail| Невозможно добавление двух книг с одинаковым названием                                            |
|test_add_new_book_41_chars_in_book_fail| Невозможно добавление книги с названием длиной 41 символ                                          |
|test_set_book_genre_success| Успешная установка жанра книги, если книга есть в books_genre и её жанр входит в список genre     |
|test_set_book_genre_not_in_genre_fail| Невозможно установить жанр книги, если книга есть в books_genre и её жанр не входит в список genre |
|test_set_book_genre_name_not_in_books_genre_fail| Невозможно установить жанр книги, если книги нет в books_genre и её жанр входит в список genre    |
|test_get_book_genre_success| Успешное получение жанра книги                                                                    |
|test_get_books_with_specific_genre_success| Успешное получение списка книг с одним жанром                                                     |
|test_get_books_with_specific_genre_fail| Получение пустого списка, если искомый жанр отсутствует в списке genre                            |
|test_get_books_genre_success| Успешное получение текущего словаря books_genre                                                   |
|test_get_books_for_children_success| Добавление в список книг без возврастного рейтинга                                                |
|test_add_book_in_favorites_success| Добавление книги в избранное, если книга находится в словаре books_genre                          |
|test_add_book_in_favorites_fail| Невозможно добавление книги в избранное, если книги нет в словаре books_genre                     |
|test_add_book_in_favorites_two_identical_books_fail| Невозможно добавление в избранное двух книг с одинаковым названием                                |
|test_delete_book_from_favorites_success| Удаление книги из избранного, если она там есть                                                   |
|test_delete_book_from_favorites_fail| Невозможно удаление книги из избранного, если ее там нет                                          |
|test_get_list_of_favorites_books_success| Получение списка избранных книг                                                                   