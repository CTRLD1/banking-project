import unittest
import shutil
import os

from bank.bank_system import BankSystem


class TestBankSystem(unittest.TestCase):
    def setUp(self):
        # George: Option 1:Use a seperate csv file for testing delete or overwrite it in the teardown method google 'how to delete file python'
        # i created this temporary 'test_bank.csv' file for testing and to keep my original 'bank.csv' clean
        shutil.copyfile('bank.csv', 'test_bank.csv')
        self.bank = BankSystem('test_bank.csv')
        
    def tearDown(self):
        if os.path.exists('test_bank.csv'):
            os.remove('test_bank.csv')
        
    
    def test_load_customers(self):
        customers = self.bank.customers

        self.assertEqual(customers[0].frst_name, 'suresh')
        self.assertEqual(customers[0].last_name, 'sigera')
        self.assertEqual(customers[0].checking.balance, 1000)
        self.assertEqual(customers[0].savings.balance, 10000)

    # testing add customer methood
    def test_add_customer(self):
        start_count = len(self.bank.customers)
        new_customer = self.bank.add_customer('Danah', 'Alsubaie', 'd1234', save_to_file=True)

        self.assertEqual(len(self.bank.customers), start_count + 1)
        self.assertEqual(new_customer.frst_name, 'Danah')
        self.assertEqual(new_customer.last_name, 'Alsubaie')
        
        # to make sure that the new customer was added in testing and before the tearDown deletes it
        with open('test_bank.csv', 'r') as f:
            lines = f.readlines()
            last_line = lines[-1].strip()
            # print('last line', last_line)

        self.assertIn('Danah', last_line)
        self.assertIn('Alsubaie', last_line)


    # testing Login method
    def test_login_success(self):
        customer = self.bank.login(10002, 'idh36%@#FGd')
        self.assertIsNotNone(customer)
        self.assertEqual(customer.frst_name, 'james')

    def test_invalid_login(self):
        customer = self.bank.login(10002, 'xxoooo3')
        self.assertIsNone(customer)

    # testing deposit (required login)
    def test_deposit_success(self):
        # 9800 + 200 = 10000
        customer = self.bank.deposit(10002,'idh36%@#FGd', 'checking', 200) 
        self.assertEqual(customer.checking.balance, 10000)

    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.bank.deposit(10001, '123546', 'checking', 200)

    # testing withdraw (required login)
    def test_withdraw_success(self):
        # 9800 - 100 = 9700
        customer = self.bank.withdraw(10002,'idh36%@#FGd', 'checking', 100) 
        self.assertEqual(customer.checking.balance, 9700)


    # transfer between users tests
    def test_transfer_between_users(self):
        # transfer from 10005 to 10006
        self.bank.transfer_between_useres(
            sender_id=10005, sender_pass='d^dg23g)@', sender_type='checking',
            receiver_id=10006, receiver_type='savings', 
            amount= 1000
        )

        sender = self.bank.login(10005, 'd^dg23g)@')
        receiver = self.bank.login(10006, 'd1234')
        
        # 99000 - 1000 = 98000
        self.assertEqual(sender.checking.balance, 98000)
        # 1000 + 1000 = 2000
        self.assertEqual(receiver.savings.balance, 2000)


if __name__ == '__main__':
    unittest.main()