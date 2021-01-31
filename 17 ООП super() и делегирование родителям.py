class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name)
        self.surname = surname
        # super().__init__(name)


s = Student('Ivan', 'Ivanov')

print('s.__dict__', s.__dict__)


class Person1:
    def hello(self):
        print(f'Bound with {self}')


class Student1(Person1):
    def hello(self):
        print(f'Student1 obj.hello() is called')
        super().hello()


s = Student1()
print('s.hello()', s.hello())
print('hex(id(s))', hex(id(s)))
