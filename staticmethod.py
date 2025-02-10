# add setter and getter methods to the BankAccount class to allow access to the _balance attribute
class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self.is_valid_interest_rate(amount):
            self._balance += amount
            print(f"{self.owner} deposited {amount}. New balance is {self._balance}")
        else:
            print("Deposit amount must be greater than 0")

    def _is_valid_amount(self, amount):
        return amount > 0

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BankAccount("John", 1000)
account.deposit(90)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(6))
