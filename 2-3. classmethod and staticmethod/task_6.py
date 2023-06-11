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

class CaseHelper:
    @staticmethod
    def is_snake(string: str) -> bool:
