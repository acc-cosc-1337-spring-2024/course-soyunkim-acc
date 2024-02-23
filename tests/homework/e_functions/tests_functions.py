import unittest

from src.homework.e_functions.value_return import get_hours, get_minutes, get_seconds

class Test_Config(unittest.TestCase):
    
    def test_get_hours(self):
        self.assertEqual(get_hours(3800), 1)
        self.assertEqual(get_hours(3600), 1)

    def test_get_minutes(self):
        self.assertEqual(get_minutes(3800), 3)
        self.assertEqual(get_minutes(3600), 0)
    
    def test_get_seconds(self):
        self.assertEqual(get_seconds(3800), 20)
        self.assertEqual(get_seconds(3600), 0)
