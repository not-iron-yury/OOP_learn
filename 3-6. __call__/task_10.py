"""
Реализуйте класс SortKey, описывающий ключ для сортировки объектов на основе значений их определенных атрибутов.
При создании экземпляра класс должен принимать произвольное количество позиционных аргументов,
каждый из которых представляет имя атрибута, участвующего в сортировке.


Чтобы приведенный ниже код:

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]

print(sorted(users, key=SortKey('age')))            # сортировка по age
print(sorted(users, key=SortKey('name', 'age')))    # сортировка по name, а затем по age

выводил:
[User(Arthur, 20), User(Timur, 30), User(Gvido, 67)]
[User(Arthur, 20), User(Gvido, 67), User(Timur, 30)]

"""

class SortKey:
    def __init__(self, *args):
        self.keys = args

    def __call__(self, *args):
        return 


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]

print(sorted(users, key=SortKey('age')))            # [User(Arthur, 20), User(Timur, 30), User(Gvido, 67)]
print(sorted(users, key=SortKey('name', 'age')))    # [User(Arthur, 20), User(Gvido, 67), User(Timur, 30)]
