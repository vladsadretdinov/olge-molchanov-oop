import weakref
from weakref import WeakKeyDictionary

a = 123
b = a
print('b', b)
print('a', a)

print('id(a)', id(a))
print('id(b)', id(b))

del a
print('b', b)


class Person:
    pass


p = Person()
w = weakref.ref(p)

print('w', w)
print('hex(id(p))', hex(id(p)))
print('p', p)

del p
print('w', w)

p1 = Person()
w1 = weakref.ref(p1)
print('w1()', w1())
del p1
print('w1()', w1())


p2 = Person()
d = weakref.WeakKeyDictionary()
print('d', d)
d[p2] = 10
print('d[p2', d[p2])

print('dir(d)', dir(d))
print('d.keyrefs()', d.keyrefs())

del p2
print('d.keyrefs()', d.keyrefs())


class IntDescriptor:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __set__(self, instance, value):
        # print(f'I got {value}')
        self._values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            # print('Call from a class')
            return self
        # print('Call from instance')
        return self._values.get(instance)


class Vector:
    x = IntDescriptor()
    y = IntDescriptor()


v = Vector()
print('hex(id(v))', hex(id(v)))
v.x = 10
print('Vector.x._values.keyrefs()', Vector.x._values.keyrefs())
del v
print('Vector.x._values.keyrefs()', Vector.x._values.keyrefs())
