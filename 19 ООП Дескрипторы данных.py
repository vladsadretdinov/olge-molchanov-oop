import ctypes
import sys
from time import time


class Epoch:
    def __get__(self, instance, owner_class):
        # print(f'Self: {self}')
        # print(f'instance: {instance}')
        # print(f'owner_class: {owner_class}')

        print(f'id of self: {id(self)}')

        if instance is None:
            return self
        return int(time())

    def __set__(self, instance, value):
        pass


class MyTime:
    epoch = Epoch()


m = MyTime()
print('m.epoch', m.epoch)
print('MyTime.epoch', MyTime.epoch)

m1 = MyTime()
print('m1.epoch', m.epoch)


class Person:
    _name = 'Oleg'

    @property
    def name(self):
        return self._name


print('Person.name', Person.name)
print('Person().name', Person().name)


class IntDescriptor:
    def __init__(self):
        self._values = {}

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

v.x = 5

v2 = Vector()

print('v2.x', v2.x)

v2.x = 200

print('v.x', v.x)
print('v2.x', v2.x)


print('Vector.x._values', Vector.x._values)


v = 1
print('sys.getrefcount(v)', sys.getrefcount(v))
val = 'oleg'
print('sys.getrefcount(val)', sys.getrefcount(val))


def ref_count(obj_id):
    return ctypes.c_long.from_address(obj_id).value


print('ref_count(id(val))', ref_count(id(val)))
v3 = Vector()
print('ref_count(id(v3))', ref_count(id(v3)))

id_v = id(v3)
v3.x = 5
print('ref_count(id(v3))', ref_count(id_v))
v3.y = 5
print('ref_count(id(v3))', ref_count(id_v))
del v3
print('ref_count(id(v3))', ref_count(id_v))


print('Vector.x._values', Vector.x._values)
print('Vector.x._values.keys()', Vector.x._values.keys())
print('list(Vector.x._values.keys())[0]', list(Vector.x._values.keys())[0])
