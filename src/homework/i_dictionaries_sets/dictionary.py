def add_inventory(widget_add, quantity, inventory):

    if widget_add in inventory:
        inventory[widget_add] += quantity
    else:
        inventory[widget_add] = quantity

def remove_inventory_widget(widget_remove, inventory):
    if widget_remove in inventory:
        del inventory[widget_remove]
        return 'Record deleted'
    else:
        return 'Item not found'
