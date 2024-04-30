import random


def display_menu():
    print('1 - Display Balance')
    print('2 - Deposit')
    print('3 - Withdraw')
    print('4 - Exit')

def run_menu(atm):

    choice = '-1'

    while(choice != '4'):
        display_menu()
        choice = input('Enter menu option: ')
        handle_menu_option(choice, atm.get_bank_account())


def handle_menu_option(choice, account):

    if (choice == '1'):
        print (account.get_balance())

    elif(choice == '2'):
        amount = int(input('Enter deposit amount: '))
        account.deposit(amount)

    elif (choice == '3'):
        amount = float(input('Enter withdraw amount: '))
        account.withdraw(amount)

    elif(choice == '4'):
        print('Exiting...')

    else:
        print('Invalid option')


def update_account(account):
    account.deposit(50)
