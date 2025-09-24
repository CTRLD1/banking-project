import csv 
from bank.customer import Customer

class BankSystem:
    def __init__(self, file_path='bank.csv'):
        self.file_path = file_path
        self.customers = self.load_customers()

    def load_customers(self):
        customers = []
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
                customers.append(c)
        return customers
    
    def update_csv(self):
        with open(self.file_path, 'w', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(['account_id', 'frst_name', 'last_name', 'password', 'balance_checking', 'balance_savings'])

            for c in self.customers:
                writer.writerow([
                    c.account_id,
                    c.frst_name,
                    c.last_name,
                    c.password,
                    c.checking.balance if c.checking else 0,
                    c.savings.balance if c.savings else 0,
                ])


     # add_customer method
    def add_customer(self, frst_name, last_name, password, save_to_file=True):
        new_account_id = max(c.account_id for c in self.customers) + 1 if self.customers else 10001

        new_customer = Customer(new_account_id, frst_name, last_name, password, has_checking=True, has_savings=True)

        self.customers.append(new_customer)
        if save_to_file:
            with open(self.file_path, 'a', newline='') as f:
                 writer = csv.writer(f)
                 writer.writerow([new_customer.account_id, new_customer.frst_name, new_customer.last_name, new_customer.password,
                            new_customer.checking.balance if new_customer.checking else 0,
                            new_customer.savings.balance if new_customer.savings else 0])
        return new_customer





if __name__ == '__main__':
    bank = BankSystem('bank.csv')
    bank.add_customer('Danah', 'Alsubaie', 'd1234')