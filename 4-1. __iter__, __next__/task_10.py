"""
Реализуйте класс LoopTracker.

При создании экземпляра класс должен принимать один аргумент:
iterable — итерируемый объект

Экземпляр класса LoopTracker должен являться итератором, который генерирует элементы итерируемого объекта iterable
в исходном порядке, а затем возбуждает исключение StopIteration.

Класс LoopTracker должен иметь четыре свойства:
    1) accesses — свойство, доступное только для чтения,
    возвращающее количество элементов, сгенерированных итератором на данный момент

    2) empty_accesses — свойство, доступное только для чтения,
    возвращающее количество попыток получить следующий элемент опустевшего итератора

    3) first — свойство, доступное только для чтения,
    возвращающее первый элемент итератора и не сдвигающее его.

    Если итератор не имеет первого элемента, то есть создан на основе пустого итерируемого объекта,
    то должно быть возбуждено исключение AttributeError с текстом: Исходный итерируемый объект пуст

    4) last — свойство, доступное только для чтения,
    возвращающее последний элемент, сгенерированный итератором на данный момент.

    Если итератор еще не сгенерировал ни одного элемента, то должно быть возбуждено исключение AttributeError с текстом:
    Последнего элемента нет

Класс LoopTracker должен иметь один метод экземпляра:
    is_empty() — метод, возвращающий True, если итератор опустошен, или False в противном случае

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Класс LoopTracker должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__().
Реализация же протокола может быть произвольной.
"""




class LoopTracker:
    def __init__(self, iterable):
        self._iterable = tuple(iterable)
        self._it = iter(iterable)
        self._count = 0
        self._last_elem = None
        self._attempt = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._count == len(self._iterable):
            self._attempt += 1
            raise StopIteration
        self._last_elem = next(self._it)
        self._count += 1
        return self._last_elem

    @property
    def accesses(self):
        return self._count

    @property
    def empty_accesses(self):
        return self._attempt

    @property
    def first(self):
        if not self._iterable:
            raise AttributeError('Исходный итерируемый объект пуст')
        return self._iterable[0]

    @property
    def last(self):
        if self._last_elem is None:
            raise AttributeError('Последнего элемента нет')
        return self._last_elem

    def is_empty(self):
        return True if self._count == len(self._iterable) else False


if __name__ == '__main__':
    loop_tracker = LoopTracker([1, 2, 3])

    print(next(loop_tracker))
    print(loop_tracker.last)

    print(next(loop_tracker))
    print(loop_tracker.last)

    print(next(loop_tracker))
    print(loop_tracker.last)
