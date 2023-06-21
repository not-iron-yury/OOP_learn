"""
Реализуйте декоратор @CachedFunction, который кэширует вычисленные значения декорируемой функции.
Кэш должен быть доступен по атрибуту cache и представлять собой словарь, ключом в котором является кортеж с аргументами,
а значением — возвращаемое значение декорируемой функции при вызове с этими аргументами.

Примечание. Для однозначного кеширования гарантируется,
что декорируемая функция принимает только позиционные аргументы.
"""


class CachedFunction:

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]


if __name__ == '__main__':

    # @CachedFunction
    def slow_fibonacci(n):
        if n == 1:
            return 0
        elif n in (2, 3):
            return 1
        return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


    print(slow_fibonacci(20))

    print('-' * 15)

    @CachedFunction
    def slow_fibonacci(n):
        if n == 1:
            return 0
        elif n in (2, 3):
            return 1
        return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


    slow_fibonacci(5)

    for args, value in sorted(slow_fibonacci.cache.items()):
        print(args, value)
