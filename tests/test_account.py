import unittest

from bank.account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('checking', 500)
        # self.account2 = Account ('checking', 0)
        
    def test_make_account(self):
        self.assertEqual(self.account.account_type, 'checking')
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
            self.account.withdraw(0)
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)

    # overdraft protection tests
    def test_first_overdraft(self):
       account2 = Account ('checking', 0)
       account2.overdraft_protect(50)
       # 0 - 50 = -50
       # -50 - 35 = -85
       self.assertEqual(account2.balance, -85)
       self.assertEqual(account2.overdraft_times, 1)
       self.assertTrue(account2.is_active)

    def test_second_overdraft_deactivate(self):
        account2 = Account ('checking', 0)
        account2.overdraft_protect(50)
        account2.overdraft_protect(10)
        self.assertFalse(account2.is_active)
        self.assertEqual(account2.overdraft_times, 2)

    def test_trying_to_withdraw_after_deactivate(self):
        account2 = Account ('checking', 0)
        account2.overdraft_protect(50)
        account2.overdraft_protect(5)
        with self.assertRaises(ValueError):
            account2.overdraft_protect(10)

    def test_reactivate_after_deposit(self):
        account2 = Account('checking', 0)
        account2.overdraft_protect(50)
        account2.overdraft_protect(5)
        account2.deposit(200)
        self.assertTrue(account2.is_active)

    def test_cant_go_below_negative_100(self):
        account2 = Account('checking', 0)
        with self.assertRaises(ValueError):
            account2.overdraft_protect(120)

    def test_prevent_withdraw_over_100_when_negative(self):
        account2 = Account('checking', 0)
        account2.overdraft_protect(50)
        with self.assertRaises(ValueError):
            account2.overdraft_protect(150)


if __name__ == '__main__':
    unittest.main()