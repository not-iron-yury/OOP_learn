"""
Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case и Upper Camel Case.
При создании экземпляра класс не должен принимать никаких аргументов.

Класс CaseHelper должен иметь четыре статических метода:

is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True,
если переданная строка записана в стиле Snake Case, или False в противном случае.

is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True,
если переданная строка записана в стиле Upper Camel Case, или False в противном случае.

to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case,
записывает ее в стиле Snake Case и возвращает полученный результат.

to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case,
записывает ее в стиле Upper Camel Case и возвращает полученный результат.

"""

from re import fullmatch


class CaseHelper:
    @staticmethod
    def is_snake(string: str) -> bool:
        return bool(fullmatch('[a-z_]+', string))

    @staticmethod
    def is_upper_camel(string: str) -> bool:
        return bool(fullmatch('([A-Z][a-z]+)+', string))

    @staticmethod
    def to_snake(string: str) -> str:
        pass  # sub

    @staticmethod
    def to_upper_camel(string: str) -> str:
        pass  # split


if __name__ == '__main__':
    print(CaseHelper.is_snake('beegeek'))
    print(CaseHelper.is_snake('bee_geek'))
    print(CaseHelper.is_snake('Beegeek'))
    print(CaseHelper.is_snake('BeeGeek'))
    print('-' * 15)
    print(CaseHelper.is_upper_camel('beegeek'))
    print(CaseHelper.is_upper_camel('bee_geek'))
    print(CaseHelper.is_upper_camel('Beegeek'))
    print(CaseHelper.is_upper_camel('BeeGeek'))
    print('-' * 15)
    print(CaseHelper.to_snake('Beegeek'))
    print(CaseHelper.to_snake('BeeGeek'))
    print('-' * 15)
    print(CaseHelper.to_upper_camel('beegeek'))
    print(CaseHelper.to_upper_camel('bee_geek'))
