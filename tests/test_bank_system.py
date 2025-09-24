import unittest

from bank.bank_system import BankSystem


class TestBankSystem(unittest.TestCase):
    def setUp(self):
        self.bank = BankSystem('bank.csv')
        
    def test_load_customers(self):
        custemers = self.bank.customers
        self.assertEqual(len(custemers), 5)

        self.assertEqual(custemers[0].frst_name, 'suresh')
        self.assertEqual(custemers[0].last_name, 'sigera')
        self.assertEqual(custemers[0].checking.balance, 1000)
        self.assertEqual(custemers[0].savings.balance, 10000)
         
        