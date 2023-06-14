"""
 Объявите класс с именем Model, объекты которого создаются командой:

model = Model()

Объявите в этом классе метод query() для формирования записи базы данных.

Использоваться этот метод должен следующим образом:

model.query(field_1=value_1, field_2=value_2, ..., field_N=value_N)

Например:

model.query(id=1, fio='Sergey', old=33)

Все эти переданные данные должны сохраняться внутри объекта model класса Model.

Затем, при выполнении команды  print(model), в консоль должна выводиться информация об объекте в формате:

"Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N"

Например:

"Model: id = 1, fio = Sergey, old = 33"

Если метод query() не вызывался, то в консоль выводится строка:

"Model"
"""


class Model:
    def query(self, **kwargs):
        self.__dict__ = kwargs

    def __repr__(self):
        if self.__dict__:
            return f"Model: {self._representation()}"
        # return "Model"

    def _representation(self):
        return ', '.join([f"{name} = {value}" for name, value in self.__dict__.items()])


if __name__ == '__main__':

    model = Model()
    model.query(id=1, fio='Sergey', old=33)
    print(model)