"""
Реализуйте класс WriteSpy.

При создании экземпляра класс должен принимать три аргумента в следующем порядке:
    file1 — файловый объект
    file2 — файловый объект
    to_close — булево значение, по умолчанию равняется False

Экземпляр класса WriteSpy должен являться контекстным менеджером, который выполняет операцию записи
сразу в оба файловых объекта file1 и file2.

Параметр to_close должен определять состояние файловых объектов file1 и file2 после завершения блока with.
Если он имеет значение True, после завершения блока with контекстный менеджер должен закрыть оба файловых объекта,
если False — оставить открытыми.

Класс WriteSpy должен иметь четыре метода экземпляра:

    write() — метод, принимающий в качестве аргумента текст и записывающий его в оба файловых объекта.
              Если хотя бы один из файловых объектов закрыт или недоступен для записи,
              должно быть возбуждено исключение ValueError с текстом: Файл закрыт или недоступен для записи

    close() — метод, немедленно закрывающий оба файловых объекта

    writable() — метод, возвращающий True, если оба файловых объекта доступны для записи, или False в противном случае

    closed() — метод, возвращающий True, если оба файловых объекта закрыты, или False в противном случае


Примечание 1. Наглядные примеры использования класса WriteSpy продемонстрированы в тестовых данных.

Примечание 2. Для проверки того, является ли файловый объект доступным для записи, используйте метод writable().
Данный метод возвращает True, если файловый объект доступен для записи, или False в противном случае.
При попытке применить метод на закрытом файловом объекте будет возбуждено исключение.

Примечание 3. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Класс WriteSpy должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__()
и __exit__(). Реализация же протокола может быть произвольной.
"""


class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1, self.file2 = file1, file2
        self.to_close = to_close

    def write(self, string):
        if not self.writable():
            raise ValueError('Файл закрыт или недоступен для записи')
        self.file1.write(string)
        self.file2.write(string)

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        return all((self.file1.mode == 'w', self.file2.mode == 'w', not self.file1.closed, not self.file2.closed))

    def closed(self):
        return self.file1.closed and self.file2.closed

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close:
            self.close()

if __name__ == '__main__':
    f1 = open('file1.txt', mode='w')
    f2 = open('file2.txt', mode='w')
    f2.close()

    try:
        with WriteSpy(f1, f2, to_close=True) as combined:
            combined.write('No cost too great')
    except ValueError as error:
        print(error)

    print('-' * 15)

    f1 = open('file1.txt', mode='r')
    f2 = open('file2.txt', mode='w')

    try:
        with WriteSpy(f1, f2, to_close=True) as combined:
            combined.write('No cost too great')
    except ValueError as error:
        print(error)

    print('-' * 15)

    f1 = open('file1.txt', mode='w')
    f2 = open('file2.txt', mode='w')

    with WriteSpy(f1, f2, to_close=True) as combined:
        print(combined.writable())

    f1 = open('file1.txt')
    f2 = open('file2.txt')

    with WriteSpy(f1, f2, to_close=True) as combined:
        print(combined.writable())

    print('-' * 15)

    f1 = open('file1.txt', mode='w')
    f2 = open('file2.txt', mode='w')

    with WriteSpy(f1, f2, to_close=True) as combined:
        print(combined.closed())
        f1.close()
        print(combined.closed())
        f2.close()
        print(combined.closed())