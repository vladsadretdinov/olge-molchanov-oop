class Person:
    name = "Ivan"


print("dir(Person)", dir(Person))

print("Person.__dict__", Person.__dict__)

print('Person.name', Person.name)

Person.age = 24

print('Person.age', Person.age)

print("Person.__dict__", Person.__dict__)

print("getattr(Person, 'name')", getattr(Person, 'name'))

setattr(Person, 'dob', 123)

print("Person.__dict__", Person.__dict__)

delattr(Person, 'dob')

print("Person.__dict__", Person.__dict__)


class Person1:
    name = 'Ivan'

    def hello():
        pass


print('Person1.__dict__', Person1.__dict__)
