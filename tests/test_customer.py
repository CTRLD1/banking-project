import unittest

from bank.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.account1 = Customer(1021, 'Danah', 'Alsubaie', 'd1234', has_checking= True, has_savings= True)
        self.account2 = Customer(1033, 'Mishaal', 'Alddosari', '&3M456', has_checking= False, has_savings= True)
        self.account3 = Customer(1044, 'Rakan', 'Almutairi', '#76D96', has_checking= True, has_savings= False)


    def test_customer_with_checking_and_savings(self):
        self.assertIsNotNone(self.account1.checking)
        self.assertIsNotNone(self.account1.savings)


    def test_customer_with_savings_only(self):
        self.assertIsNone(self.account2.checking)
        self.assertIsNotNone(self.account2.savings)
        self.assertEqual(self.account2.savings.balance, 0)


    def test_customer_with_checking_only(self):
        self.assertIsNotNone(self.account3.checking)
        self.assertEqual(self.account3.checking.balance, 0)
        self.assertIsNone(self.account3.savings)

    # password verification tests
    def test_verify_pass(self):
        self.assertTrue(self.account1.verify_pass('d1234'))
        self.assertFalse(self.account2.verify_pass('ssd876'))

    # deposit tests
    def test_deposit_to_checking(self):
        self.account1.deposit('checking', 300)
        self.assertEqual(self.account1.checking.balance, 300)

    def test_deposit_savings(self):
        self.account1.deposit('savings', 100)
        self.assertEqual(self.account1.savings.balance, 100)

    def test_invalid_deposit_account(self):
        with self.assertRaises(ValueError):
            # account3 does not have a savings accountt
            self.account3.deposit('savings', 100)

    # withdraw tests
    def test_withdraw_to_checking(self):
        self.account1.deposit('checking', 400)
        self.account1.withdraw('checking', 200)
        # 400 - 200 = 200
        self.assertEqual(self.account1.checking.balance, 200)

    def test_withdraw_from_savings(self):
        self.account1.deposit('savings', 300)
        self.account1.withdraw('savings', 100)
        # 300 - 100 = 200
        self.assertEqual(self.account1.savings.balance, 200)

    def test_invalid_withdraw_account(self):
        with self.assertRaises(ValueError):
            # account2 does not have a checking account
            self.account2.withdraw('checking', 30)


    # transfer tests
    def test_transfer_from_checking_to_savings(self):
        self.account1.deposit('checking', 2000)
        self.account1.deposit('savings', 500)

        # fromm checking to savings
        self.account1.transfer_personal_accounts('checking', 'savings', 300)
        # 2000 - 300 = 1700
        self.assertEqual(self.account1.checking.balance, 1700)
        # 500 + 300 = 800
        self.assertEqual(self.account1.savings.balance, 800)
