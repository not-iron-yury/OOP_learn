"""
Реализуйте класс RandomLooper.
При создании экземпляра класс должен принимать произвольное количество позиционных аргументов,
каждый из которых является итерируемым объектом.

Экземпляр класса RandomLooper должен являться итератором, который генерирует в случайном порядке
все элементы всех итерируемых объектов, переданных в конструктор, а затем возбуждает исключение StopIteration.

Примечание 1. Порядок элементов в возвращаемом итераторе необязательно должен совпадать с их порядком в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс RandomLooper должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__().
Реализация же протокола может быть произвольной.
"""

from itertools import chain
from random import shuffle


class RandomLooper:
    def __init__(self, *args):
        self.data = list(args)
        shuffle(self.data)
        self.data = chain(*self.data)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data)


if __name__ == '__main__':
    randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

    print(list(randomlooper))
    print(list(randomlooper))

    print('-'*15)

    colors = ['red', 'blue', 'green', 'purple']
    shapes = ['square', 'circle', 'triangle', 'octagon']
    randomlooper = RandomLooper(colors, shapes)

    print(list(randomlooper))