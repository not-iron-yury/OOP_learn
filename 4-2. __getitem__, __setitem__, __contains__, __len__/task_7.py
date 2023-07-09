"""
Реализуйте класс PermaDict, описывающий словарь, который позволяет добавлять и удалять пары (<ключ>, <значение>),
но не позволяет изменять значения по уже имеющимся ключам.

При создании экземпляра класс должен принимать один аргумент:
    data — словарь, определяющий начальный набор элементов экземпляра класса PermaDict.
            Если не передан, начальный набор элементов считается пустым.

Класс PermaDict должен иметь три метода экземпляра:
    keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса PermaDict
    values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей экземпляра
    items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра класса PermaDict
              в виде кортежей (<ключ>, <значение>)

При передаче экземпляра класса PermaDict в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса PermaDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи,
например, с помощью цикла for.

Наконец, экземпляр класса PermaDict должен позволять получать значения своих элементов по их ключам,
добавлять новые пары (ключ, значение) и удалять уже имеющиеся с помощью оператора del.

При этом изменение значений по уже имеющимся ключам должно быть недоступно, и при попытке выполнения такой операции
должно возбуждаться исключение KeyError с текстом: Изменение значения по ключу невозможно

Примечание 1. Экземпляр класса PermaDict не должен зависеть от словаря, на основе которого он был создан.
Другими словами, если исходный словарь изменится, то экземпляр класса PermaDict измениться не должен.

Примечание 2. Реализация класса PermaDict может быть произвольной, т.е. требований к наличию определенных атрибутов нет.

Примечание 3. Дополнительная проверка данных на корректность в методах не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""

from copy import copy

class PermaDict:
    def __init__(self, data=()):
        self._data = copy(data) or {}

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def __len__(self):
        return len(self._data.keys())

    def __iter__(self):
        yield from self._data.keys()

    def __getitem__(self, key):
        return self._data.get(key, None)

    def __setitem__(self, key, value):
        if key in self._data:
            raise KeyError('Изменение значения по ключу невозможно')
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]


if __name__ == '__main__':
    permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})

    print(permadict['name'])
    print(len(permadict))

    print('-'*15)

    permadict = PermaDict({'name': 'Timur', 'city': 'Moscow', 'age': 30})

    print(*permadict)
    print(*permadict.keys())
    print(*permadict.values())
    print(*permadict.items())

    print('-'*15)

    permadict = PermaDict()

    permadict['name'] = 'Timur'
    permadict['age'] = 30
    del permadict['name']
    print(permadict['age'])
    print(len(permadict))