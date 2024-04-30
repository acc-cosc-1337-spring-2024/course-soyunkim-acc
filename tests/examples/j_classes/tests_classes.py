import unittest

import random
from src.examples.j_classes.bank_account import BankAccount
from src.examples.j_classes.menu import update_account

class Test_Config(unittest.TestCase):
    def test_account_get_balance(self):
        account = BankAccount(50)
        self.assertEqual(account.get_balance(), 50)

    def test_account_deposit(self):
        account = BankAccount(50)
        self.assertEqual(account.get_balance(), 50)

        account.deposit(100)
        self.assertEqual(account.get_balance(), 150)

    def test_account_withdraw(self):
        account = BankAccount(50)
        self.assertEqual(account.get_balance(), 50)

        account.withdraw(25)
        self.assertEqual(account.get_balance(), 25)

    def test_account_withdraw_w_balance_at_zero(self):
        account = BankAccount(0)
        self.assertEqual(account.get_balance(), 0)

        account.withdraw(1000)
        self.assertEqual(account.get_balance(), 0)

    def test_account_w_deposits_and_withdraws(self):
        account = BankAccount(50)
        self.assertEqual(account.get_balance(), 50)
        
        account.deposit(500)
        self.assertEqual(account.get_balance(), 550)

        account.withdraw(100)
        self.assertEqual(account.get_balance(), 450)

    def test_account_function_parameter_works_w_original_variable(self):
        account = BankAccount(50) #original variable

        update_account(account)
        self.assertEqual(account.get_balance(), 100)

   