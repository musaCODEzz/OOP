# class BankAccount:

#     def __init__(self, owner, balance=0):
#         if balance > 0:
#             self.owner = owner
#             self._balance = balance
#         else:
#             raise ValueError(
#                 "Balance should be greater than 0 when opening the account"
#             )

#     @property
#     def balance(self):
#         # getter for balance
#         return f"The account balance is {self._balance}"

#     @balance.setter
#     def balance(self, amount):
#         # setter for balance
#         if amount <= 0:
#             raise ValueError("Balance should be greater than 0")
#         self._balance = amount
#         print(f"Balance updated to {self._balance}")

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited {amount} in the account")
#         else:
#             print("Amount should be greater than 0")

#     def withdraw(self, amount):
#         if amount > 0:
#             if self._balance >= amount:
#                 self._balance -= amount
#                 print(f"Withdrew {amount} from the account")
#             else:
#                 print("Insufficient balance")
#         else:
#             print("Amount should be greater than 0")


# account = BankAccount("John", 9000)
# print(account.balance)
# account.balance = 10000
# account.deposit(500)
# print(account.balance)
# account.withdraw(200)
# print(account.balance)


# #########
# class BankAccount:

#     def __init__(self, owner, balance=0):
#         # if balance > 0:
#             self.owner = owner
#             self._balance = balance
#         else:
#             raise ValueError(
#                 "Balance should be greater than 0 when opening the account"
#             )

#     @property
#     def balance(self):
#         # getter for balance
#         return f"The account balance is {self._balance}"

#     @balance.setter
#     def balance(self, amount):
#         # setter for balance
#         if amount <= 0:
#             raise ValueError("Balance should be greater than 0")
#         self._balance = amount
#         print(f"Balance updated to {self._balance}")

#     def deposit(self, amount):
#         if amount < 0:
#             raise ValueError("Deposit must be greater than 0")
#         self._balance += amount
#         print(f"Deposited {amount} in the account")

#     def withdraw(self, amount):
#         if amount < 0:
#             raise ValueError("Withdrawal amount must be greater than 0")
#         if self._balance < amount:
#             raise ValueError("Insufficient balance")
#         self._balance -= amount
#         print(f"Withdrew {amount} from the account")


# class SavingsAccount(BankAccount):
#     def __init__(self, owner, balance=0, interest_rate=3):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self._balance * self.interest_rate / 100
#         return interest


# # Create a BankAccount instance
# account = BankAccount("John", 9000)
# print(account.balance)

# # Update balance
# account.balance = 10000
# account.deposit(500)
# print(account.balance)

# # Withdraw money
# account.withdraw(200)
# print(account.balance)

# # Create a SavingsAccount instance using owner and balance
# interest_account = SavingsAccount("John", 10000)
# interest = interest_account.calculate_interest()
# print(f"The interest accrued is {interest}")  # Print interest as a number
