import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''

#Dont forget to change where the code is FROM & IMPORTed code & SUITE

from tests.examples.g_lists_and_tuples import tests_lists_and_tuples
suite = unittest.TestLoader().loadTestsFromModule(tests_lists_and_tuples)
unittest.TextTestRunner(verbosity=2).run(suite)
