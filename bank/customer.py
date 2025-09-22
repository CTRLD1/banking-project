from bank.account import Account

class Customer:
    def __init__(self, account_id, first_name, last_name, password, has_checking = True, has_savings = True ):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

        # George's recommendation: "I’d just put None in any account that the user didn’t have. This way a user can have 0 without the account being ‘closed’".
        self.checking = Account('checking') if has_checking else None
        self.savings = Account('savings') if has_savings else None


    # to verify if password T or F
    def verify_pass(self, password):
        return self.password == password
    
    
    # As a user, I want to open a savings account so that I can deposit money into my savings
    def deposit(self, account_type, amount):
        if account_type == 'checking' and self.checking:
            self.checking.deposit(amount)
        elif account_type == 'savings' and self.savings:
            self.savings.deposit(amount)
        else:
            raise ValueError ('account does not exist')
    
    # As a user, I want to open a savings account so that I can withdraw money from my savings
    def withdraw(self, account_type, amount):
        if account_type == 'checking' and self.checking:
            self.checking.withdraw(amount)
        elif account_type == 'savings' and self.savings:
            self.savings.withdraw(amount)
        else: 
            raise ValueError ('account does not exist')


    def __str__(self):
        return (f'{self.account_id}: {self.first_name} {self.last_name}')
    



if __name__ == '__main__':
    # this is where the user faceing "program" goes
    customer1= Customer(1021, 'Danah', 'Alsubaie', '1234', has_checking= True, has_savings= False)
    print(customer1)
    print('checking account:', customer1.checking)
    print('savings account:', customer1.savings)


    # testing verify pass
    print(customer1.verify_pass('1234'))
    print(customer1.verify_pass('3214'))


    # testing deposit method
    customer1.deposit('checking', 100)
    print(f'Current balance after deposit: {customer1.checking.balance}')


    # testing withdraw
    customer1.withdraw('checking', 50)
    print(f'Current balance after withdraw: {customer1.checking.balance}')


    # testing raised errors (customer1 does not have a savings account )
    try:
        customer1.deposit('savings', 200)
    except ValueError as err:
        print (err)

