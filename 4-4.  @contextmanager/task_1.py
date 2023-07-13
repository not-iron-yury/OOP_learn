"""Реализуйте контекстный менеджер make_tag с помощью декоратора @contextmanager, который принимает один аргумент:

tag — произвольная строка

Контекстный менеджер должен выводить строку tag при входе в блок with и после выхода из блока with.

Примечание 1. Наглядные примеры использования контекстного менеджера make_tag продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный контекстный менеджер используется только с корректными данными"""

from contextlib import contextmanager

@contextmanager
def make_tag(tag):
    print(tag)
    yield
    print(tag)


if __name__ == '__main__':
    with make_tag('---'):
        print('Поколение Python')