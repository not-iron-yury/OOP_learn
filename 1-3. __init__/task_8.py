class Todo:
    def __init__(self):
        self.things = []
        self.min_priority = 10
        self.max_priority = 0

    def add(self, task, priortet):
        """принимает название дела и его приоритет (int)
        и добавляет данное дело в список в виде кортежа (<название дела>, <приоритет>)"""
        self.things.append((task, priortet))
        if self.min_priority > priortet:
            self.min_priority = priortet
        if self.max_priority < priortet:
            self.max_priority = priortet

    def get_by_priority(self, priortet):
        """принимает в качестве аргумента целое число n
        и возвращающий список названий дел, имеющих приоритет n"""
        return list(map(lambda x: x[0], filter(lambda x: x[1] == priortet, self.things)))

    def get_low_priority(self):
        """возвращает список названий дел, имеющих самый низкий приоритет"""
        return list(map(lambda x: x[0], filter(lambda x: x[1] == self.min_priority, self.things)))

    def get_high_priority(self):
        """возвращает список названий дел, имеющих самый высокий приоритет"""
        return list(map(lambda x: x[0], filter(lambda x: x[1] == self.max_priority, self.things)))




todo = Todo()

todo.add('Проснуться', 3)
todo.add('Помыться', 2)
todo.add('Поесть', 2)
todo.add('Потискать котэ', 8)
todo.add('Уборка', 5)

print(todo.get_by_priority(3))
print(todo.get_low_priority())
print(todo.get_high_priority())