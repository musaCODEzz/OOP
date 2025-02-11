from abc import ABC, abstractmethod
from datetime import datetime


class Transaction(ABC):
    def __init__(self, amount, account):
        self.amount = amount
        self.account = account
        self.timestamp = datetime.now()

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def revert(self):
        pass


class DepositTransaction(Transaction):

    # Handling deposits and allows reversion
    def execute(self):
        if self.amount <= 0:
            raise ValueError("Deposit must be greater than 0")
        self.account._balance += self.amount
        self.account.history.append(self)
        print(f"Deposited {self.amount}. New balance: {self.account.balance}")

    def revert(self):
        self.account._balance -= self.amount
        print(f"Reverted deposit of {self.amount}. New balance: {self.account.balance}")
        # Add the reverted deposit transaction to history
        reverted_transaction = DepositTransaction(-self.amount, self.account)
        self.account.history.append(reverted_transaction)


class WithdrawTransaction(Transaction):
    # handles withdrawals and reversions
    def execute(self):
        if self.amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        if self.account._balance + self.account.overdraft_limit < self.amount:
            raise ValueError("Insufficient balance and overdraft limit exceeded")
        self.account._balance -= self.amount
        self.account.history.append(self)
        print(f"Withdrew {self.amount}. New balance: {self.account.balance}")

    def revert(self):
        self.account._balance += self.amount
        print(
            f"Reverted withdrawal of {self.amount}. New balance: {self.account.balance}"
        )
        # Add the reverted withdrawal transaction to history
        reverted_transaction = WithdrawTransaction(self.amount, self.account)
        self.account.history.append(reverted_transaction)


class BankAccount:

    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.owner = owner
        self._balance = balance
        self.history = []  # List to store transaction history

    @property
    def balance(self):
        # getter for balance
        return self._balance

    def deposit(self, amount):
        transaction = DepositTransaction(amount, self)
        transaction.execute()

    def withdraw(self, amount):
        transaction = WithdrawTransaction(amount, self)
        transaction.execute()

    def print_history(self):

        # diaplay transaction history
        print(f"\nTransaction history for account: {self.owner}")
        for t in self.history:
            print(
                f"{t.timestamp}: {'Deposit' if isinstance(t, DepositTransaction) else 'Withdraw'} {t.amount}"
            )

    def revert_last_transaction(self):
        if self.history:
            last_transaction = self.history[-1]
            last_transaction.revert()
            # No need to remove the transaction from history
        else:
            print("No transactions to revert.")


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
        if self._balance + self.overdraft_limit < amount:
            raise ValueError("Insufficient balance and overdraft limit exceeded")
        self._balance -= amount
        transaction = WithdrawTransaction(
            amount, self
        )  # Create transaction for withdrawal
        self.history.append(transaction)  # Append the transaction
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_overdraft(self):
        """Method specific to CurrentAccount to check overdraft."""
        if self._balance < 0:
            print(
                f"Overdraft used: {-self._balance}. Overdraft limit: {self.overdraft_limit}"
            )


# Example Usage

# Savings Account
savings = SavingsAccount("Alice", 1000, interest_rate=0.05)
savings.deposit(500)
savings.calculate_interest()

# Current Account with overdraft limit
current = CurrentAccount("Bob", 500, overdraft_limit=1500)

# Try withdrawing an amount within the overdraft limit
current.withdraw(
    600
)  # This will work because 500 (balance) + 1500 (overdraft) is enough

# Check the overdraft
current.check_overdraft()

# Print transaction history
print("\nSavings Account History:")
savings.print_history()

print("\nCurrent Account History:")
current.print_history()

# Revert last transaction for both accounts
print("\nReverting last transaction for Savings Account:")
savings.revert_last_transaction()

print("\nReverting last transaction for Current Account:")
current.revert_last_transaction()

# Print history again after reverting
print("\nSavings Account History After Revert:")
savings.print_history()

print("\nCurrent Account History After Revert:")
current.print_history()
