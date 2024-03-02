import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''

#Dont forget to change where the code is FROM & IMPORTed code & SUITE

from tests.homework.h_strings import tests_strings
suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
unittest.TextTestRunner(verbosity=2).run(suite)
