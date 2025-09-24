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
        pass
        
    
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
        
        # to make sure taht the new customer was added in testing and before the tearDown deletes it
        with open('test_bank.csv', 'r') as f:
            lines = f.readlines()
            last_line = lines[-1].strip()
            print('last line', last_line)

        self.assertIn('Danah', last_line)
        self.assertIn('Alsubaie', last_line)