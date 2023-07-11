"""
Реализуйте класс HtmlTag. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

tag — HTML тег
inline — булево значение, по умолчанию равняется False
Экземпляр класса HtmlTag должен являться реентерабельным контекстным менеджером, который позволяет генерировать
HTML-код с правильными отступами и глубиной вложенности тегов. Параметр inline должен определять положение тегов и их
содержимого. Если он имеет значение True, теги и содержимое должны располагаться на одной строке,
если False — на разных строках.

Класс HtmlTag должен иметь один метод экземпляра:

print() — метод, принимающий в качестве аргумента содержимое тега и выводящий его в рамках этого тега
Примечание 1. Наглядные примеры использования класса HtmlTag продемонстрированы в тестовых данных.

Примечание 2. В качестве отступов для каждого уровня используйте два пробела.

Примечание 3. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Класс HtmlTag должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__()
и __exit__(). Реализация же протокола может быть произвольной.
"""


class HtmlTag:
    INDENT = 2
    depth = 0

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.depth = type(self).depth
        self.inline = inline
        self.end_char = '' if inline else '\n'

    def __enter__(self):
        print(' ' * type(self).INDENT * self.depth + f'<{self.tag}>', end=self.end_char)
        type(self).depth += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.inline:
            print(f'</{self.tag}>')
        else:
            print(' ' * type(self).INDENT * self.depth + f'</{self.tag}>')
        type(self).depth -= 1

    def print(self, txt):
        if self.inline:
            print(txt, end=self.end_char)
        else:
            print(' ' * type(self).INDENT * (self.depth + 1) + txt, end=self.end_char)


if __name__ == '__main__':
    with HtmlTag('body') as _:
        with HtmlTag('h1') as header:
            header.print('Поколение Python')
        with HtmlTag('p') as section:
            section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')

    # with HtmlTag('body') as _:
    #     with HtmlTag('h1', True) as header:
    #         header.print('Поколение Python')
    #     with HtmlTag('p', True) as section:
    #         section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')