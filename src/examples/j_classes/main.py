# main only using bank_account.py
import bank_account
import atm
import menu 

account = bank_account.BankAccount(50)
my_atm = atm.ATM(account)

menu.run_menu(my_atm)

print(account)
