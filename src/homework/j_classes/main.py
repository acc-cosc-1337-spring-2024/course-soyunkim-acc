from class_a import Die

def run_menu():

    choice = 'Y'

    while choice.upper() != 'N':
        choice = input('Would you like to roll the dice? Y/N ')
        handle_menu_option(choice)

def handle_menu_option(choice):
    die = Die()

    if choice.upper() == 'Y':
        die.roll()
        print(die)
    elif choice.upper() == 'N':
        print('Exiting...')
    else: 
        print('Invalid choice. Please pick Y/N')

run_menu()
