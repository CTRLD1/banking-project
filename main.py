from bank.bank_system import BankSystem
from termcolor import colored
from alive_progress import alive_bar
import time
import pyfiglet
import pwinput

GREEN = '\033[92m'
RESET = '\033[0m'

# sources:pypi.org & youtube toturial

def banner():
    ascii_banner = pyfiglet.figlet_format('ACME   Bank')
    print(colored(ascii_banner, 'green', attrs=['bold']))
    print(colored('='*40, 'cyan'))
    print(colored('  Welcome to your CLI Banking App  ', 'grey', attrs=['bold']))  
    print(colored('='*40, 'cyan'))

def menu():
    print(colored("╔══════════════════════════════════╗", "cyan"))
    print(colored("║           MAIN  MENU             ║", "grey", attrs=["bold"]))
    print(colored("╠══════════════════════════════════╣", "cyan"))
    print(colored("║ 1. ➕ Add new customer           ║", "green"))
    print(colored("║ 2. 💰 Make a deposit             ║", "blue"))
    print(colored("║ 3. 💸 Make a withdraw            ║", "yellow"))
    print(colored("║ 4. 🔄 Transfer between users     ║", "magenta"))
    print(colored("║ 5. 🔁 Transfer personal accounts ║", "cyan"))
    print(colored("║ 6. 🚪 Logout                     ║", "red"))
    print(colored("╚══════════════════════════════════╝", "cyan"))

def main():
    banner()
    bank = BankSystem('bank.csv')

    while True:
        menu()
        choice = input(colored('Choose a number: ', 'yellow'))

        if choice == '1':
            frst_name = input('Enter your first name: ')
            last_name= input('Enter your last name: ')
            password = pwinput.pwinput(prompt='Enter password: ', mask='*')
            savings_choice=input('Do you want a savings account? (yes/no): ')
            has_savings = savings_choice == 'yes'

            print(colored('Creating customer account...', 'light_cyan'))
            print(GREEN, end="")
            with alive_bar(100, bar='smooth', length=20) as bar:
                for _ in range(100):
                    time.sleep(0.05)
                    bar()
            print(RESET)
            customer = bank.add_customer(frst_name, last_name, password, has_savings=has_savings)
            print('Customer added successfully!')
            print(colored('-- Customer Information--', 'cyan'))
            print(f'ID: {customer.account_id}')
            print(f'Name: {customer.frst_name} {customer.last_name}')

            if customer.checking:
               print(f"Checking Account: Active | Balance: {customer.checking.balance}")
            else:
               print("Checking Account: Not created")
    
            if customer.savings:
               print(f"Savings Account: Active | Balance: {customer.savings.balance}")
            else:
               print("Savings Account: Not created")


        elif choice == '2':
            try:
                account_id = int(input('Enter account ID: '))
                password = pwinput.pwinput(prompt='Enter password: ', mask='*')
                account_type = input('choose account type (checking/savings): ')
                amount = float(input('Enter amount: '))

                print(colored('Processing deposit...', 'light_cyan'))
                print(GREEN, end="")
                with alive_bar(100, bar='smooth', length=20) as bar:
                  for _ in range(100):
                    time.sleep(0.05)
                    bar()
                print(RESET)

                customer = bank.deposit(account_id, password, account_type, amount)
                print(f'deposit succesfull! new {account_type} balance: {getattr(customer, account_type).balance}')

            except Exception as err:
                print('error: ', err)


        elif choice == '3':
            try:
                account_id = int(input('account ID: '))
                password = pwinput.pwinput(prompt='Enter password: ', mask='*')
                account_type = input('choose account type (checking/savings): ')
                amount = float(input('Enter amount: '))

                print(colored('Processing withdraw...', 'light_cyan'))
                print(GREEN, end="")
                with alive_bar(100, bar='smooth', length=20) as bar:
                  for _ in range(100):
                    time.sleep(0.05)
                    bar()
                print(RESET)

                customer = bank.withdraw(account_id, password, account_type, amount)
                print(f'withdraw succesfull! new {account_type} balance: {getattr(customer, account_type).balance}')

            except Exception as err:
                print('error: ', err)


        elif choice == '4':
            try:
                sender_id = int(input('sender ID: '))
                password = pwinput.pwinput(prompt='Enter password: ', mask='*')
                sender_type = input('sender account: (checking/savings): ')
                receiver_id = int(input('receiver ID: '))
                receiver_type = input('receiver account: (checking/savings): ')
                amount = float(input('Enter amount: '))

                print(colored('Processing transfer...', 'light_cyan'))
                print(GREEN, end="")
                with alive_bar(100, bar='smooth', length=20) as bar:
                  for _ in range(100):
                    time.sleep(0.05)
                    bar()
                print(RESET)

                bank.transfer_between_useres(sender_id, password, sender_type, receiver_id, receiver_type, amount)
                print('transfer successful!')

            except Exception as err:
                print('error:', err)


        elif choice == '5':
            try:
                account_id = int(input('account ID: '))
                password = pwinput.pwinput(prompt='Enter password: ', mask='*')
                customer = bank.login(account_id, password)
                if not customer:
                    raise ValueError('Invalid login')
                from_type = input('transfer from: (checking/savings): ')
                to_type = input('transfer to: (checking/savings)')
                amount = float(input('Enter amount: '))

                print(colored('Processing transfer...', 'light_cyan'))
                print(GREEN, end="")
                with alive_bar(100, bar='smooth', length=20) as bar:
                  for _ in range(100):
                    time.sleep(0.05)
                    bar()
                print(RESET)

                customer.transfer_personal_accounts(from_type, to_type, amount)

                bank.update_csv()
                print('personal transfer successfull!')
                print(f'new {from_type} balance: {getattr(customer, to_type).balance}')

            except Exception as err:
                print('error:', err)

        elif choice == '6':
            print(colored('thank you for visiting my bank, goodbye!🫡', 'light_grey'))
            break

        else: 
            print('invalid choice, try again')

if __name__ == '__main__':
    main()
