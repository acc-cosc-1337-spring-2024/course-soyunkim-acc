import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''

#Dont forget to change where the code is FROM & IMPORTed code & SUITE

from tests.examples.c_decisions import tests_decisions
suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)
unittest.TextTestRunner(verbosity=2).run(suite)
