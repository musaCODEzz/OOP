from abc import ABC, abstractmethod
from datetime import datetime


class Transaction(ABC):
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
    # allows deposits and also revesion
    def execute(self):
        if self.amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        self.account._balance += self.amount
        self.account.history.append(self)
        print(f"Deposited {self.amount}. New balance: {self.account.balance}")
