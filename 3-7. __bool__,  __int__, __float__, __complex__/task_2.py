"""
Реализуйте класс Temperature, описывающий температуру в градусах по шкале Цельсия.

При создании экземпляра класс должен принимать один аргумент:
    temperature — температура в градусах по шкале Цельсия

Класс Temperature должен иметь один метод экземпляра:
    to_fahrenheit() — метод, возвращающий температуру по шкале Фаренгейта

Класс Temperature должен иметь один метод класса:
    from_fahrenheit() — метод, принимающий в качестве аргумента температуру по шкале Фаренгейта
    и возвращающий экземпляр класса Temperature, созданный на основе переданной температуры.

Экземпляр класса Temperature должен иметь следующее неформальное строковое представление:
    <температура в градусах по шкале Цельсия с округлением до двух знаков после запятой>°C

Также экземпляр класса Temperature должен поддерживать приведение к типам bool, int и float:
    1) при приведении к типу bool значением экземпляра класса Temperature должно являться значение True,
    если его температура выше нуля, или False в противном случае;
    2) при приведении к типу int значением экземпляра класса Temperature должна являться его температура
    в виде целого числа с отброшенной дробной частью;
    3) при приведении к типу float значением экземпляра класса Temperature должна являться его температура
    в виде вещественного числа.

Примечание 1. Перевести температуру из шкалы Фаренгейта в шкалу Цельсия позволяет формула:
    tC = (tF - 32) * 5/9, tC — температура в градусах по шкале Цельсия, tF — температура в градусах по шкале Фаренгейта.
    tF = (tC * 9/5) + 32

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Temperature нет, она может быть произвольной.
"""


class Temperature:
    def __init__(self, tC: int | float):
        self.tC = tC

    def to_fahrenheit(self) -> int | float:
        return (self.tC * 9 / 5) + 32

    @classmethod
    def from_fahrenheit(cls, tF: int | float):
        return Temperature((tF - 32) * 5 / 9)

    def __repr__(self):
        return f"{self.tC.__round__(2)}°C"

    def __bool__(self):
        return 0 < self.tC

    def __int__(self):
        return int(self.tC)

    def __float__(self):
        return float(self.tC)


if __name__ == '__main__':
    t = Temperature(5.5)
    print(t)
    print(str(t) == '5.5°C')
    print(int(t) == 5)
    print(float(t) == 5.5)
    print(t.to_fahrenheit() == 41.9)

    print('-' * 15)

    t1 = Temperature(1)
    t2 = Temperature(0)
    t3 = Temperature(-1)

    print(bool(t1) == True)
    print(bool(t2) == False)
    print(bool(t3) == False)
