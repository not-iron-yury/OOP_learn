"""
Реализуйте класс User, описывающий интернет-пользователя.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — имя пользователя. Если name не является непустой строкой, состоящей только из букв,
должно быть возбуждено исключение ValueError с текстом:
Некорректное имя
age — возраст пользователя. Если age не является целым числом, принадлежащим отрезку [0; 110],
должно быть возбуждено исключение ValueError с текстом:
Некорректный возраст
Экземпляр класса User должен иметь два атрибута:

_name — имя пользователя
_age — возраст пользователя
Класс User должен иметь четыре метода экземпляра:

get_name() — метод, возвращающий имя пользователя
set_name() — метод, принимающий в качестве аргумента значение new_name и изменяющий имя пользователя на new_name.
Если new_name не является непустой строкой, состоящей только из букв,
должно быть возбуждено исключение ValueError с текстом: Некорректное имя
get_age() — метод, возвращающий возраст пользователя
set_age() — метод, принимающий в качестве аргумента значение new_age и изменяющий возраст пользователя на new_age.
Если new_age не является целым числом, принадлежащим отрезку [0; 110],
должно быть возбуждено исключение ValueError с текстом: Некорректный возраст
"""


class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self) -> str:
        """Возвращает имя пользователя"""
        return self._name

    def set_name(self, new_name: str) -> None:
        """Изменяет имя пользователя, либо возбуждает исключение"""
        if not (isinstance(new_name, str) and len(new_name) > 0 and new_name.isalpha()):
            raise ValueError('Некорректное имя')
        self._name = new_name

    def get_age(self) -> int:
        """Возвращает возраст пользователя"""
        return self._age

    def set_age(self, new_age: int) -> None:
        """Изменяет возраст пользователя, либо возбуждает исключение"""
        if not (isinstance(new_age, int) and -1 < new_age < 111):
            raise ValueError('Некорректный возраст')
        self._age = new_age


if __name__ == '__main__':
    user1 = User('Гвидо', 67)

    print(user1.get_name())
    print(user1.get_age())
    print("---------------------")
    user2 = User('Гвидо', 67)

    user2.set_name('Тимур')
    user2.set_age(30)

    print(user2.get_name())
    print(user2.get_age())
    print("---------------------")
    user3 = User('Гвидо', 67)
    try:
        user3.set_name('Т1мур')
        user3.set_age(30)
    except ValueError as e:
        print(e)
    print("---------------------")
    user4 = User('Гвидо', 67)
    try:
        user4.set_age(130)
    except ValueError as e:
        print(e)
