class BankAccount:

    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        # getter for balance
        return self._balance

    @balance.setter
    def balance(self, amount):
        # setter for balance
        if amount <= 0:
            raise ValueError("Balance should be greater than 0")
        self._balance = amount
        print(f"Balance updated to {self._balance}")

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit must be greater than 0")
        self._balance += amount
        print(f"Deposited {amount} in the account")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        if self._balance < amount:
            raise ValueError("Insufficient balance")
        self._balance -= amount
        print(f"Withdrew {amount} from the account")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=3):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._balance * self.interest_rate / 100
        self._balance += interest
        print(f"Applied interest: {interest}. New balance: {self._balance}")


class CurrentAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=1000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        if self._balance - amount < -self.overdraft_limit:
            raise ValueError("Withdrawal amount exceeds the overdraft limit")
        self._balance -= amount
        print(f"Withdrew {amount} from the account")


# Testing
account = BankAccount("John", 9000)
print(account.balance)  # ✅ Should return 9000

# Update balance
account.balance = 10000
account.deposit(500)
print(account.balance)

# Withdraw money
account.withdraw(200)
print(account.balance)

# Create a SavingsAccount instance (Fixed)
savings_account = SavingsAccount("John", account.balance)
savings_account.calculate_interest()  # ✅ Corrected: Applies interest
print(f"New balance after interest: {savings_account.balance}")

# Create a CurrentAccount instance
current_account = CurrentAccount("John", 500, overdraft_limit=1000)
print(current_account.balance)

# Test overdraft functionality
try:
    current_account.withdraw(1200)  # ✅ Allowed
    print(current_account.balance)
except ValueError as e:
    print(e)

try:
    current_account.withdraw(400)  # ❌ Should fail
    print(current_account.balance)
except ValueError as e:
    print(e)

# Test SavingsAccount methods
savings_acc = SavingsAccount("John", 1000)
print(savings_acc.balance)
savings_acc.deposit(100)
print(savings_acc.balance)
savings_acc.withdraw(200)
print(savings_acc.balance)
