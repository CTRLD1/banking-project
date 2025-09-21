class Account:
    def __init__(self, account_type: str, balance: float=0.0):
        self.account_type = account_type
        self.balance = float(balance)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError('amount should be positive')
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError('amount should be positive')
        if amount > self.balance:
            raise ValueError('credit is insufficent')
        self.balance -= amount

    def __str__(self):
        return (f'{self.account_type} SAR{self.balance}')
    




if __name__ == '__main__':
    # this is where the user faceing "program" goes
    account1= Account('Checking', 100)

    account1.deposit(200)
    print(account1)

    account1.withdraw(50)
    print(account1)

    try:
        account1.withdraw(300)
    except ValueError as err:
        print(err)

        
    