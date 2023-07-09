"""
Реализуйте класс OrderedSet, описывающий упорядоченное множество.

При создании экземпляра класс должен принимать один аргумент:
    iterable — итерируемый объект, определяющий начальный набор элементов упорядоченного множества.
    Если не передан, начальный набор элементов считается пустым.

Класс OrderedSet должен иметь два метода экземпляра:
    add() — метод, принимающий в качестве аргумента произвольный объект
            и добавляющий его в конец упорядоченного множества
    discard() — метод, принимающий в качестве аргумента произвольный объект
            и удаляющий его из упорядоченного множества, если он в нем присутствует

При передаче экземпляра класса OrderedSet в функцию len() должно возвращаться количество элементов в нем.

Помимо этого, экземпляр класса OrderedSet должен быть итерируемым объектом, то есть позволять перебирать свои элементы,
например, с помощью цикла for.

Также экземпляр класса OrderedSet должен поддерживать операцию проверки на принадлежность с помощью оператора in.

Наконец, экземпляры класса OrderedSet должны поддерживать операции сравнения с помощью операторов == и !=.
Методы, реализующие операции сравнения, должны уметь сравнивать как два экземпляра класса OrderedSet между собой,
так и экземпляр класса OrderedSet с экземпляром класса set. Если упорядоченное множество сравнивается с
упорядоченным множеством, они считаются равными в том случае, если они имеют равную длину и содержат равные элементы
на равных позициях. Если упорядоченное множество сравнивается с обычным множеством, они считаются равными в том случае,
если имеют равную длину и содержат равные элементы без учета их расположения.

Примечание 1. Экземпляр класса OrderedSet не должен зависеть от итерируемого объекта, на основе которого он был создан.
Другими словами, если исходный итерируемый объект изменится, то экземпляр класса OrderedSet измениться  не должен.

Примечание 2. Если объект, с которыми происходит сравнение, некорректен, метод, реализующий операцию сравнения,
должен вернуть константу NotImplemented.

Примечание 3. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса OrderedSet нет, она может быть произвольной.
"""


class OrderedSet:
    def __init__(self, iterable=None):
        self.iterable = []
        if iterable != None:
            for obj in iterable:
                self.add(obj)

    def __contains__(self, item):
        return item in self.iterable

    def __len__(self):
        return len(self.iterable)

    def add(self, obj):
        if not self.__contains__(obj):
            self.iterable.append(obj)

    def discard(self, obj):
        if self.__contains__(obj):
            del self.iterable[self.iterable.index(obj)]

    def __iter__(self):
        yield from self.iterable

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return self.iterable == other.iterable
        elif isinstance(other, set):
            return set(self.iterable) == other
        return NotImplemented

    def __hash__(self):
        return hash(tuple(self.iterable))


if __name__ == '__main__':
    orderedset = OrderedSet()

    orderedset.add('green')
    orderedset.add('green')
    orderedset.add('blue')
    orderedset.add('red')
    print(*orderedset)
    orderedset.discard('blue')
    orderedset.discard('white')
    print(*orderedset)
    print(hash(orderedset))

    print('-' * 15)

    orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

    print(*orderedset)
    print(len(orderedset))

    print('-' * 15)

    orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

    print('python' in orderedset)
    print('C++' in orderedset)
