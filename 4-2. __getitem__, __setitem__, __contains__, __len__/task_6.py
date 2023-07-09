"""
Реализуйте класс AttrDict, описывающий упрощенный словарь, значения элементов которого можно получать
как по ключам ([key]), так и по одноименным атрибутам (.key).

При создании экземпляра класс должен принимать один аргумент:
    data — словарь, определяющий начальный набор элементов упрощенного словаря.
           Если не передан, начальный набор элементов считается пустым.

При передаче экземпляра класса AttrDict в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса AttrDict должен быть итерируемым объектом,
то есть позволять перебирать свои ключи, например, с помощью цикла for.

Наконец, экземпляр класса AttrDict должен позволять получать значения своих элементов как по их ключам, так и по
одноименным атрибутам. Реализовывать добавление элементов и изменение их значений по одноименным атрибутам не нужно.

Примечание 1. Экземпляр класса AttrDict не должен зависеть от словаря, на основе которого он был создан.
Другими словами, если исходный словарь изменится, то экземпляр класса AttrDict измениться не должен.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса AttrDict нет, она может быть произвольной.
"""


class AttrDict:
    def __init__(self, data=()):
        self._data = dict(data) or {}

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getattr__(self, key):
        return self._data[key]

    def __iter__(self):
        yield from self._data


if __name__ == '__main__':

    d = AttrDict()
    d.name = 'Leonardo da Vinci'

    try:
        print(d['name'])
    except KeyError:
        print('Ключ отсутствует')

    print('-' * 15)

    attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})

    attrdict['city'] = 'Dubai'
    attrdict['age'] = 31
    print(attrdict.city)
    print(attrdict.age)

    print('-' * 15)

    attrdict = AttrDict({'name': 'X Æ A-12', 'father': 'Elon Musk'})

    print(attrdict['name'])
    print(attrdict.father)
    print(len(attrdict))
