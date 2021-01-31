from datetime import datetime


WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'


class Account:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
        self._history = []

    @staticmethod
    def _get_current_time():
        return datetime.now().strftime('%d, %b %Y')

    def deposit(self, amount):
        self._balance = amount
        self.show_balance()
        self._history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount
            print(f'You spent {amount} units')
            self._history.append([-amount, self._get_current_time()])
        else:
            print('Not enough money')
        self.show_balance()

    def show_balance(self):
        print(f'Balance: {self._balance}')

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
a.show_balance()

a.deposit(100)

a.withdraw(50)

a.show_history()
