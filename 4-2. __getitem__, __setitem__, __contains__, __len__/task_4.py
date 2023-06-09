"""
Реализуйте класс SequenceZip.
При создании экземпляра класс должен принимать произвольное количество позиционных аргументов,
каждый из которых является итерируемым объектом.

Класс SequenceZip должен описывать последовательность, элементами которой являются элементы переданных в конструктор
итерируемых объектов, объединенные в кортежи. Объединение должно происходить аналогично тому,
как это делает функция zip().

При передаче экземпляра класса SequenceZip в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса SequenceZip должен быть итерируемым объектом,
то есть позволять перебирать свои элементы, например, с помощью цикла for.

Наконец, экземпляр класса SequenceZip должен позволять получать значения своих элементов с помощью индексов.

Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.

Примечание 2. Экземпляр класса SequenceZip не должен зависеть от итерируемых объектов, на основе которых он был создан.
Другими словами, если исходные итерируемые объекты изменятся, то экземпляр класса SequenceZip измениться не должен.

Примечание 3. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса SequenceZip нет, она может быть произвольной.
"""

from copy import deepcopy
from itertools import islice


class SequenceZip:
    def __init__(self, *args):
        self.data = deepcopy(zip(*args))

    def __len__(self):
        return sum(1 for _ in deepcopy(self.data))

    def __getitem__(self, item):
        return next(islice(deepcopy(self.data), item, item + 1))

    def __iter__(self):
        yield from deepcopy(self.data)


if __name__ == '__main__':
    many_large_sequences = [range(100000) for _ in range(100)]
    sequencezip = SequenceZip(*many_large_sequences)
    print(len(sequencezip))
    print(len(sequencezip))
    print(sequencezip[99999])
    print(sequencezip[99999])
