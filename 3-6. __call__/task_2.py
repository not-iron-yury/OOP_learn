"""
Реализуйте класс RaiseTo, экземпляры которого позволяют возводить числа в фиксированную степень.
При создании экземпляра класс должен принимать один аргумент:
degree — показатель степени

Экземпляр класса RaiseTo должен являться вызываемым объектом и принимать один аргумент:
x — число

Экземпляр класса RaiseTo должен возвращать значение x в степени degree.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса RaiseTo нет, она может быть произвольной.
"""


class RaiseTo:

    def __init__(self, degree):
        self.degree = degree

    def __call__(self, x):
        return x ** self.degree


if __name__ == '__main__':
    raise_to_two = RaiseTo(2)

    print(raise_to_two(2))
    print(raise_to_two(3))
    print(raise_to_two(4))

    print('-' * 15)

    raise_to_three = RaiseTo(3)
    raise_to_four = RaiseTo(4)

    print(raise_to_three(3))
    print(raise_to_four(2))
