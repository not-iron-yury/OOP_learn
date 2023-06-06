"""Реализуйте класс BankAccount, описывающий банковский счет. При создании экземпляра класс должен принимать один аргумент:

balance — баланс счета, по умолчанию имеет значение 0
Экземпляр класса BankAccount должен иметь один атрибут:

_balance — баланс счета
Класс BankAccount должен иметь четыре метода экземпляра:

get_balance() — метод, возвращающий актуальный баланс счета
deposit() — метод, принимающий в качестве аргумента число amount и увеличивающий баланс счета на amount
withdraw() — метод, принимающий в качестве аргумента число amount и уменьшающий баланс счета на amount. Если amount превышает количество средств на балансе счета, должно быть возбуждено исключение ValueError с сообщением:
На счете недостаточно средств
transfer() — метод, принимающий в качестве аргументов банковский счет account и число amount. Метод должен уменьшать баланс текущего счета на amount и увеличивать баланс счета account на amount. Если amount превышает количество средств на балансе текущего счета, должно быть возбуждено исключение ValueError с сообщением:
На счете недостаточно средств
"""
class BankAccount:
    def __init__(self, balance=0):
        if type(balance) in (int, float):
            self._balance = balance
        else:
            raise ValueError('Ёпта, не знаешь что такое цифры?')

    def get_balance(self) -> int | float:
        """Возвращает актуальный баланс счета"""
        return self._balance

    def deposit(self, amount: int | float) -> None:
        """Принимает число amount и увеличивающий баланс счета на amount"""
        if type(amount) not in (int, float):
            raise ValueError('Ёпта, не знаешь что такое цифры?')
        self._balance += amount

    def withdraw(self, amount: int | float) -> None:
        """Принимает число amount и уменьшающий баланс счета на amount. Либо возбуждает исключение"""
        if type(amount) not in (int, float):
            raise ValueError('Ёпта, не знаешь что такое цифры?')
        if self._balance - amount < 0:
            raise ValueError('На счете недостаточно средств')
        self._balance -= amount


    def transfer(self, account, amount: int | float) -> None:
        """Принимает банковский счет account и число amount.
        Уменьшает баланс текущего счета на amount и увеличивает баланс счета account на amount.
        Либо возбуждает исключение"""
        if type(amount) not in (int, float) or type(account) != BankAccount:
            raise ValueError('Введены не корректные данные')
        if self._balance - amount < 0:
            raise ValueError('На счете недостаточно средств')
        account.deposit(amount)
        self._balance -= amount



if __name__ == '__main__':
    account1 = BankAccount(100)
    account2 = BankAccount(200)

    account1.transfer(account2, 50)
    print(account1.get_balance())
    print(account2.get_balance())
    print('----------------------')
    account3 = BankAccount(100)
    account4 = BankAccount(200)

    try:
        account3.transfer(account4, 150)
    except ValueError as e:
        print(e)
    print('----------------------')
    account5 = BankAccount(200)
    account6 = BankAccount(200)

    try:
        account5.transfer(account6, 150)
    except ValueError as e:
        print(e)
    print(account6.get_balance())
    print('----------------------')
    account7 = BankAccount(100)
    account8 = BankAccount(200)
    try:
        account7.transfer(1, 50)
    except ValueError as e:
        print(e)