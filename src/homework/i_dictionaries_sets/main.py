import dictionary

def display_menu():
    print('Menu\n'
        '1 - Add or Update Item\n'
        '2 - Delete Item\n'
        '3 - Exit')
    
def run_menu(inventory):

    option = 0

    while (option != 3):
        display_menu()
        option = int(input("Enter option number: "))
        handle_menu_option(option, inventory)

def handle_menu_option(option, inventory):
    if option == 1:
        widget_add = input("Enter widget to add: ")
        quantity = int(input("Enter the quantity of the widget: "))
        dictionary.add_inventory(widget_add, quantity, inventory)
        print('Widget added')

    elif option == 2:
        widget_remove = input("Enter widget to delete: ")
        result = dictionary.remove_inventory_widget(widget_remove, inventory)
        print(result)

    elif option == 3:
        print('Exiting')

    else:
        print('Invalid option')


inventory = {}
run_menu(inventory)