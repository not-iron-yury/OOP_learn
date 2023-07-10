"""
Реализуйте класс Greeter.

При создании экземпляра класс должен принимать один аргумент:
    name — имя пользователя

Экземпляр класса Greeter должен иметь один атрибут:
    name — имя пользователя

Экземпляр класса Greeter должен являться контекстным менеджером, который приветствует пользователя с именем name
перед выполнением блока with и выводит текст: Приветствую, <имя пользователя>!
а также прощается с ним после выполнения блока with и выводит текст: До встречи, <имя пользователя>!

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Класс Greeter должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__()
и __exit__(). Реализация же протокола может быть произвольной.
"""

class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Приветствую, {self.name}!')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'До встречи, {self.name}!')



if __name__ == '__main__':
    with Greeter('Кейв'):
        print('...')

    print('-'*15)

    with Greeter('Кейв') as greeter:
        print(greeter.name)