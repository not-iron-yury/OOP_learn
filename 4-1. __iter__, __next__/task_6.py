"""
Реализуйте класс AttrsIterator.

При создании экземпляра класс должен принимать один аргумент:
    obj — произвольный объект

Экземпляр класса AttrsIterator должен являться итератором, который генерирует все атрибуты объекта obj
в виде кортежей из двух элементов, первый из которых представляет имя атрибута, второй — значение атрибута.

Примечание 1. Порядок атрибутов при генерации должен совпадать с их порядком в словаре атрибутов __dict__.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс AttrsIterator должен удовлетворять протоколу итератора,
то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.
"""


class AttrsIterator:
    def __init__(self, obj):
        self.obj = iter(obj.__dict__.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.obj)


if __name__ == '__main__':
    class User:
        def __init__(self, name, surname, age):
            self.name = name
            self.surname = surname
            self.age = age


    user = User('Debbie', 'Harry', 77)

    attrsiterator = AttrsIterator(user)
    print(*attrsiterator)
