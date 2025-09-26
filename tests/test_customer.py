import unittest

from bank.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer(1021, 'Danah', 'Alsubaie', 'd1234', has_checking= True, has_savings= True)
        self.customer2 = Customer(1033, 'Mishaal', 'Alddosari', '&3M456', has_checking= False, has_savings= True)
        self.customer3 = Customer(1044, 'Rakan', 'Almutairi', '#76D96', has_checking= True, has_savings= False)


    def test_customer_with_checking_and_savings(self):
        self.assertIsNotNone(self.customer1.checking)
        self.assertIsNotNone(self.customer2.savings)


    def test_customer_with_savings_only(self):
        self.assertIsNone(self.customer2.checking)
        self.assertIsNotNone(self.customer2.savings)
        self.assertEqual(self.customer2.savings.balance, 0)


    def test_customer_with_checking_only(self):
        self.assertIsNotNone(self.customer3.checking)
        self.assertEqual(self.customer3.checking.balance, 0)
        self.assertIsNone(self.customer3.savings)

    # password verification tests
    def test_verify_pass(self):
        self.assertTrue(self.customer1.verify_pass('d1234'))
        self.assertFalse(self.customer2.verify_pass('ssd876'))

    # deposit tests
    def test_deposit_to_checking(self):
        self.customer1.deposit('checking', 300)
        self.assertEqual(self.customer1.checking.balance, 300)

    def test_deposit_savings(self):
        self.customer1.deposit('savings', 100)
        self.assertEqual(self.customer1.savings.balance, 100)

    def test_invalid_deposit_account(self):
        with self.assertRaises(ValueError):
            # account3 does not have a savings accountt
            self.customer3.deposit('savings', 100)

    # withdraw tests
    def test_withdraw_to_checking(self):
        self.customer1.deposit('checking', 400)
        self.customer1.withdraw('checking', 200)
        # 400 - 200 = 200
        self.assertEqual(self.customer1.checking.balance, 200)

    def test_withdraw_from_savings(self):
        self.customer1.deposit('savings', 300)
        self.customer1.withdraw('savings', 100)
        # 300 - 100 = 200
        self.assertEqual(self.customer1.savings.balance, 200)

    def test_invalid_withdraw_account(self):
        with self.assertRaises(ValueError):
            # customer2 does not have a checking account
            self.customer2.withdraw('checking', 30)


    # transfer tests
    def test_transfer_from_checking_to_savings(self):
        self.customer1.deposit('checking', 2000)
        self.customer1.deposit('savings', 500)

        # fromm checking to savings
        self.customer1.transfer_personal_accounts('checking', 'savings', 300)
        # 2000 - 300 = 1700
        self.assertEqual(self.customer1.checking.balance, 1700)
        # 500 + 300 = 800
        self.assertEqual(self.customer1.savings.balance, 800)
     
    def test_transfer_from_savings_to_checking(self):
        self.customer1.deposit('checking', 500)
        self.customer1.deposit('savings', 1000)
        
        # from savings to checking
        self.customer1.transfer_personal_accounts('savings','checking', 100 )
        # 1000 - 100 =900
        self.assertEqual(self.customer1.savings.balance, 900)
        # 500 + 100 =600
        self.assertEqual(self.customer1.checking.balance, 600)
    
    def test_invalid_transfer(self):
        with self.assertRaises(ValueError):
            # customer1 does not have 'emergency account' only has 2 accounts: checking & savings
            self.customer1.transfer_personal_accounts('checking', 'emergency account', 50)


    # Overdraft tests 
    def test_if_overdraft_fee_applied_on_checking(self):
        self.customer3.checking.overdraft_protect(50)
        # 0 - 50 -35 = -85
        self.assertEqual(self.customer3.checking.balance, -85)
        self.assertEqual(self.customer3.checking.overdraft_times, 1)
        self.assertTrue(self.customer3.checking.is_active)


if __name__ == '__main__':
    unittest.main()