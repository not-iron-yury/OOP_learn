"""
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен.
При создании экземпляра класс должен принимать три аргумента в следующем порядке:
a — коэффициент a квадратного трехчлена
b — коэффициент b квадратного трехчлена
c — коэффициент c квадратного трехчлена

Экземпляр класса QuadraticPolynomial должен иметь три атрибута:
a — коэффициент a квадратного трехчлена
b — коэффициент b квадратного трехчлена
c — коэффициент c квадратного трехчлена


Класс QuadraticPolynomial должен иметь два метода класса:

from_iterable() — метод, принимающий в качестве аргумента итерируемый объект из трех элементов a, b и c,
которые представляют коэффициенты квадратного трехчлена, и возвращающий экземпляр класса QuadraticPolynomial,
созданный на основе переданных коэффициентов.

from_str() — метод, принимающий в качестве аргумента строку,
которая содержит коэффициенты a, b и c квадратного трехчлена, записанные через пробел.
Метод должен возвращать экземпляр класса QuadraticPolynomial, созданный на основе переданных коэффициентов,
предварительно преобразованных в экземпляры класса float
"""

from typing import Type

class QuadraticPolynomial:
    def __init__(self, a: int | float, b: int | float, c: int | float):
        self.a, self.b, self.c = a, b, c

    @classmethod
    def from_iterable(cls, data: tuple[int | float] | list[int | float]) -> 'QuadraticPolynomial':
        return cls(*data)

    @classmethod
    def from_str(cls, data: str) -> 'QuadraticPolynomial':
        return cls(*map(float, data.split()))


if __name__ == '__main__':
    polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')
    print(polynom.a)
    print(polynom.b)
    print(polynom.c)
    print(polynom.a + polynom.b + polynom.c)

    print('-' * 15)

    polynom = QuadraticPolynomial.from_iterable([2, 13, -1])
    print(polynom.a)
    print(polynom.b)
    print(polynom.c)

    print('-' * 15)

    polynom = QuadraticPolynomial(1, -5, 6)
    print(polynom.a)
    print(polynom.b)
    print(polynom.c)
