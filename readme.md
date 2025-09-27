# ACME Bank System 🏦

## Overview
This project is a simple banking system built with python. It allows users to:
💸 Create accounts (checking or savings or BOTH)
💸 Deposit and withdraw money
💸 Transfer between personal accounts 
💸 Transfer between different users
💸 Automatically update the data in a CSV file


## Exaample of code
Here is a snippet of the update_csv method that keeps the customer data updated!
```python
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
 ```


 ## What i learned
 📝 How to use OOP in python
 📝 How to handle CSV files for saving and loading data
 📝 How to implement different functionality like login, withdraw and transfer
 📝 How to unit test multiple classes and think of all possible cases 
 📝 Overdraft protection logic
 📝 Error and exception handling 
 📝 Building a Command-Line Interface (CLI) to interact with the banking system