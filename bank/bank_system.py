import csv 
from bank.customer import Customer

class BankSystem:
    def __init__(self, file_path='bank.csv'):
        self.file_path = file_path
        self.customers = self.load_customers()
    
    # dictReader source:https://docs.python.org/3/library/csv.html
    def load_customers(self):
        customers = []
        with open(self.file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                c = Customer(
                    int(row['account_id']),
                    row['frst_name'].strip(),
                    row['last_name'].strip(),
                    row['password'].strip(),
                    has_checking=True,
                    has_savings=True,
                )
                c.checking.balance = float(row['balance_checking'])
                c.savings.balance= float(row['balance_savings'])
                c.checking.is_active = row.get('status_checking', 'active') == 'active'
                c.savings.is_active = row.get('status_savings', 'active') == 'active'
                customers.append(c)
        return customers
    
    def update_csv(self):
        with open(self.file_path, 'w', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(['account_id', 'frst_name', 'last_name', 'password', 'balance_checking', 'balance_savings', 'status_checking', 'status_savings'])

            for c in self.customers:
                writer.writerow([
                    c.account_id,
                    c.frst_name,
                    c.last_name,
                    c.password,
                    c.checking.balance if c.checking else 0,
                    c.savings.balance if c.savings else 0,
                    'active' if c.checking and c.checking.is_active else 'inactive',
                    'active' if c.savings and c.savings.is_active else 'inactive',
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
                            new_customer.savings.balance if new_customer.savings else 0,
                            'active' if new_customer.checking and new_customer.checking.is_active else 'inactive',
                            'active' if new_customer.savings and new_customer.savings.is_active else 'inactive',])
        return new_customer
    

    # Login method
    def login(self, account_id, password):
        account_id = int(account_id)
        password = password.strip()
        for c in self.customers:
            if c.account_id  == account_id and c.verify_pass(password):
             return c
        return None
    
    # Deposit Money into Account (required login) 
    def deposit(self, account_id, password, account_type, amount):
        customer = self.login(account_id, password)
        if customer:
            customer.deposit(account_type, amount)
            self.update_csv()
            return customer
        else:
            raise ValueError('Invalid login')
        
    # Withdraw Money from Account (required login)
    def withdraw(self, account_id, password, account_type, amount):
        customer = self.login(account_id, password)
        if customer:
            customer.withdraw(account_type, amount)
            self.update_csv()
            return customer
        else:
            raise ValueError('Invalid login')
        
    # Transfer Money Between Users (required login)
    def transfer_between_useres(self, sender_id, sender_pass, sender_type, receiver_id, receiver_type, amount):
        sender = self.login(sender_id, sender_pass)
        receiver = None
        for c in self.customers:
            if c.account_id == receiver_id:
                receiver = c
                break 
        if sender and receiver:
            sender.withdraw(sender_type, amount)
            receiver.deposit(receiver_type, amount)
            self.update_csv()
        else:
            raise ValueError('Invalid transfer, login failed or receiver not found')



if __name__ == '__main__':
    bank = BankSystem('bank.csv')
    # bank.add_customer('Danah', 'Alsubaie', 'd1234')

    # Testing login method
    customer = bank.login(10001, 'juagw362')
    if customer:
        print('login succesful:')
    else:
        print('invalid login')

    #Testing login (deposit) method, worked!
    # try:
    #     update_customer = bank.deposit(10001, 'juagw362', 'checking', 500)
    #     print(f'deposit succcesful, updated checking balance: {update_customer.checking.balance}')
    # except ValueError as err:
    #     print('Error: ',err)

    # Testing login (withdraw) method, worked!
    # try:
    #     update_customer = bank.withdraw(10002, 'idh36%@#FGd', 'checking', 100)
    #     print(f'withdraw succcesful, updated checking balance: {update_customer.checking.balance}')
    # except ValueError as err:
    #     print('Error: ',err )


    #Testing transfer between useres 10005 and 10006
    # bank.transfer_between_useres(sender_id=10005, sender_pass='d^dg23g)@', sender_type='checking',
    #                              receiver_id=10006, receiver_type='savings', amount= 1000
    #                              )
    # print('Transfer successful')