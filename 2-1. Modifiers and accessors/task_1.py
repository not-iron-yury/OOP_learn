"""
Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:

radius — радиус круга
Экземпляр класса Circle должен иметь три атрибута:

_radius — радиус круга
_diameter — диаметр круга
_area — площадь круга
Класс Circle должен иметь три метода экземпляра:

get_radius() — метод, возвращающий радиус круга
get_diameter() — метод, возвращающий диаметр круга
get_area() — метод, возвращающий площадь круга
"""

from math import pi


class Circle:
    def __init__(self, radius: int):
        if type(radius) is int:
            self._radius = radius
            self._diameter = radius * 2
            self._area = pi * (radius ** 2)
        else:
            raise ValueError('Введите целое число')

    def get_radius(self) -> int:
        """Возвращает радиус круга"""
        return self._radius

    def get_diameter(self) -> int:
        """Возвращает диаметр круга"""
        return self._diameter

    def get_area(self) -> int:
        """Возвращает площадь круга"""
        return self._area


circle = Circle(5)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))
