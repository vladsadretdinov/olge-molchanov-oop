from datetime import datetime


class Person:
    __name = "Ivan"


p = Person()

# p.__name AttributeError:

print('dir(p)', dir(p))

print('p.__dict__', p.__dict__)


WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._history = []

    @staticmethod
    def _get_current_time():
        return datetime.now().strftime('%d, %b %Y')

    def deposit(self, amount):
        self.__balance = amount
        self.show_balance()
        self._history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'You spent {amount} units')
            self._history.append([-amount, self._get_current_time()])
        else:
            print('Not enough money')
        self.show_balance()

    def show_balance(self):
        print(f'Balance: {self.__balance}')

    def show_history(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdrawn'
                color = RED
            print(f'{color} {amount} {WHITE} {transaction} on {date}')


a = Account('oleg', 0)
a.deposit(100)
a.show_balance()
a.__balance = 100000
a.show_balance()
print('a.__dict__', a.__dict__)
