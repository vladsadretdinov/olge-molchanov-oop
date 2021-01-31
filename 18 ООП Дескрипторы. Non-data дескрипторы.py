from random import choice
from time import time


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


class StringD:
    def __init__(self, value=None):
        if value:
            self.set(value)

    def set(self, value):
        self._value = value

    def get(self):
        return self._value


class Person1:
    def __init__(self, name, surname):
        self.name = StringD(name)
        self.surname = StringD(surname)


p = Person('Ivan', 'Ivanov')

p = Person1('Ivan', 'Ivanov')
print('p.name', p.name)
print('p.name', p.name)
print('p.name.get()', p.name.get())


class Epoch:
    def __get__(self, instance, owner_class):
        return int(time())


class MyTime:
    epoch = Epoch()


m = MyTime()

print('m.epoch', m.epoch)
print('m.epoch', m.epoch)
print('m.epoch', m.epoch)


class Dice:
    @property
    def number(self):
        return choice(range(1, 7))


d = Dice()

print('d.number', d.number)
print('d.number', d.number)
print('d.number', d.number)


class Choice:
    def __init__(self, *choice):
        self._choice = choice

    def __get__(self, obj, owner):
        return choice(self._choice)


# class Game:
#     @property
#     def rock_paper_scissors(self):
#         return choice(['Rock', 'Paper', 'Scissors'])

#     @property
#     def flip(self):
#         return choice(['Heads', 'Tails'])

#     @property
#     def dice(self):
#         return choice(range(1, 7))

class Game:
    dice = Choice(1, 2, 3, 4, 5, 6)
    flip = Choice('Heads', 'Tails')
    rock_paper_scissors = Choice('Rock', 'Paper', 'Scissors')


g = Game()

for i in range(3):
    print(g.dice)

print(g.flip)
print(g.flip)
print(g.flip)
