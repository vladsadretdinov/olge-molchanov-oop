class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._full_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._full_name = None

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        self._full_name = None

    @property
    def full_name(self):
        if self._full_name is None:
            self._full_name = f'{self._name} {self._surname}'
        return self._full_name


p = Person('Dima', 'Ivanov')
print('p.name', p.name)
p.name = 'Ivan'
print('p.full_name', p.full_name)

p.surname = 'Petroff'
print('p.full_name', p.full_name)

print('p.__dict__', p.__dict__)
p.surname = 'Sadr'
print('p.__dict__', p.__dict__)
print('p.full_name', p.full_name)
print('p.__dict__', p.__dict__)
