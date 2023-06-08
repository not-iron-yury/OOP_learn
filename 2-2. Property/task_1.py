"""
Реализуйте класс Rectangle, описывающий прямоугольник.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

length — длина прямоугольника
width — ширина прямоугольника
Экземпляр класса Rectangle должен иметь два атрибута:

length — длина прямоугольника
width — ширина прямоугольника
Класс Rectangle должен иметь два свойства:

perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
area — свойство, доступное только для чтения, возвращающее площадь прямоугольника.

При изменении сторон прямоугольника должны изменяться его периметр и площадь.
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (self.length + self.width) * 2

    perimeter = property(get_perimeter)
    area = property(get_area)


if __name__ == '__main__':

    rectangle1 = Rectangle(4, 5)
    print(rectangle1.length)
    print(rectangle1.width)
    print(rectangle1.perimeter)
    print(rectangle1.area)
    print('-------------------')

    rectangle2 = Rectangle(4, 5)

    rectangle2.length = 2
    rectangle2.width = 3
    print(rectangle2.length)
    print(rectangle2.width)
    print(rectangle2.perimeter)
    print(rectangle2.area)
