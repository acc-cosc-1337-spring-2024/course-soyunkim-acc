def test_config():
    return True

def create_dictionary():
    prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
    print(prog_langs['C++'])                                                    #calling the key
    print(prog_langs['C#'])
    #print(prog_langs['c++']) generates a keyError, key sensitive
    #cannot use numeric index, as not ordered

def find_keys_in_dictionary_with_in(key, prog_langs):

    if key in prog_langs:
        print(prog_langs[key])
    else:
        print(key, 'key not in dictionary')

def find_keys_in_dictionary_with_not_in(key, value, prog_langs):

    if key not in prog_langs:
        print(key, 'key not in dictionary')
    else:
        print(prog_langs[key])

def add_key_pairs_to_dictionary(key, value, prog_langs):
    prog_langs[key] = value

def delete_from_dictionary(key, prog_langs):
    del prog_langs[key]

def display_menu():
    print('1-Add key pair')
    print('2-Delete key pair')
    print('3-Display dictionary')
    print('4-Get length')
    print('5-Exit')

def run_menu(prog_langs):
    
    choice = -1

    while (choice != 5):
        display_menu()
        choice = int(input("Enter choice: "))
        handle_menu_option(choice, prog_langs)


def handle_menu_option(choice, prog_langs):
    if choice == 1:
        key = input('Enter key: ')
        value = input('Enter value: ')
        add_key_pairs_to_dictionary(key, value, prog_langs)
    elif choice == 2:
        key = input('Enter key: ')
        delete_from_dictionary(key, prog_langs)
    elif choice ==3:
        print(prog_langs)
    elif choice == 4:
        print(len(prog_langs))
    elif choice == 5:
        print('Exiting')
    else:
        print('Invalid option')
   

def loop_dictionary_for():
    prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
    for current_key in prog_langs:
        print(current_key, prog_langs[current_key])

def get_dictionary_keys(): 
    prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
    keys = prog_langs.keys()
    print(keys)

def use_get_dictionary_keys_in_loop():
    prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}

    for key in prog_langs.keys():
        print(prog_langs[key])

def get_dictionary_values():
    prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
    values = prog_langs.values()

    for values in values:
        print(values)

