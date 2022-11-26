"""Модуль выполнения д/з"""


class Add_class:
    indent_size = 4
    indent = 0

    def __init__(self):
        self.name_class = ''
        self.designer = 'def __init__(self):'
        self.parameter_designer = []

    def __str__(self):
        return self.__str

    @property
    def __str(self):
        lines = ' ' * (self.indent + 1) * self.indent_size
        new_designer = ''
        string_parameter = ''
        new_class = f'class {self.name_class}:'
        if self.parameter_designer:
            for el in self.parameter_designer:
                string_parameter += f'{lines + lines}{el}\n'
            new_designer += f'{new_class}\n{lines}{self.designer}\n{string_parameter}'
        else:
            new_designer = f'{new_class}\n{lines}pass'
        return new_designer


'''Строитель'''


class Builder_class(Add_class):
    # в конструктор передается имя функции

    def __init__(self, name):
        super().__init__()
        self.name_class = name

    # возможность добавлять новые параметры и их значения

    def add_field(self, parameter: str, meaning: str = "''"):
        self.parameter_designer.append(f'self.{parameter} = {meaning}')
        return self

    # возможность определять название функции(сделано как пример для возможного масштабирования)

    def add_function(self, function: str):
        self.designer = function
        return self


Ruslan = Builder_class('Person').add_field('name', 'Ruslan').add_field('age')

print(Ruslan)

random_class = Builder_class('Foo')

print(random_class)
