import unittest
from unittest.mock import patch
from bank import BankAccount  # Import the class


class TestBankAccount(unittest.TestCase):

    def test_create_account_with_positive_balance(self):
        """Test account creation with a valid balance"""
        account = BankAccount("Alice", 1000)
        self.assertEqual(account.balance, "The account balance is 1000")

    def test_create_account_with_zero_balance(self):
        """Test that creating an account with zero balance raises an error"""
        with self.assertRaises(ValueError):
            BankAccount("Bob", 0)

    def test_deposit_positive_amount(self):
        """Test depositing a positive amount"""
        account = BankAccount("Alice", 1000)
        with patch("builtins.print") as mock_print:
            account.deposit(500)
            self.assertEqual(account.balance, "The account balance is 1500")
            mock_print.assert_called_with("Deposited 500 in the account")

    def test_deposit_negative_amount(self):
        """Test depositing a negative amount raises an error"""
        account = BankAccount("Alice", 1000)
        with self.assertRaises(ValueError):
            account.deposit(-100)

    def test_withdraw_valid_amount(self):
        """Test withdrawing a valid amount"""
        account = BankAccount("Alice", 1000)
        with patch("builtins.print") as mock_print:
            account.withdraw(300)
            self.assertEqual(account.balance, "The account balance is 700")
            mock_print.assert_called_with("Withdrew 300 from the account")

    def test_withdraw_insufficient_balance(self):
        """Test withdrawing more than the available balance"""
        account = BankAccount("Alice", 500)
        with self.assertRaises(ValueError):
            account.withdraw(1000)

    def test_set_balance_to_zero(self):
        """Test setting balance to zero raises an error"""
        account = BankAccount("Alice", 1000)
        with self.assertRaises(ValueError):
            account.balance = 0


if __name__ == "__main__":
    unittest.main()
