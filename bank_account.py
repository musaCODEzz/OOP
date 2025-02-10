class BankAccount:
    def __init__(self, owner, balance=0):
        if balance <= 0:
            raise ValueError(
                "Balance should be greater than 0"
            )  # ✅ Ensure balance is valid at creation
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        """Getter for balance"""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """Setter for balance"""
        if amount <= 0:
            raise ValueError(
                "Balance should be greater than 0"
            )  # ✅ Raise error instead of printing
        self._balance = amount

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            raise ValueError(
                "Deposit amount must be greater than 0"
            )  # ✅ Fix: Raise an exception
        self._balance += amount
        print(f"Deposited {amount} in the account")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be greater than 0"
            )  # ✅ Fix: Raise an exception

        if self._balance < amount:
            raise ValueError(
                "Insufficient balance"
            )  # ✅ Fix: Raise an exception instead of printing

        self._balance -= amount
        print(f"Withdrew {amount} from the account")


account = BankAccount("John", 9000)
print(account.balance)
account.deposit(500)
print(account.balance)
account.withdraw(200)
print(account.balance)
