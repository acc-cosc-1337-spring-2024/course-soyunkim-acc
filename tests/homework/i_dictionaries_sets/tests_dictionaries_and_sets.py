import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory = {}

        add_inventory('widget1', 10, inventory)
        self.assertEqual(inventory['widget1'], 10)

        add_inventory('widget1', 25, inventory)
        self.assertEqual(inventory['widget1'], 35)

        add_inventory('widget1', -10, inventory)
        self.assertEqual(inventory['widget1'], 25)

    def test_remove_inventory_widget(self):
        inventory = {}
        inventory['widget1'] = 50
        inventory['widget2'] = 100

        result = remove_inventory_widget('widget1', inventory)

        self.assertEqual(result, 'Record deleted')
        self.assertEqual(len(inventory), 1)
        self.assertEqual(inventory['widget2'], 100)