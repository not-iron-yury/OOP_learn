"""
Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Formatter должен иметь один статический метод:

format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict
и выводящий информацию о переданном объекте в формате, зависящем от его типа.

Если переданный объект принадлежит какому-либо другому типу,
должно быть возбуждено исключение TypeError с текстом: Аргумент переданного типа не поддерживается

Примечание 1. Примеры форматирования объектов всех типов показаны в тестовых данных.

Примечание 2. Обратите внимание, что метод format() должен обрамлять апострофами строковые элементы коллекций.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса Formatter нет, она может быть произвольной.
"""

from functools import singledispatchmethod


class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(val):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def _from_int(val):
        print(f'Целое число: {val}')

    @format.register(float)
    @staticmethod
    def _from_float(val):
        print(f'Вещественное число: {val}')

    @format.register(list)
    @staticmethod
    def _from_list(val):
        values = ', '.join([f"\'{i}\'" if type(i) == str else str(i) for i in val])
        print(f"Элементы списка: {values}")

    @format.register(tuple)
    @staticmethod
    def _from_tuple(val):
        values = ', '.join([f"\'{i}\'" if type(i) == str else str(i) for i in val])
        print(f'Элементы кортежа: {values}')

    @format.register(dict)
    @staticmethod
    def _from_dict(val):
        print('Пары словаря: ' + ', '.join([str(i) for i in val.items()]))


if __name__ == '__main__':
    Formatter.format(1337)  # Целое число: 1337
    Formatter.format(20.77)  # Вещественное число: 20.77
    Formatter.format([10, 20, 30, 40, 50])  # Элементы списка: 10, 20, 30, 40, 50
    Formatter.format([10, 20, '30', '40', 50])  # Элементы списка: 10, 20, '30', '40', 50
    Formatter.format(([1, 3], [2, 4, 6]))  # Элементы кортежа: [1, 3], [2, 4, 6]
    Formatter.format(([1, '3'], [2, '4', 6]))  # Элементы кортежа: [1, 3], [2, 4, 6]
    Formatter.format({'Cuphead': 1, 'Mugman': 3})  # Пары словаря: ('Cuphead', 1), ('Mugman', 3)
    Formatter.format({1: 'one', 2: 'two'})  # Пары словаря: (1, 'one'), (2, 'two')
    Formatter.format({1: True, 0: False})  # Пары словаря: (1, True), (0, False)
    try:
        Formatter.format('All them years, Dutch, for this snake?')
    except TypeError as e:
        print(e)  # Аргумент переданного типа не поддерживается
