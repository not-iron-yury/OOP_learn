"""
Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:

radius — радиус круга
Экземпляр класса Circle должен иметь один атрибут:

radius — радиус круга
Класс Circle должен иметь один метод класса:

from_diameter() — метод, принимающий в качестве аргумента диаметр круга и возвращающий экземпляр класса Circle,
созданный на основе переданного диаметра
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diametr):
        if cls.validator(diametr):
            return cls(diametr / 2)

    @staticmethod
    def validator(value):
        return isinstance(value, int)


if __name__ == '__main__':
    circle = Circle.from_diameter(10)
    print(circle.radius)

    print('-' * 15)

    circle = Circle(5)
    print(circle.radius)
