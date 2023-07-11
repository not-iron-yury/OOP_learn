"""
Вам доступен класс Processor. При создании экземпляра класс не принимает никаких аргументов.

class Processor:
    @staticmethod
    def process(data):
        if isinstance(data, (int, float)):
            return data * 2
        elif isinstance(data, str):
            return data.upper()
        elif isinstance(data, list):
            return sorted(data)
        elif isinstance(data, tuple):
            return tuple(sorted(data))
        raise TypeError('Аргумент переданного типа не поддерживается')

Класс Processor имеет один статический метод:
process() — метод, который принимает в качестве аргумента произвольный объект,
преобразует его в зависимости от его типа и возвращает полученный результат.

Если тип переданного объекта не поддерживается методом, возбуждается исключение TypeError с текстом:
Аргумент переданного типа не поддерживается

Перепишите метод process() класса Processor с использованием декоратора @singledispatchmethod,
чтобы он выполнял ту же задачу.
"""

from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(int)
    @process.register(float)
    @staticmethod
    def _from_int_float(data):
        return data * 2

    @process.register(str)
    @staticmethod
    def _from_str(data):
        return data.upper()

    @process.register(list)
    @staticmethod
    def _from_list(data):
        return sorted(data)

    @process.register(tuple)
    @staticmethod
    def _from_tuple(data):
        return tuple(sorted(data))


if __name__ == '__main__':
    print(Processor.process(10))  # 20
    print(Processor.process(5.2))  # 10.4
    print(Processor.process('hello'))  # HELLO
    print(Processor.process((4, 3, 2, 1)))  # (1, 2, 3, 4)
    print(Processor.process([3, 2, 1]))  # [1, 2, 3]

    try:
        Processor.process({1, 2, 3})
    except TypeError as e:
        print(e)  # Аргумент переданного типа не поддерживается
