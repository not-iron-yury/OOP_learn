"""
Реализуйте класс MutableString, описывающий изменяемую строку.

При создании экземпляра класс должен принимать один аргумент:
    string — строка, определяющая начальное значение изменяемой строки. Если не передана, строка считается пустой

Класс MutableString должен иметь два метода экземпляра:
    lower() — метод, переводящий все символы изменяемой строки в нижний регистр
    upper() — метод, переводящий все символы изменяемой строки в верхний регистр

Экземпляр класса MutableString должен иметь неформальное строковое представление в следующем виде:
    <текущее значение изменяемой строки>

Также экземпляр класса MutableString должен иметь формальное строковое представление в следующем виде:
    MutableString('<текущее значение изменяемой строки>')

При передаче экземпляра класса MutableString в функцию len() должно возвращаться количество символов в нем.

Помимо этого, экземпляр класса MutableString должен быть итерируемым объектом, т.е. позволять перебирать свои символы,
например, с помощью цикла for.

Также экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью
индексов, причем как положительных, так и отрицательных. Экземпляр класса MutableString должен поддерживать полноценные
срезы, результатами которых должны быть новые изменяемые строки.

Наконец, экземпляры класса MutableString должны поддерживать между собой операцию сложения с помощью оператора +,
результатом которой должен являться новый экземпляр класса MutableString, представляющий конкатенацию исходных.

Примечание 1. Реализация класса MutableString может быть произвольной, требований к наличию определенных атрибутов нет.

Примечание 2. Дополнительная проверка данных на корректность в методах не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""


class MutableString:
    def __init__(self, string=''):
        self.string = list(string)

    def lower(self):
        self.string = list(map(str.lower, self.string))

    def upper(self):
        self.string = list(map(str.upper, self.string))

    def __iter__(self):
        return iter(self.string)

    def __str__(self):
        return ''.join(self.string)

    def __repr__(self):
        return f"MutableString('{self.__str__()}')"

    def __len__(self):
        return len(self.string)

    def __check_index(self, index):
        len_ = self.__len__()
        return -(len_ + 1) < index < len_

    def __getitem__(self, index):
        if isinstance(index, slice):
            return MutableString(self.__str__()[index])
        elif self.__check_index(index):
            return self.string[index]
        raise IndexError

    def __setitem__(self, index, value):
        self.string[index] = value
        self.string = list(self.__str__())

    def __delitem__(self, index):
        if isinstance(index, slice):
            del self.string[index]
        elif self.__check_index(index):
            del self.string[index]

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(self.__str__() + other.__str__())


if __name__ == '__main__':
    # mutablestring = MutableString('beegeek')
    #
    # s1 = mutablestring[2:]
    # s2 = mutablestring[:5]
    # s3 = mutablestring[2:5:2]
    #
    # print(s1, type(s1))
    # print(s2, type(s2))
    # print(s3, type(s3))

    mutablestring = MutableString('beegeek')
    print(mutablestring)
    mutablestring[3] = 'ab'
    print(list(mutablestring))

    mutablestring[2:] = 'geek'
    print(list(mutablestring))
    #
    # mutablestring = MutableString('beegeek')
    #
    # del mutablestring[2:5]
    # del mutablestring[1:5:2]
    # print(mutablestring)
    #
    # mutablestring = MutableString('beegeek')
    # print(mutablestring[-7])
    # mutablestring[3] = 'X'
    # print(*mutablestring)
    # print(str(mutablestring))
    # print(repr(mutablestring))
    # print(len(mutablestring))
    # print(mutablestring[2:5])
    #
    # mutablestring1 = MutableString('bee')
    # mutablestring2 = MutableString('geek')
    #
    # print(mutablestring1 + mutablestring2)
    # print(mutablestring2 + mutablestring1)
