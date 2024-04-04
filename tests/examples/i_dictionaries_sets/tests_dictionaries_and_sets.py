import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_dictionary_key_access(self):
        prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
        self.assertEqual(prog_langs['C++'], '1979')

    def test_dictionary_find_key_with_in(self):                             #check if key exist/ eliminate keyError/ defensive programming
        prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
        self.assertEqual('C++' in prog_langs, True)
        self.assertEqual('c++' in prog_langs, False)

    def test_dictionary_find_key_with_not_in(self):
        prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
        self.assertEqual('C++' not in prog_langs, False)
        self.assertEqual('c++' not in prog_langs, True)

    def test_add_key_pair_to_dictionary(self):
        prog_langs = {}
        prog_langs['Python'] = '1996'

        self.assertEqual(prog_langs['Python'], '1996')

    def test_add_duplicate_key_pair_to_dictionary_overwrites_existing_key_values(self):
        prog_langs = {'C++':'1979'}
        prog_langs['C++'] = '1980'
        self.assertEqual(prog_langs['C++'], '1980')

    def test_add_key_pair_to_dictionary_key_case_sensitive(self):
        prog_langs = {'C++':'1979'}
        prog_langs['c++'] = '1980'
        self.assertEqual(prog_langs['C++'], '1979')
        self.assertEqual(prog_langs['c++'], '1980')

    def test_delete_key_pair_to_dictionary(self):
        prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
        del prog_langs['C#']
        self.assertEqual(prog_langs, {'C++':'1979', 'Java':'1992', 'Python':'1996'})

    def test_get_key_pair_count_in_dictionary(self):
        prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
        count = len(prog_langs)

        self.assertEqual(count, 4)

    def test_add_mix_data_types_to_dictionary(self):
        prog_langs = {'C++':1979.5, 'Java':'1992', 'Python':'1996', 'C#':2001}
        self.assertEqual(prog_langs['C++'], 1979.5)
        self.assertEqual(prog_langs['C#'], 2001)

    def test_add_simple_and_list_data_types_to_dictionary(self):
        prog_langs = {'C++':[1979, 1980, 1981, 1982, 1983], 'Java':'1992', 'Python':'1996', 'C#':2001}
        cpp_value = prog_langs['C++']
        self.assertEqual(cpp_value, [1979, 1980, 1981, 1982, 1983])

    def test_clear_dictionary(self):
        prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
        prog_langs.clear()

        self.assertEqual(prog_langs, {})

    def test_get_from_dictionary(self):
        prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
        value = prog_langs.get('c++', 'Key not found')

        self.assertEqual(value, 'Key not found')

        value = prog_langs.get('C++', 'Key not found')
        self.assertEqual(value, '1979')

    def test_create_dictionary_w_comprehensions(self):
        numbers = [1, 2, 3, 4]
        squares = {}
        for number in numbers:
            squares[number] = number**2

        self.assertEqual(squares[1], 1)  #not index, referring to key
        self.assertEqual(squares[2], 4)
        self.assertEqual(squares[3], 9)
        self.assertEqual(squares[4], 16)    

