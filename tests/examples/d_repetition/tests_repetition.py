import unittest

from src.examples.d_repetition.repetition import get_sum_for, sum_of_square, sum_of_squares_for, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_sum_of_squares(self):
        self.assertEqual(sum_of_square(3), 14)
        self.assertEqual(sum_of_square(4), 30)
        self.assertEqual(sum_of_square(5), 55)

    def test_sum_of_squares_for(self):
        self.assertEqual(sum_of_squares_for(3), 14)
        self.assertEqual(sum_of_squares_for(5), 55)

    def test_sum_for(self):
        self.assertEqual(get_sum_for(3), 6)
        