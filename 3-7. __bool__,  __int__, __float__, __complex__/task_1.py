"""
Реализуйте класс Vector, описывающий вектор на плоскости.

При создании экземпляра класс должен принимать два аргумента в следующем порядке:
    x — координата вектора по оси x
    y — координата вектора по оси y

Экземпляр класса Vector должен иметь следующее неформальное строковое представление:
    (<координата x>, <координата y>)

Также экземпляр класса Vector должен поддерживать приведение к типам bool, int, float и complex:
    1) при приведении к типу bool значением вектора должно являться значение True,
    если хотя бы одна его координата не равна нулю, или False в противном случае;
    2) при приведении к типу int значением вектора должен являться его модуль в виде целого числа
    с отброшенной дробной частью;
    3) при приведении к типу float значением вектора должен являться его модуль в виде вещественного числа;
    4) при приведении к типу complex значением вектора должно являться комплексное число,
    вещественная часть которого равна координате вектора по оси y.
"""


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.vector_value = (x ** 2 + y ** 2) ** 0.5

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        return self.vector_value != 0

    def __int__(self):
        return int(self.vector_value)

    def __float__(self):
        return float(self.vector_value)

    def __complex__(self):
        return complex(int(self.x), int(self.y))


if __name__ == '__main__':
    vector = Vector(3, 4)

    print(vector)
    print(int(vector))
    print(float(vector))
    print(complex(vector))

    print('-' * 15)

    print(bool(Vector(1, 2)))
    print(bool(Vector(1, 0)))
    print(bool(Vector(0, 1)))
    print(bool(Vector(0, 0)))
