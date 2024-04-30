import random


def display_menu():
    print('1 - Display Balance')
    print('2 - Deposit')
    print('3 - Withdraw')
    print('4 - Exit')

def run_menu(account):

    choice = '-1'

    while(choice != '4'):
        display_menu()
        choice = input('Enter menu option: ')
        handle_menu_option(choice, account)


def handle_menu_option(choice, account):

    if (choice == '1'):
        print (account.display_balance())

    elif(choice == '2'):
        amount = int(input('Enter withdraw amount: '))
        account.make_deposit(amount)

    elif (choice == '3'):
        amount = float(input('Enter deposit amount: '))
        account.make_withdraw(amount)

    elif(choice == '4'):
        print('Exiting...')

    else:
        print('Invalid option')


def update_account(account):
    account.deposit(50)
