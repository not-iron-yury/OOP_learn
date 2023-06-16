"""
Реализуйте класс Vector, описывающий вектор на плоскости.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

x — координата вектора по оси x
y — координата вектора по оси y

Экземпляр класса Vector должен иметь следующее формальное строковое представление:
Vector(<координата x>, <координата y>)

Также экземпляры класса Vector должны поддерживать операции сравнения с помощью операторов == и!=.
Два вектора считаются равными, если их координаты по обеим осям совпадают.
Методы, реализующие операции сравнения, должны уметь сравнивать как два вектора между собой,
так и вектор с кортежем из двух чисел, представляющих координаты x и y.
"""

from functools import singledispatchmethod


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"{(__class__.__name__)}({self.x}, {self.y})"

    @singledispatchmethod
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x, self.y == other.x, other.y
        return NotImplemented

    @__eq__.register(tuple)
    def _from_tuple(self, other):
        if len(other) == 2:
            return (self.x, self.y) == other
        return NotImplemented


if __name__ == '__main__':
    vec1 = Vector(4, 7)
    vec2 = Vector(4, 7)
    vec3 = Vector(3, 8)

    print(vec1)
    print(vec1 == vec2)
    print(vec2 == vec3)

    print('-' * 15)

    a = Vector(1, 2)
    pair1 = (1, 2)
    pair2 = (3, 4)
    pair3 = (5, 6, 7)
    pair4 = (1, 2, 3, 4)
    pair5 = (1, 4, 3, 2)

    print(a == pair1)  # True
    print(a == pair2)  # False
    print(a == pair3)  # False
    print(a == pair4)  # False
    print(a == pair5)  # False
