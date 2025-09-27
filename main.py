from bank.bank_system import BankSystem
from termcolor import colored

# sources:pypi.org & youtube toturial

def main():
    bank = BankSystem('bank.csv')
    print(colored('==Welcome to my ACME Bank!==', 'green'))

    while True:
        print(colored('---Menu---', 'light_grey'))
        print(colored('1- Add new customer', 'light_magenta'))
        print(colored('2- Make a deposit', 'blue'))
        print(colored('3- Make a withdraw', 'light_cyan'))
        print(colored('4- Tansfer btween users', 'green'))
        print(colored('5- Transfer between personal accounts', 'grey'))
        print(colored('6- Logout', 'red'))

        choice = input(colored('Choose a number: ', 'yellow'))

        if choice == '1':
            frst_name = input('Enter your first name: ')
            last_name= input('Enter your last name: ')
            password = input('Enter password: ')
            customer = bank.add_customer(frst_name, last_name, password)
            print('customer added successfully!')

        elif choice == '2':
            try:
                account_id = int(input('Enter account ID: '))
                password = input('Enter password: ')
                account_type = input('choose account type (checking/savings): ')
                amount = float(input('Enter amount: '))
                customer = bank.deposit(account_id, password, account_type, amount)
                print(f'deposit succesfull! new {account_type} balance: {getattr(customer, account_type).balance}')

            except Exception as err:
                print('error: ', err)


        elif choice == '3':
            try:
                account_id = int(input('account ID: '))
                password = input('Enter password: ')
                account_type = input('choose account type (checking/savings): ')
                amount = float(input('Enter amount: '))
                customer = bank.withdraw(account_id, password, account_type, amount)
                print(f'withdraw succesfull! new {account_type} balance: {getattr(customer, account_type).balance}')

            except Exception as err:
                print('error: ', err)


        elif choice == '4':
            try:
                sender_id = int(input('sender ID: '))
                password = input('Enter password: ')
                sender_type = input('sender account: (checking/savings): ')
                receiver_id = int(input('receiver ID: '))
                receiver_type = input('receiver account: (checking/savings): ')
                amount = float(input('Enter amount: '))
                bank.transfer_between_useres(sender_id, password, sender_type, receiver_id, receiver_type, amount)
                print('transfer successful!')

            except Exception as err:
                print('error:', err)


        elif choice == '5':
            try:
                account_id = int(input('account ID: '))
                password = input('Enter password: ')
                customer = bank.login(account_id, password)
                if not customer:
                    raise ValueError('Invalid login')
                from_type = input('transfer from: (checking/savings): ')
                to_type = input('transfer to: (checking/savings)')
                amount = float(input('Enter amount: '))
                customer.transfer_personal_accounts(from_type, to_type, amount)

                bank.update_csv()
                print('personal transfer successfull!')
                print(f'new {from_type} balance: {getattr(customer, to_type).balance}')

            except Exception as err:
                print('error:', err)

        elif choice == '6':
            print('thank you for visiting my bank, goodbye!')
            break

        else: 
            print('invalid choice, try again')


if __name__ == '__main__':
    main()
