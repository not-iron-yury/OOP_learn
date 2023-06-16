"""
Реализуйте класс Month, описывающий месяц.

При создании экземпляра класс должен принимать два аргумента в следующем порядке:
year — год
month — порядковый номер месяца

Экземпляр класса Month должен иметь следующее формальное строковое представление:
Month(<год>, <порядковый номер месяца>)

И следующее неформальное строковое представление:
<год>-<порядковый номер месяца>

Также экземпляры класса Month должны поддерживать все операции сравнения
с помощью операторов ==, !=, >, <, >=, <=.

Два Month объекта считаются равными, если их годы и порядковые номера месяцев совпадают.

Month объект считается больше другого Month объекта, если его год больше. В случае если два Month объекта
имеют равные года, большим считается тот, чей месяц больше. Методы, реализующие операции сравнения,
должны уметь сравнивать как два Month объекта между собой, так и Month объект с кортежем из двух чисел,
представляющих год и месяц.
"""
from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year, month):
        self.year, self.month = year, month

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __eq__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) == (other.year, other.month)
        elif isinstance(other, tuple):
            return (self.year, self.month) == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) < (other.year, other.month)
        elif isinstance(other, tuple):
            return (self.year, self.month) < other
        return NotImplemented


if __name__ == '__main__':
    print(Month(1999, 12) == Month(1999, 12))  # True
    print(Month(1999, 12) < Month(2000, 1))  # True
    print(Month(1999, 12) > Month(2000, 1))  # False
    print(Month(1999, 12) <= Month(1999, 12))  # True
    print(Month(1999, 12) >= Month(2000, 1))  # False

    print('-' * 15)

    months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]
    print(sorted(months))  # [Month(1998, 12), Month(1999, 12), Month(2000, 1)]

    print('-' * 15)

    months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

    print(min(months))  # 1998-12
    print(max(months))  # 2000-1

    print('-' * 15)

    print(Month(1999, 12) == (1999, 12))
    print(Month(1999, 12) < (2000, 1))
    print(Month(1999, 12) > (2000, 1))
    print(Month(1999, 12) <= (1999, 12))
    print(Month(1999, 12) >= (2000, 1))