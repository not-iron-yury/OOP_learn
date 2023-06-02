"""
 Объявите три класса геометрических фигур: Line, Rect, Ellipse.
 Должна быть возможность создавать объекты каждого класса следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)
В качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные числа).
В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый)
в виде кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов:
для каждого текущего объекта класс выбирается случайно (или Line, или Rect, или Ellipse).
Координаты также генерируются случайным образом (числовые значения). Все объекты сохраните в списке elements.

В списке elements обнулите координаты объектов только для класса Line.

P.S. На экран в программе ничего выводить не нужно.
"""
from random import choice, randrange


class Line:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


coordinats = [randrange(0, 100) for _ in range(4)]

elements = [choice((Line, Rect, Ellipse))(*coordinats) for _ in range(217)]

for cls in elements:
    if type(cls) is Line:
        cls.sp, cls.ep = (0, 0), (0, 0)
