"""
Реализуйте класс IPAddress, описывающий IP-адрес.
При создании экземпляра класс должен принимать один аргумент:

ipaddress — IP-адрес, представленный в одном из следующих вариантов:
1) строка из четырех целых чисел, разделенных точками
2) список или кортеж из четырех целых чисел

Экземпляр класса IPAddress должен иметь следующее формальное строковое представление:
IPAddress('<IP-адрес в виде четырех целых чисел, разделенных точками>')

И следующее неформальное строковое представление:
<IP-адрес в виде четырех целых чисел, разделенных точками>

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса IPAddress нет, она может быть произвольной.
"""


class IPAddress:
    def __init__(self, ipaddress):
        self.ipaddress = self.ip_validate(ipaddress)

    @staticmethod
    def ip_validate(ip):
        if type(ip) in (tuple, list):
            return '.'.join(map(str, ip))
        return ip

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"

    def __str__(self):
        return f"{self.ipaddress}"


if __name__ == '__main__':
    ip = IPAddress('8.8.1.1')
    print(str(ip))  # 8.8.1.1
    print(repr(ip))  # IPAddress('8.8.1.1')

    print('-' * 15)

    ip = IPAddress([1, 1, 10, 10])
    print(str(ip))  # 1.1.10.10
    print(repr(ip))  # IPAddress('1.1.10.10')

    print('-' * 15)

    ip = IPAddress((1, 1, 11, 11))
    print(str(ip))  # 1.1.11.11
    print(repr(ip))  # IPAddress('1.1.11.11')
