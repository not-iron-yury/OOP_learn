"""
Реализуйте класс Ord. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса Ord должен выступать в качестве альтернативы функции ord().

При обращении к атрибуту экземпляра, именем которого является одиночный символ,
должна возвращаться его позиция в таблице символов Unicode.
"""

class Ord:
    def __getattr__(self, item):
        return ord(item)


if __name__ == '__main__':

    obj = Ord()

    print(obj.a)
    print(obj.b)