class Person:
    name = 'Ivan'


print('Person.name', Person.name)

print('Person.__name__', Person.__name__)

print('dir(Person)', dir(Person))

print('Person.__class__', Person.__class__)

p = Person()

print('p.__class__', p.__class__)

print('p.__class__.__name__', p.__class__.__name__)

print('type(p)', type(p))

new_person = type(p)()

print('new_person', new_person)

print('id(p)', id(p))
print('id(new_person)', id(new_person))
