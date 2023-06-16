"""
Будем называть словом любую последовательность из одной или более латинских букв.

Реализуйте класс Word, описывающий слово. При создании экземпляра класс должен принимать один аргумент:
word — слово

Экземпляр класса Word должен иметь следующее формальное строковое представление:  Word('<слово в исходном виде>')

И следующее неформальное строковое представление: <слово, в котором первая буква заглавная, а все остальные строчные>

Также экземпляры класса Word должны поддерживать между собой все операции сравнения
с помощью операторов ==, !=, >, <, >=, <=. Два слова считаются равными, если их длины совпадают.
Слово считается больше другого слова, если его длина больше.
"""
from functools import total_ordering

@total_ordering
class Word:

    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f"Word('{self.word}')"

    def __str__(self):
        return str.capitalize(self.word)

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented


if __name__ == '__main__':
    print(Word('bee') == Word('hey'))   # True
    print(Word('bee') < Word('geek'))   # True
    print(Word('bee') > Word('geek'))   # False
    print(Word('bee') <= Word('geek'))  # True
    print(Word('bee') >= Word('gee'))   # True

    print('-'*15)

    words = [Word('python'), Word('bee'), Word('geek')]
    print(sorted(words))    # [Word('bee'), Word('geek'), Word('python')]
    print(min(words))       # Bee
    print(max(words))       # Python