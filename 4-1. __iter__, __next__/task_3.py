"""
Реализуйте класс итератор Factorials, экземплярами которого являются бесконечные итераторы,
генерирующие последовательность факториалов всех натуральных чисел (от 1 до бесконечности).
"""


class Factorials:
    def __init__(self):
        self.value = 1
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.value *= self.index
        self.index += 1
        return self.value

if __name__ == '__main__':

    infinite_factorials = Factorials()

    for index, num in enumerate(infinite_factorials, 1):
        if index <= 10:
            print(f'Факториал числа {index} равен {num}')
        else:
            break