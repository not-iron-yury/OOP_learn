"""
Реализуйте класс Counter, экземплярами которого являются итераторы,
генерирующие последовательность целых чисел от значения low до значения high включительно с шагом один.
"""


class Counter:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return self  # возвращает сам себя, т.к. является итератором

    def __next__(self):
        if self.low > self.high:    # условие для возбуждения исключения StopIteration
            raise StopIteration
        self.low += 1               # генерация следующего значения
        return self.low - 1         # возврат следующего значения


if __name__ == '__main__':
    counter1 = Counter(3, 10)
    [print(i) for i in counter1]

    print('-' * 15)

    counter2 = Counter(100, 103)
    print(next(counter2))
    print(next(counter2))
