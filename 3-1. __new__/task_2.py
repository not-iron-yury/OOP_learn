"""
Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:

a = SingletonFive(<наименование>)
Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.

Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.)
должны быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive
"""


class SingletonFive:
    __count = 0
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__count += 1
            cls.__instance = object.__new__(cls)
            return cls.__instance
        return cls.__instance

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    objs = [SingletonFive(str(n)) for n in range(10)]

    [print(id(i)) for i in objs]


