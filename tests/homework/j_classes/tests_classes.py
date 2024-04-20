import unittest
from src.homework.j_classes.class_a import Die

class Test_Die(unittest.TestCase):
    def test_rolled_value_from_1_to_6(self):
        die = Die()

        for i in range(4):
            die.roll()
            self.assertEqual(1 <= die.get_rolled_value() <= 6, True)
            