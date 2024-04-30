class ATM:
    __bank_account = 0

    def __init__(self, bank_account):
        self.__bank_account = bank_account
    
    def display_balance(self):
        print(self.__bank_account.get_balance())

    def make_deposit(self):
        amt = int(input('Amount to deposit: '))
        self.__bank_account.deposit(amt)

    def make_withdraw(self):
        amt = int(input('Enter withdraw amount: '))
        self.__bank_account.withdraw(amt)

    def get_bank_account(self):
        return self.__bank_account
    
