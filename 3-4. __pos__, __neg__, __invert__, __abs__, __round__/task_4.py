"""
Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости.
При создании экземпляра класс должен принимать три аргумента в следующем порядке:
x — координата точки по оси x
y — координата точки по оси y
color — цвет в формате RGB, в виде кортежа из трех целых чисел в диапазоне [0; 255], значение по умолчанию (0, 0, 0)


Экземпляр класса ColoredPoint должен иметь три атрибута:
x — координата точки по оси x
y — координата точки по оси y
color — цвет в формате RGB, представленный кортежем из трех целых чисел от 0 до 255

Также экземпляр класса ColoredPoint должен иметь следующее формальное строковое представление:
ColoredPoint(<координата x>, <координата y>, <цвет точки в виде трехэлементного кортежа>)

И следующее неформальное строковое представление:
(<координата x>, <координата y>)

Наконец, экземпляр класса ColoredPoint должен поддерживать унарные операторы +, - и ~:

результатом унарного + должен являться новый экземпляр класса ColoredPoint c исходными координатами и цветом
результатом унарного - должен являться новый экземпляр класса ColoredPoint c координатами,
умноженными на минус единицу, и исходным цветом
результатом унарного ~ должен являться новый экземпляр класса ColoredPoint c координатами,
переставленными местами, и инвертированным цветом: значение каждой компоненты цвета отнимается от 255

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса ColoredPoint нет, она может быть произвольной.
"""

from typing import Type


class ColoredPoint:
    def __init__(self, x: int, y: int, color: tuple = (0, 0, 0)) -> None:
        self.x, self.y = x, y
        self.color = color

    def __repr__(self) -> str:
        return f"ColoredPoint({self.x}, {self.y}, {self.color})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __pos__(self) -> Type['ColoredPoint']:
        return __class__(self.x, self.y, self.color)

    def __neg__(self) -> Type['ColoredPoint']:
        return __class__(-self.x, -self.y, self.color)

    def __invert__(self) -> Type['ColoredPoint']:
        a, b, c = self.color
        return __class__(self.y, self.x, (255 - a, 255 - b, 255 - c))


if __name__ == '__main__':
    point = ColoredPoint(2, -3)
    print(+point)  # (2, -3)
    print(-point)  # (-2, 3)
    print(~point)  # (-3, 2)

    print('-' * 15)

    point1 = ColoredPoint(2, -3)
    point2 = ColoredPoint(10, 20, (34, 45, 67))

    print(point1.color)  # (0, 0, 0)
    print(point2.color)  # (34, 45, 67)
