"""
Реализуйте класс итератор EvenNumbers, экземплярами которого являются бесконечные итераторы,
генерирующие последовательность всех целых четных чисел начиная со значения begin (включительно).
"""


class EvenNumbers:
    def __init__(self, begin):
        self.begin = begin + begin % 2

    def __iter__(self):
        return self

    def __next__(self):
        value = self.begin
        self.begin += 2
        return value


if __name__ == '__main__':

    evens1 = EvenNumbers(10)        # все четные числа от 10 до бесконечности

    for index, num in enumerate(evens1):
        if index > 5:
            break
        print(num)

    print('-' * 15)

    evens2 = EvenNumbers(101)       # все четные числа от 102 до бесконечности
    print(next(evens2))
    print(next(evens2))
    print(next(evens2))
    print(next(evens2))
