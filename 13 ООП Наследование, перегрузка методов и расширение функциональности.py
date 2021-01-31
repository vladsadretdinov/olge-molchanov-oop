class Person:
    age = 0

    def hello(self):
        print('Hello')


class Student(Person):
    pass


s = Student()

print('dir(s)', dir(s))

print('s.age', s.age)
print('s.hello()', s.hello())

print('s.__dict__', s.__dict__)
print('Student.__dict__', Student.__dict__)
print('Person.__dict__', Person.__dict__)

print('dir(object)', dir(object))


class IntelCpu:
    cpu_socker = 1151
    name = 'Intel'


class I7(IntelCpu):
    pass


class I5(IntelCpu):
    pass


i5 = I5()
i7 = I7()

print('isinstance(i5, IntelCpu)', isinstance(i5, IntelCpu))

print('type(i5)', type(i5))


class One:
    pass


class Two(One):
    pass


class Three(Two):
    pass


print('issubclass(Three, One)', issubclass(Three, One))

print('isinstance(i5, type(i7))', isinstance(i5, type(i7)))

print('issubclass(type(i5), type(i7))', issubclass(type(i5), type(i7)))


class Person1:
    def hello(self):
        print('I am person')


class Student1(Person1):
    def hello(self):
        print("i am student")

    def goodbey(self):
        print("Goodbey")


s = Student1()

print('s.hello()', s.hello())
print('s.__dict__', s.__dict__)
print('Student1s.__dict__', Student1.__dict__)


class Person3:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello from {self.name}')


class Student2(Person3):
    pass


s = Student2('Ivan')
print('s.hello()', s.hello())
print('s.__dict__', s.__dict__)
