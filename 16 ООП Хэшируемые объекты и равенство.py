class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, person_obj):
        return isinstance(person_obj, Person) and self.name == person_obj.name


p1 = Person('Ivan')
p2 = Person('Ivan')

print('p1', p1)
print('p2', p2)

print('p1 == p2', p1 == p2)
print('p1 is p2', p1 is p2)

p3 = Person('Oleg')
print('p1 == p3', p1 == p3)

print('hash(p1)', hash(p1))
print('hash(p2)', hash(p2))

d = {p1: 'Ivanonv Ivan'}
d.get(p1)
