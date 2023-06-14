"""
Реализуйте класс AnyClass. При создании экземпляра класс должен принимать произвольное количество именованных
аргументов и устанавливать их в качестве атрибутов создаваемому экземпляру.

Экземпляр класса AnyClass должен иметь следующее формальное строковое представление:
AnyClass(<имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...)

И следующее неформальное строковое представление:
AnyClass: <имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...

Примечание 1. Обратите внимание, что в формальном строковом представлении значения атрибутов,
которые принадлежат типу str, должны быть обрамлены апострофами.

Примечание 2. Никаких ограничений касательно реализации класса AnyClass нет, она может быть произвольной.
"""


class AnyClass:
    def __init__(self, **kwargs):
         self.__dict__ = kwargs

    def __repr__(self):
        return f"AnyClass({self._representation()})"

    def __str__(self):
        return f"AnyClass: {self._representation()}"

    def _representation(self):
        return ', '.join([f"{name}={repr(value)}" for name, value in self.__dict__.items()])


if __name__ == '__main__':
    any = AnyClass()

    print(str(any))  # AnyClass:
    print(repr(any))  # AnyClass()

    print('-' * 15)

    cowboy = AnyClass(name='John', surname='Marston')

    print(str(cowboy))   # AnyClass: name='John', surname='Marston'
    print(repr(cowboy))  # AnyClass(name='John', surname='Marston')

    print('-' * 15)

    obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

    print(str(obj))
    # AnyClass: attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None
    print(repr(obj))
    # AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)
