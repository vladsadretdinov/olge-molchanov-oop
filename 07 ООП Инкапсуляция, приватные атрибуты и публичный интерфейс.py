class Person():
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self.name = f'{self._name} {self._surname}'


p = Person('oleg', 'molchanov')
print('print(p.name)', p.name)
