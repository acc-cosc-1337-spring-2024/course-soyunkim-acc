import unittest

#don't forget to add IMPORT

from src.examples.a_example.devprocess import add_numbers, subtract_numbers

class Test_Config(unittest.TestCase):

#create test function where task = test that add numbers work as expected
# (self) required
# self.assertEqual required

    def test_add_numbers_2(self):
        self.assertEqual(2, add_numbers(1, 1))

    def test_subtract_numbers_1(self):
        self.assertEqual(5, subtract_numbers(10,5))

