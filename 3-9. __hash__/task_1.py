"""
Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости.
При создании экземпляра класс должен принимать три аргумента в следующем порядке:
    x — координата точки по оси x
    y — координата точки по оси y
    color — цвет точки

Класс ColoredPoint должен иметь три свойства:
    x — свойство, доступное только для чтения, возвращающее координату точки по оси x
    y — свойство, доступное только для чтения, возвращающее координату точки по оси y
    color — свойство, доступное только для чтения, возвращающее цвет точки
    
Экземпляр класса ColoredPoint должен иметь следующее формальное строковое представление:
    ColoredPoint(<координата x>, <координата y>, '<цвет точки>')

Также экземпляры класса ColoredPoint должны поддерживать между собой операции сравнения
с помощью операторов == и!=. Две цветные точки считаются равными, если их цвета и координаты по обеим осям совпадают.

Наконец, при передаче экземпляра класса ColoredPoint в функцию hash()
должно возвращаться его хеш-значение, вычисленное с помощью функции hash() на основе кортежа,
первым элементом которого является координата точки по оси x, вторым — координата точки по оси y, третьим — цвет точки.

Примечание 1. Если объект, с которым происходит сравнение, некорректен, метод,
реализующий операцию сравнения, должен вернуть константу NotImplemented.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса ColoredPoint нет, она может быть произвольной.
"""


class ColoredPoint:
    def __init__(self, x: int, y: int, color: str) -> None:
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def color(self) -> str:
        return self._color

    def __repr__(self) -> str:
        return f"ColoredPoint({self._x}, {self._y}, {self._color})"

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return (self._x, self._y, self._color) == (other._x, other._y, other._color)
        return NotImplemented

    def __hash__(self):
        return hash((self._x, self._y, self._color))


if __name__ == '__main__':
    point1 = ColoredPoint(1, 2, 'white')
    point2 = ColoredPoint(1, 2, 'white')
    point3 = ColoredPoint(3, 4, 'black')

    print(point1 == point2)
    print(hash(point1) == hash(point2))
    print(point1 == point3)
    print(hash(point1) == hash(point3))

    print('-' * 15)

    points = {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}
    print(points)

    print('-' * 15)

    point = ColoredPoint(1, 2, 'white')

    try:
        point.color = 'black'
    except AttributeError as e:
        print('Error')
