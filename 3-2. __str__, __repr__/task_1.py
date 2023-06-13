"""
Требуется реализовать класс Book, описывающий книгу.
При создании экземпляра класс должен был принимать три аргумента в следующем порядке:

title — название книги
author — автор книги
year — год выпуска книги

Предполагается, что экземпляры класса Book будут иметь следующее формальное строковое представление:
Book('<название книги>', '<автор книги>', <год выпуска книги>)

И следующее неформальное строковое представление:
<название книги> (<автор книги>, <год выпуска книги>)
"""


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.author}, {self.year})"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


if __name__ == '__main__':
    book = Book('Изучаем Python', 'Марк Лутц', 2021)
    print(book)  # Изучаем Python (Марк Лутц, 2021)
    print(repr(book))  # Book('Изучаем Python', 'Марк Лутц', 2021)
    print('-' * 15)
    book = Book('Программируем на Python', 'Майкл Доусон', 2023)
    print(str(book))  # Программируем на Python (Майкл Доусон, 2023)
    print(repr(book))  # Book('Программируем на Python', 'Майкл Доусон', 2023)
