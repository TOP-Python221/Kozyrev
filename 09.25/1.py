class Add_class:
    indent_size = 4
    indent = 0

    def __init__(self):
        self.name_class = ''
        self.designer_class = []

    def __str__(self):
        return self.__str

    @property
    def __str(self):
        designer = 'def __init__(self):'
        lines = ' ' * (self.indent + 1) * self.indent_size
        new_designer = ''
        string_parameter = ''
        new_class = f'class {self.name_class}:'
        if self.designer_class:
            for el in self.designer_class:
                string_parameter += f'{lines + lines}{el}\n'
            new_designer += f'{new_class}\n{lines}{designer}\n{string_parameter}'
        else:
            new_designer = f'{new_class}\n{lines}pass'
        return new_designer


class Builder_class(Add_class):
    def __init__(self, name):
        super().__init__()
        self.name_class = name

    def add_field(self, parameter: str, meaning: str = "''"):
        self.designer_class.append(f'self.{parameter} = {meaning}')
        return self


Ruslan = Builder_class('Person').add_field('name', 'Ruslan').add_field('age', )

print(Ruslan)

random_class = Builder_class('Foo')

print(random_class)
