'''
1) Разработайте класс BankAccount, который имеет атрибуты balance (баланс) и owner (владелец).
Реализуйте методы deposit(amount) для внесения средств на счет и
withdraw(amount) для снятия средств со счета.
Учтите возможность проверки наличия достаточного баланса перед снятием.
'''


from decimal import Decimal


class BankAccount:
    def __init__(self, balance: Decimal, owner: str):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount: Decimal):
        self.balance += amount

    def withdraw(self, amount: Decimal):
        result_balance = self.balance - amount
        if result_balance < 0:
            print(f'Недостаточный баланс на аккаунте: {self.owner}')
            return
        self.balance -= amount

    def __str__(self):
        return f'owner: {self.owner}; balance: {self.balance}'


a = BankAccount(balance=Decimal('10'), owner='Bob')
b = BankAccount(balance=Decimal('100.12'), owner='John')
print(a)
a.deposit(Decimal('1000'))
print(a)
print('----------------')
print(b)
b.withdraw(Decimal('1000'))
print(b)
b.withdraw(Decimal('100'))
print(b)
