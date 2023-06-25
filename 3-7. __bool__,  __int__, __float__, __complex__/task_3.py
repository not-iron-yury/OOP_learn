"""
Реализуйте класс RomanNumeral, описывающий число в римской системе счисления.

При создании экземпляра класс должен принимать один аргумент:
    number — число в римской системе счисления. Например, IV

Экземпляр класса RomanNumeral должен иметь следующее неформальное строковое представление:
    <число в римской системе счисления>

Помимо этого, экземпляр класса RomanNumeral должен поддерживать приведение к типу int, при приведении к которому,
значением должно являться целое число в десятичной системе счисления. (которому он соответствует).

Также экземпляры класса RomanNumeral должны поддерживать между собой все операции сравнения
с помощью операторов ==, !=, >, <, >=, <=.

Наконец, экземпляры класса RomanNumeral должны поддерживать между собой операции сложения и вычитания
с помощью операторов + и - соответственно:
    1) результатом сложения должен являться новый экземпляр класса RomanNumeral, представляющий сумму исходных
    2) результатом вычитания должен являться новый экземпляр класса RomanNumeral, представляющий разность исходных

Примечание 1. Гарантируется, что из римского числа всегда вычитается строго меньшее римское число.

Примечание 2. Подробнее про римскую систему счисления можно почитать по ссылке.

Примечание 3. Не забывайте, что именно константу NotImplemented рекомендуется возвращать в методах, реализующих
арифметические операции или операции сравнения, если эти операции для объектов каких-либо типов не определены.

Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 5. Никаких ограничений касательно реализации класса RomanNumeral нет, она может быть произвольной.
"""


from functools import total_ordering


@total_ordering
class RomanNumeral:
    __INT_ROMAN = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }

    __ROMAN = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
    }

    @staticmethod
    def _int_to_roman(number):
        result = ''
        for n in (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1):
            while n <= number:
                result += RomanNumeral.__INT_ROMAN[n]
                number -= n
        return result

    @staticmethod
    def _roman_to_int(number):
        i, num = 0, 0
        while i < len(number):
            if i + 1 < len(number) and number[i:i + 2] in RomanNumeral.__ROMAN:
                num += RomanNumeral.__ROMAN[number[i:i + 2]]
                i += 2
            else:
                num += RomanNumeral.__ROMAN[number[i]]
                i += 1
        return num

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __int__(self):
        return RomanNumeral._roman_to_int(self.number)

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            num1, num2 = int(self), int(other)
            return RomanNumeral(RomanNumeral._int_to_roman(num1 + num2))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            num1, num2 = int(self), int(other)
            return RomanNumeral(RomanNumeral._int_to_roman(num1 - num2))
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.number == other.number
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral._roman_to_int(self.number) > RomanNumeral._roman_to_int(other.number)
        return NotImplemented
