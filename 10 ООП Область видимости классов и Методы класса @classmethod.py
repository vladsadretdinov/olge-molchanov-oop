name = 'Ivan'


class Person:
    name = "Dima"

    def print_name(self):
        print(name)
        print(self.name)

    @classmethod
    def change_name(cls, name):
        cls.name = name


p = Person()
p.print_name()


# x = 1
# def a():
#     x  = x + 1
#     print(x)
# a()


# def a():
#     x = 1


# def b():
#     print(x)


# b()

print('p.__dict__', p.__dict__)
p.print_name()

p.name = 'adasdadasd'
print('Istance dict: ', p.__dict__)
p.print_name()

print('Person.name:', Person.name)


p1 = Person()
print('p1.__dict__', p1.__dict__)
p1.change_name('123')
print('Istance dict: ', p.__dict__)
print('Person.name:', Person.name)


class Person2:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            name = f.read().strip()
        return cls(name=name)

    @classmethod
    def from_obj(cls, obj):
        if hasattr(obj, 'name'):
            name = getattr(obj, 'name')
            return cls(name=name)
        return cls


class Config:
    name = 'Igor'


p1 = Person2('oleg')
print('p.__dict__', p.__dict__)
print('p.name', p.name)

p = Person2.from_file('text')
print('p.__dict__', p.__dict__)
print('p.name', p.name)

p = Person2.from_obj(Config)
print('p.__dict__', p.__dict__)
print('p.name', p.name)
