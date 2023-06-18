"""
Реализуйте класс Money, описывающий денежную сумму в рублях.
При создании экземпляра класс должен принимать один аргумент: amount — количество денег

Экземпляр класса Money должен иметь следующее неформальное строковое представление: <количество денег> руб.

Также экземпляр класса Money должен поддерживать унарные операторы + и -:

результатом унарного + должен являться новый экземпляр класса Money с неотрицательным количеством денег
результатом унарного - должен являться новый экземпляр класса Money с отрицательным количеством денег

Примечание. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"{self.amount} руб."

    def __pos__(self):
        if 0 <= self.amount:
            return Money(self.amount)
        return Money(-self.amount)

    def __neg__(self):
        if 0 <= self.amount:
            return Money(-self.amount)
        return Money(self.amount)

if __name__ == '__main__':

    money1 = Money(-100)
    print(money1)       # 100 руб.
    print(+money1)      # 100 руб.
    print(-money1)      # -100 руб.

    print('-' * 15)

    money2 = Money(100)
    print(money2)       # -100 руб.
    print(+money2)      # 100 руб.
    print(-money2)      # -100 руб.