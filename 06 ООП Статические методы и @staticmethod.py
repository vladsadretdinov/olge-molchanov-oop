class Person():
    def hello(self):
        print('Hello')

    def goodbye():
        print('Goodbye')


p = Person()
# p.goodbye() TypeError


class Person1():
    def hello(self):
        print('Hello')

    @staticmethod
    def goodbye():
        print('Goodbye')


p = Person1()
p.goodbye()

a = Person1()
b = Person1()

print('a.hello()', a.hello())
print('a.goodbye()', a.goodbye())

print('id(a.hello)', id(a.hello))
print('id(b.hello)', id(b.hello))

print('id(a.goodbye)', id(a.goodbye))
print('id(b.goodbye)', id(b.goodbye))

print('a.__dict__', a.__dict__)
print('b.__dict__', b.__dict__)

print('type(a.goodbye)', type(a.goodbye))
print('Person1.goodbye', Person1.goodbye)
