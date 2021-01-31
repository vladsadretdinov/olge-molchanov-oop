class Person:
    def hello(self):
        print('I am person')


class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError('Food should be set')
        print(f'I like {self.food}')


class Student(FoodMixin, Person):
    food = 'Pizza'

    def hello(self):
        print("i am student")


class Prof(Person):
    def hello(self):
        print("i am Prof")


class Someone(Student, Prof):
    # class Someone(Person, Student): #  MRO
    pass


s = Someone()

print('s.hello()', s.hello())
print('s.__class__.mro()', s.__class__.mro())


s = Student()
print('s.get_food()', s.get_food())
