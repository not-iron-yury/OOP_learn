"""
Реализуйте класс StrExtension, описывающий набор функций для работы со строками.
При создании экземпляра класс не должен принимать никаких аргументов.

Класс StrExtension должен иметь три статических метода:

remove_vowels() — метод, который принимает в качестве аргумента строку,
удаляет из нее все гласные латинские буквы без учета регистра и возвращает полученный результат.

leave_alpha() — метод, который принимает в качестве аргумента строку,
удаляет из нее все символы, не являющиеся латинскими буквами, и возвращает полученный результат.

replace_all() — метод, который принимает три строковых аргумента string, chars и char,
заменяет в строке string все символы из chars на char с учетом регистра и возвращает полученный результат.
"""


class StrExtension:
    @staticmethod
    def remove_vowels(string: str) -> str:
        return ''.join([s for s in string if s.lower() not in 'aeoiuy'])

    @staticmethod
    def leave_alpha(string: str) -> str:
        return ''.join([s for s in string if s.isalpha()])

    @staticmethod
    def replace_all(string: str, chars: str, char: str) -> str:
        for i in chars:
            string = string.replace(i, char)
        return string


if __name__ == '__main__':
    print(StrExtension.remove_vowels('Asus'))
    print(StrExtension.remove_vowels('Python'))
    print(StrExtension.remove_vowels('Stepik'))
    print(StrExtension.leave_alpha('Python111'))
    print(StrExtension.leave_alpha('__Stepik__()'))
    print(StrExtension.replace_all('Python', 'Ptn', '-'))   #   -y-ho-
    print(StrExtension.replace_all('Stepik', 'stk', '#'))   #   S#epi#

    from string import ascii_lowercase

    text = '''I live in a house near the mountains. I have two brothers and one sister, and I was born last. My father teaches mathematics, and my mother is a nurse at a big hospital. My brothers are very smart and work hard in school. My sister is a nervous girl, but she is very kind. My grandmother also lives with us. She came from Italy when I was two years old. She has grown old, but she is still very strong. She cooks the best food!
    My family is very important to me. We do lots of things together. My brothers and I like to go on long walks in the mountains. My sister likes to cook with my grandmother. On the weekends we all play board games together. We laugh and always have a good time. I love my family very much.'''

    print(StrExtension.remove_vowels(text))
    print(StrExtension.leave_alpha(text))
    print(StrExtension.replace_all(text, ascii_lowercase, ''))