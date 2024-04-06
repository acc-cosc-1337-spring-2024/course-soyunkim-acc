import unittest

from src.homework.i_dictionaries_sets.sets import get_students_who_took_prog1_and_prog2, get_students_who_took_prog1_not_prog2, get_students_who_took_prog2_not_prog1, get_students_who_took_prog1_or_prog2

class Test_Config(unittest.TestCase):

    def test_get_students_who_took_prog1_and_prog2(self):
        prog1 = (['Student1', 'Student2', 'Student3'])
        prog2 = (['Student3', 'Student4', 'Student5'])

        result = get_students_who_took_prog1_and_prog2(prog1, prog2)
        self.assertEqual(result, {'Student3'})

    def test_get_students_who_took_prog1_or_prog2(self):
        prog1 = (['Student1', 'Student2', 'Student3'])
        prog2 = (['Student3', 'Student4', 'Student5'])

        result = get_students_who_took_prog1_or_prog2(prog1, prog2)
        self.assertEqual(result, {'Student1', 'Student2', 'Student3', 'Student4', 'Student5'})

    def test_get_students_who_took_prog1_not_prog2(self):
        prog1 = (['Student1', 'Student2', 'Student3'])
        prog2 = (['Student3', 'Student4', 'Student5'])

        result = get_students_who_took_prog1_not_prog2(prog1, prog2)
        self.assertEqual(result, {'Student1', 'Student2'})

    def test_get_students_who_took_prog2_not_prog1(self):
        prog1 = (['Student1', 'Student2', 'Student3'])
        prog2 = (['Student3', 'Student4', 'Student5'])
        
        result = get_students_who_took_prog2_not_prog1(prog1, prog2)
        self.assertEqual(result, {'Student4', 'Student5'})