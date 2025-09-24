import csv 
from bank.customer import Customer

class BankSystem:
    def __init__(self, file_path='bank.csv'):
        self.file_path = file_path
        self.customers = self.load_customers()

    def load_customers(self):
        custmers = []
        with open(self.file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                c = Customer(
                    int(row['account_id']),
                    row['frst_name'],
                    row['last_name'],
                    row['password'],
                    has_checking=True,
                    has_savings=True,
                )
                c.checking.balance = float(row['balance_checking'])
                c.savings.balance= float(row['balance_savings'])
                custmers.append(c)
        return custmers