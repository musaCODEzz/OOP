from abc import ABC, abstractmethod
from datetime import datetime


class Transaction(ABC):
    """Abstract base class for transactions."""

    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
        self.timestamp = datetime.now()

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def revert(self):
        pass


class DepositTransaction(Transaction):
    """Handles deposits and allows reversion."""

    def execute(self):
        if self.amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        self.account._balance += self.amount
        self.account.history.append(self)  # Append the transaction itself
        print(f"Deposited {self.amount}. New balance: {self.account.balance}")

    def revert(self):
        self.account._balance -= self.amount
        print(f"Reverted deposit of {self.amount}. New balance: {self.account.balance}")
        # Add the reverted deposit transaction to history
        reverted_transaction = DepositTransaction(self.account, -self.amount)
        self.account.history.append(reverted_transaction)


class WithdrawTransaction(Transaction):
    """Handles withdrawals and allows reversion."""

    def execute(self):
        if self.amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        if self.account._balance + self.account.overdraft_limit < self.amount:
            raise ValueError("Insufficient balance and overdraft limit exceeded")

        self.account._balance -= self.amount
        self.account.history.append(self)  # Append the transaction itself
        print(f"Withdrew {self.amount}. New balance: {self.account.balance}")

    def revert(self):
        self.account._balance += self.amount
        print(
            f"Reverted withdrawal of {self.amount}. New balance: {self.account.balance}"
        )
        # Add the reverted withdrawal transaction to history
        reverted_transaction = WithdrawTransaction(self.account, self.amount)
        self.account.history.append(reverted_transaction)


class BankAccount:
    """Represents a general bank account."""

    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.owner = owner
        self._balance = balance
        self.history = []  # Store transaction history

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        transaction = DepositTransaction(self, amount)
        transaction.execute()

    def withdraw(self, amount):
        transaction = WithdrawTransaction(self, amount)
        transaction.execute()

    def print_history(self):
        """Displays transaction history."""
        print(f"\nTransaction History for {self.owner}:")
        for t in self.history:
            print(
                f"{t.timestamp}: {'Deposit' if isinstance(t, DepositTransaction) else 'Withdraw'} {t.amount}"
            )

    def revert_last_transaction(self):
        """Reverts the last transaction in the history."""
        if self.history:
            last_transaction = self.history[-1]
            last_transaction.revert()
            # No need to remove the transaction from history
        else:
            print("No transactions to revert.")


class SavingsAccount(BankAccount):
    """Represents a Savings Account. May apply interest."""

    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # Savings account may have an interest rate

    def apply_interest(self):
        """Apply interest to the savings account balance."""
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest applied: {interest}. New balance: {self.balance}")


class CurrentAccount(BankAccount):
    """Represents a Current Account. May have an overdraft feature."""

    def __init__(self, owner, balance=0, overdraft_limit=1000):
        super().__init__(owner, balance)
        self.overdraft_limit = (
            overdraft_limit  # Current accounts may have an overdraft limit
        )

    def withdraw(self, amount):
        """Override withdraw method to account for overdraft."""
        if self._balance + self.overdraft_limit < amount:
            raise ValueError("Insufficient balance and overdraft limit exceeded")

        self._balance -= amount
        transaction = WithdrawTransaction(
            self, amount
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
savings.apply_interest()

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
