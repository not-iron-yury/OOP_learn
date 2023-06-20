"""
Реализуйте декоратор @CountCalls, который считает количество вызовов декорируемой функции.
Счетчик вызовов должен быть доступен по атрибуту calls
"""


class CountCalls:
    calls = 0

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        return self.func(*args)


if __name__ == '__main__':

    @CountCalls
    def add(a, b):
        return a + b


    print(add(1, 2))
    print(add(2, 3))
    print(add.calls)

    print('-' * 15)


    @CountCalls
    def square(a):
        return a ** 2


    for i in range(100):
        square(i)

    print(square.calls)
