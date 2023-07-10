"""
Реализуйте класс UpperPrint.

При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса UpperPrint должен являться контекстным менеджером, который внутри блока with позволяет выполнять
все операции записи в стандартный поток вывода sys.stdout в верхнем регистре.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Класс UpperPrint должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__()
и __exit__(). Реализация же протокола может быть произвольной.
"""

import sys


class UpperPrint:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.upper_write

    def upper_write(self, text):
        self.original_write(text.upper())

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_write


if __name__ == '__main__':
    print('Если жизнь одаривает вас лимонами — не делайте лимонад')
    print('Заставьте жизнь забрать их обратно!')

    with UpperPrint():
        print('Мне не нужны твои проклятые лимоны!')
        print('Что мне с ними делать?')

    print('Требуйте встречи с менеджером, отвечающим за жизнь!')

    print('-' * 15)

    with UpperPrint():
        print('Bee', 'Geek', 'Love', sep=' one ', end=' end')
