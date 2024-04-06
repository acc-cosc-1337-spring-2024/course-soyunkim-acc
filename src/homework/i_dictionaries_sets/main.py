import sets

def display_menu():
    print('Menu\n'
          '1 - Students who took prog1 and prog2\n'
          '2 - Students who took prog1 or prog2\n'
          '3 - Students who took prog1 not prog2\n'
          '4 - Students who took prog2 not prog1\n'
          '5 - Exit')

def run_menu(prog1, prog2):

    option = 0 
    while option != 5:
        display_menu()
        option = int(input('Enter option number for function: '))
        handle_menu_option(option, prog1, prog2)

def handle_menu_option(option, prog1, prog2):
    if option == 1:
        print('Students who took prog1 & prog2: ', sets.get_students_who_took_prog1_and_prog2(prog1, prog2))

    elif option == 2:
        print('Students who took prog1 or prog2: ', sets.get_students_who_took_prog1_or_prog2(prog1, prog2))
        
    elif option == 3:
        print('Students who took prog1 not prog2: ' ,sets.get_students_who_took_prog1_not_prog2(prog1, prog2))

    elif option == 4:
        print('Students who took prog2 not prog1: ', sets.get_students_who_took_prog2_not_prog1(prog1, prog2))
    
    elif option == 5:
        print('Exiting...')
    else:
        print('Invalid option')

prog1 = (['Student1', 'Student2', 'Student3'])
prog2 = (['Student3', 'Student4', 'Student5'])

run_menu(prog1, prog2)