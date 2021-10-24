# используется для сортировки
from operator import itemgetter


class Book:
    """Книга"""

    def __init__(self, id, name, cost, LibID):
        self.id = id
        self.name = name
        self.cost = cost
        self.LibID = LibID


class Lib:
    """Библиотека"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class LibBook:
    """
    'Книги библиотеки' для реализации
    связи многие-ко-многим
    """

    def __init__(self, libID, bookID):
        self.libID = libID
        self.bookID = bookID


libs = [
    Lib(1, 'Москвоская библиотека'),
    Lib(2, 'Петербургская библиотека'),
    Lib(3, 'библиотека имени Пушкина'),
    # для связи многие-ко-многим:
    Lib(11, 'Новгородская библиотека'),
    Lib(22, 'библиотека имени Лермонтова'),
    Lib(33, 'библиотека имени Толстого'),
]

# Сотрудники
books = [
    Book(1, 'Война и мир', 1000, 1),
    Book(2, 'Капитанская дочка', 200, 2),
    Book(3, 'Богач, бедняк', 600, 2),
    Book(4, 'Преступление и наказание', 500, 3),
    Book(5, 'Гордость и предубеждение', 400, 3),


]

libBooks = [
    LibBook(3, 1),
    LibBook(2, 2),
    LibBook(2, 2),
    LibBook(3, 3),
    LibBook(3, 3),


    LibBook(11, 1),
    LibBook(22, 2),
    LibBook(22, 3),
    LibBook(33, 4),
    LibBook(33, 5),
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(h.name, h.cost, l.name)
                   for l in libs
                   for h in books
                   if h.LibID == l.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(l.name, lb.libID, lb.bookID)
                         for l in libs
                         for lb in libBooks
                         if l.id == lb.libID]

    many_to_many = [(b.name, b.cost, bookName)
                    for bookName, streetID, bookID in many_to_many_temp
                    for b in books if b.id == bookID]

    print('Задание D1')
    res1 = list(filter(lambda x: x[0].endswith("ие"), one_to_many))
    print(res1)

    print('\nЗадание D2')
    res2unsorted = []
    # Перебираем все библиотеки
    for l in libs:
        # Список книг в библиотеке
        bookss = list(filter(lambda i: i[2] == l.name, one_to_many))
        # Если на улице есть дома
        if len(bookss) > 0:
             # Все цены книг в библиотеке
             allCosts = [sal for _, sal, _ in bookss]
             # Средняя цена книги в библиотеке
             averageCosts = round(sum(allCosts) / len(allCosts), 2)
             res2unsorted.append((l.name, averageCosts))

    # Сортировка по средней стоимости
    res2 = sorted(res2unsorted, key=itemgetter(1), reverse=True)
    print(res2)
    print('\nЗадание D3')
    res3 = {}
    for l in libs:
        if l.name.startswith("б"):
            # Список книг в библиотеке
            bookss = list(filter(lambda i: i[2] == l.name, many_to_many))
            # Только имя книг
            booksNames = [x for x, _, _ in bookss]
            # Добавляем результат в словарь
            # ключ - библиотека, значение - список названий книг
            res3[l.name] = booksNames

    print(res3)


if __name__ == '__main__':
    main()

