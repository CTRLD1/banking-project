class Account:
    def __init__(self, account_type: str, balance: float=0.0):
        self.account_type = account_type
        self.balance = float(balance)
        self.overdraft_times = 0
        self.is_active = True

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self.balance += amount

        # reactivate the account if the customer brings the account current
        if self.balance >= 0:
           self.is_active = True


    def withdraw(self, amount: float):
        # if amount <= 0:
        #     raise ValueError('amount must be positive')
        # if amount > self.balance:
        #     raise ValueError('credit is insufficent')
        # self.balance -= amount

        self.overdraft_protect(amount)


    def overdraft_protect(self, amount: float):
        if not self.is_active:
            raise ValueError('sorry mate, account is deactivated due to overdrafts')
        
        if amount <= 0:
            raise ValueError('amount must be positive')
        # prevent customer from withdrawing more than $100 USD if account is currently negative
        if self.balance < 0 and amount > 100:
            raise ValueError('can NOT withdraw more than SAR100 when account is negative')
        # the account cannot have a resulting balance of less than -$100
        if self.balance - amount < -100:
            raise ValueError('can NOT go bellow -100')
        
        self.balance -= amount

        # charge customer ACME overdraft protection fee of $35 when overdraft
        if self.balance < 0:
            self.balance -= 35
            self.overdraft_times += 1

        # deactivate the account after 2 overdrafts
        if self.overdraft_times >= 2:
            self.is_active = False



    def __str__(self):
        return (f'{self.account_type} SAR{self.balance}')
    




if __name__ == '__main__':
    # this is where the user faceing "program" goes
    account1= Account('checking', 100)

    account1.deposit(200)
    print(account1)

    account1.withdraw(50)
    print(account1)

    try:
        account1.withdraw(300)
    except ValueError as err:
        print(err)

    account2= Account('checking', 0)
    try:
        # 0 - 50 = -50
        # overdraft fee: 35
        # -50 - 35 = -85
        account2.overdraft_protect(50)
        print(f'balance AFTER first overdraft: {account2.balance}')
    except ValueError as err:
        print(err)

    try:
        # -85 - 5 = -90
        # overdraft fee: 35
        # -90 - 35 = -125
        account2.overdraft_protect(5)
        print(f'balance AFTER second overdraft: {account2.balance}')
    except ValueError as err:
        print(err)

    
    try:
        account2.overdraft_protect(50)
    except ValueError as err:
        print(err)
    
        account2.deposit(200)
        print(f'balance AFTER deposit: {account2.balance} active?: {account2.is_active}')
