class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, value):
        print('From set_name()')
        self._name = value

    # name = property(fget=get_name, fset=set_name)

    name = property()
    name = name.getter(get_name)
    name = name.setter(set_name)


p = Person('Dima')

# print('p.name', p.name)
# p.name = "Ivan"
# print('p.name', p.name)

print('p.__dict__', p.__dict__)
print('p.name', p.name)

p.name = 'Ivan'
print('p.__dict__', p.__dict__)


class Person2:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # name = property(name)
    # name = name.property(set_name)
