import unittest

from bank.account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('Checking', 500)
        
    def test_make_account(self):
        self.assertEqual(self.account.account_type, 'Checking')
        self.assertEqual(self.account.balance, 500)

    # here im testing the deposit process
    def test_deposit(self):
        self.account.deposit(50)
        # 500 + 50 = 550
        self.assertEqual(self.account.balance, 550)

    def test_invalid_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)
        with self.assertRaises(TypeError):
            self.account.deposit('Fifty')
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    # here im testing teh withdraw process
    def test_withdraw(self):
        self.account.withdraw(50)
        # 500 - 50 = 450
        self.assertEqual(self.account.balance, 450)

    def test_invalid_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(600)
        with self.assertRaises(TypeError):
            self.account.withdraw('Twenty')
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)
        with self.assertRaises(ValueError):
            self.account.withdraw(0)
        
        

# i will test the __main__ later 