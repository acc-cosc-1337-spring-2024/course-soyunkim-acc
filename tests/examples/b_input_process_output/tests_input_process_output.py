import unittest

from src.examples.b_input_proc_output.input_process_output import add_values, floating_point_division, get_remainder, integer_division, operator_precedence_1, operator_precedence_2, power_function, test_config
    #don't forget to import!
class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
    
    def test_add_numbers(self):
        self.assertEqual(add_values(3, 4), 7)
        self.assertEqual(add_values(10.99, 1.50), 12.49)
        self.assertEqual(add_values("12.49", "1.50"), "12.491.50")


    def test_floating_point_division_1(self):
        self.assertEqual(floating_point_division(5, 2), 2.5)

    def test_floating_point_division_2(self):
        self.assertEqual(floating_point_division(20, 8), 2.5)

    def test_integer_division_1(self):
        self.assertEqual(integer_division(20, 8), 2)
        
    def test_operator_precedence_1(self):
        self.assertEqual(operator_precedence_1(12, 6, 3), 14)
        
    def test_operator_precedence_2(self):
        self.assertEqual(operator_precedence_2(12, 6, 3), 6)

    def test_power_function(self):
        self.assertEqual(power_function(2, 3), 8)

    def test_get_remainder(self):
        self.assertEqual(get_remainder(2, 2), 0)