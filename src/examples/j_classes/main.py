# main only using bank_account.py
import bank_account

account = bank_account.BankAccount(50)

print(account.get_balance())

print(account)                          #with the __str__ method in the BankAccount class, will produced the designated string output

#main using menu.py & bank_account.py 
import menu 

menu.run_menu(account)   

