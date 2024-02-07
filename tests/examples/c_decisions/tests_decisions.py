import unittest

from src.examples.c_decisions.decisions import get_and_result, get_not_result, get_or_result, is_even, is_odd, is_vowel, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_and_truth_table(self):
        self.assertEqual(get_and_result(True, True), True)
        self.assertEqual(get_and_result(True, False), False)
        self.assertEqual(get_and_result(False, True), False)
        self.assertEqual(get_and_result(False, False), False)

    def test_or_truth_table(self):
        self.assertEqual(get_or_result(True, True), True)
        self.assertEqual(get_or_result(True, False), True)
        self.assertEqual(get_or_result(False, True), True)
        self.assertEqual(get_or_result(False, False,), False)

    def test_not_truth_table(self):
        self.assertEqual(get_not_result(True), False)
        self.assertEqual(get_not_result(False), True)

    def test_is_even(self):
        self.assertEqual(is_even(1), False)
        self.assertEqual(is_even(2), True)

    def tes_odd_even(self):
        self.assertEqual(is_odd(5), True)
        self.assertEqual(is_odd(2), False)

    def tet_is_vowel(self):
        self.assertEqual(is_vowel('u'), True)
        self.assertEqual(is_vowel(b), False)
        
        

