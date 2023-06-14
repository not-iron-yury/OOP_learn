"""
Реализуйте класс PhoneNumber, описывающий телефонный номер.
При создании экземпляра класс должен принимать один аргумент:

phone_number — телефонный номер, представляющий строку из десяти цифр в одном из следующих форматов:
1) dddddddddd
2) ddd ddd dddd

Экземпляр класса PhoneNumber должен иметь следующее формальное строковое представление:
PhoneNumber('<телефонный номер в формате dddddddddd>')

И следующее неформальное строковое представление:
<телефонный номер в формате (ddd) ddd-dddd>

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса PhoneNumber нет, она может быть произвольной.
"""


class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = phone_number.replace(' ', '')

    def __repr__(self):
        return f"PhoneNumber('{self.phone_number}')"

    def __str__(self):
        return f"({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}"


if __name__ == '__main__':
    phone = PhoneNumber('9173963385')
    print(str(phone))  # (917) 396-3385
    print(repr(phone))  # PhoneNumber('9173963385')

    print('-' * 15)

    phone = PhoneNumber('918 396 3389')
    print(str(phone))  # (918) 396-3389
    print(repr(phone))  # PhoneNumber('9183963389')

    print('-' * 15)

    phone1 = PhoneNumber('9173963385')
    phone2 = PhoneNumber('918 396 3389')
    phone3 = PhoneNumber('919 333 3344')
    print(phone1, phone2, phone3, sep=', ')  # (917) 396-3385, (918) 396-3389, (919) 333-3344
    print([phone1, phone2, phone3])  # [PhoneNumber('9173963385'), PhoneNumber('9183963389'), PhoneNumber('9193333344')]
