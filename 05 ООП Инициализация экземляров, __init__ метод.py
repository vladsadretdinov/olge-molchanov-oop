class Person:
    pass


p = Person()
p.name = 'Ivan'
print("p.name", p.name)


class Person1():
    def create(self):
        self.name = 'Ivan'

    def display(self):
        print(self.name)


p = Person1()
# p.display() AttrubuteError
print('p.__dict__', p.__dict__)

p.create()
print('p.__dict__', p.__dict__)


class Person2():
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


p = Person2('ivan')
print('p.name', p.name)
print('p.__dict__', p.__dict__)
