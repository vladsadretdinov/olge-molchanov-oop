class Person:
    name = 'Ivan'


print('Person.__dict__', Person.__dict__)

p1 = Person()

print('pr1', p1)

p2 = Person()

print('id(p1)', id(p1))
print('id(p2)', id(p2))

print('p1.name', p1.name)
print('p2.name', p2.name)

print('id(p1.name)', id(p1.name))
print('id(p2.name)', id(p2.name))
print('id(Person.name)', id(Person.name))

print('p1.__dict__', p1.__dict__)
print('p2.__dict__', p2.__dict__)
print('Person.__dict__', Person.__dict__)

p1.name = 'Oleg'
p2.name = 'Dima'
p2.age = 25
print('p1.__dict__', p1.__dict__)
print('p2.__dict__', p2.__dict__)


print('p1.name', p1.name)
print('p2.name', p2.name)
print('Person.__dict__', Person.__dict__)


# print('p1.age', p1.age) AttributeError

p1 = Person()
p2 = Person()
Person.name = 'asdasd'
print('p1.name', p1.name)
print('p2.name', p2.name)
