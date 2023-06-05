class Wordplay:
    def __init__(self, words=None):
        self.words = [] if words == None else words[:]

    def add_word(self, word: str) -> None:
        """Принимает слово и добавляет его в набор, если его нет в наборе."""
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n: int) -> list[str]:
        """Принимает целое число n и возвращает список слов из набора, длина которых равна n."""
        return list(filter(lambda x: len(x) == n, self.words))

    def only(self, *args: str) -> list[str]:
        """Принимает произвольное количество аргументов — букв,
        и возвращает все слова из набора, которые состоят только из переданных букв"""
        return list(filter(lambda x: set(x).issubset(args), self.words))

    def avoid(self, *args: str) -> list[str]:
        """Принимает произвольное количество аргументов — букв,
        и возвращает все слова из списка words, которые не содержат ни одну из этих букв"""
        return list(filter(lambda x: set(args).isdisjoint(x), self.words))


if __name__ == '__main__':
    wordplay = Wordplay()

    print(wordplay.words_with_length(1))
    print(wordplay.only('a', 'b', 'c'))
    print(wordplay.avoid('a', 'b', 'c'))
    print()
    wordplay2 = Wordplay()

    print(wordplay2.words)
    wordplay2.add_word('bee')
    wordplay2.add_word('geek')
    print(wordplay2.words)
    print()
    wordplay3 = Wordplay(['bee', 'geek', 'cool', 'stepik'])

    wordplay3.add_word('python')
    print(wordplay3.words_with_length(4))
    print()
    wordplay4 = Wordplay(['o', 'to', 'otto', 'top', 't'])

    print(wordplay4.only('o', 't'))