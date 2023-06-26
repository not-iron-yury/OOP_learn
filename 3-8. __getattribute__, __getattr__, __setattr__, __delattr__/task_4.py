"""
Реализуйте класс AttrsNumberObject.
При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Экземпляр класса AttrsNumberObject должен иметь один атрибут:
    attrs_num — количество атрибутов, которыми обладает экземпляр класса AttrsNumberObject на данный момент,
    включая сам атрибут attrs_num

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса AttrsNumberObject нет, она может быть произвольной.
"""

# Вариант 1
class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.attrs_num = len(self.__dict__)

    def __setattr__(self, key, value):
        self.__dict__.update({key: value})
        self.__dict__['attrs_num'] += 1

    def __delattr__(self, attr):
        del self.__dict__[attr]
        self.__dict__['attrs_num'] -= 1


# Вариант 2
# class AttrsNumberObject:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#
#     def __getattr__(self, name):
#         if name == 'attrs_num':
#             return len(self.__dict__) + 1


if __name__ == '__main__':
    music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')

    print(music_group.attrs_num)
    del music_group.genre
    print(music_group.attrs_num)

    print('-' * 15)

    music_group = AttrsNumberObject(name='Woodkid', genre='pop')

    print(music_group.attrs_num)
    music_group.country = 'France'
    print(music_group.attrs_num)
