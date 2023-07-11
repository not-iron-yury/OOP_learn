"""
Реализуйте класс Person, описывающий человека с использованием декоратора @property.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — имя человека
surname — фамилия человека
Экземпляр класса Person должен иметь два атрибута:

name — имя человека
surname — фамилия человека
Класс Person должен иметь одно свойство:

fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки: <имя> <фамилия>

Примечание 1. При изменении имени и/или фамилии человека должно изменяться и его полное имя.
Аналогично при изменении полного имени должны изменяться имя и фамилия.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()


if __name__ == '__main__':
    person = Person('Меган', 'Фокс')
    print(person.name)
    print(person.surname)
    print(person.fullname)

    print('-' * 15)

    person = Person('Меган', 'Фокс')
    person.name = 'Стефани'
    print(person.fullname)

    print('-' * 15)

    person = Person('Алан', 'Тьюринг')
    person.surname = 'Вирт'
    print(person.fullname)

    print('-' * 15)

    person = Person('Джон', 'Маккарти')

    person.fullname = 'Алан Тьюринг'
    print(person.name)
    print(person.surname)