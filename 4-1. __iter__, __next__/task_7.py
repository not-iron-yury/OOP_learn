"""
Реализуйте класс SkipIterator.

При создании экземпляра класс должен принимать два аргумента в следующем порядке:
    iterable — итерируемый объект
    n — целое неотрицательное число

Экземпляр класса SkipIterator должен являться итератором, который генерирует элементы итерируемого объекта iterable,
пропуская по n элементов, а затем возбуждает исключение StopIteration.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Класс SkipIterator должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__().
Реализация же протокола может быть произвольной.
"""
from itertools import islice
class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = islice(iterable, 0, None, n+1)
        # self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)


if __name__ == '__main__':

    skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
    print(*skipiterator)

    skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
    print(*skipiterator)

    skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
    print(*skipiterator)