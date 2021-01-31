class Person:
    def hello():
        print('Hello')


print('Person.hello', Person.hello)

p = Person()

print('p.hello', p.hello)

print('hex(id(p))', hex(id(p)))

print('Person.hello()', Person.hello())

# print('p.hello()', p.hello()) TypeError


print('type(p.hello)', type(p.hello))
print('type(p.hello)', type(Person.hello))

print('id(p.hello)', id(p.hello))
print('id(p.hello)', id(Person.hello))

print('dir(p.hello)', dir(p.hello))
print('dir(p.hello)', dir(Person.hello))

print('p.__dict__', p.__dict__)


print("'person-dima'.split('-')", 'person-dima'.split('-'))
print("'person'.split('-')", 'person'.split('-'))

# Person.hello(p)

print('p.hello.__self__', p.hello.__self__)
print('hex(id(p))', hex(id(p)))

print('p.hello.__func__', p.hello.__func__)

# p.hello.__func__(hello.__self__, *args)


class Person1:
    def hello(self):
        print(self)


p = Person1()

print('p.hello', p.hello)
print('hex(id(p))', hex(id(p)))
