import unittest

from src.examples.g_lists_and_tuples.lists import find_item_in_list, list_parameter, list_parameter_return
class Test_Config(unittest.TestCase):


    def test_list_parameter_works_with_one_list(self):
        even_numbers = [2,4,6,8,10]
        expected_list = [0,4,6,8,10]

        list_parameter(even_numbers)

        self.assertEqual(even_numbers, expected_list)

    def test_list_parameters_return_works_with_one_list(self):
        even_numbers = [2,4,6,8,10]
        expected_list = [0,4,6,8,10]

        list_parameter(even_numbers)

        self.assertEqual(even_numbers, expected_list)
        
    def test_lists_parameter_return_works_with_one_list_capture_return_value(self):
        even_numbers = [2,4,6,8,10]
        expected_list = [0,4,6,8,10]

        return_list = list_parameter_return(even_numbers)

        self.assertEqual(return_list, even_numbers) 
        
        #test to see if the modified list originates from "even_number"


    def test_find_item_in_list1(self):
        prods = ["V475", "F987", "Q143", "R666"]
        result = find_item_in_list("Q143", prods)

        self.assertEqual(result, True)

    def test_find_item_not_in_list(self):
        prods = ["V475", "F987", "Q143", "R666"]
        result = find_item_in_list("q143", prods)

        self.assertEqual(result, False)

    def test_append_item_to_list(self):
        names = []
        names.append("Python")

        self.assertEqual(names, ["Python"])

    def test_get_list_index(self):
        names = ["C++", "C#", "Java", "Python"]
        index = names.index("Python")

        self.assertEqual(index, 3)
        self.assertEqual(names[index], "Python")

    def test_insert_into_list(self):
        names = ["C++", "C#", "Java", "Python"]
        names.insert(0, "C")

        self.assertEqual(names, ["C", "C++", "C#", "Java", "Python"])

    def test_list_sort(self):
        nums = [9,1,0,2,8,5,4,6,3,7]
        nums.sort()

        self.assertEqual(nums, [0,1,2,3,4,5,6,7,8,9])

    def test_list_remove_item(self):
        nums = [9,1,0,2,8,5,4,6,3]
        nums.remove(5)

        self.assertEqual(nums, [9,1,0,2,8,4,6,3])

    def test_list_del_item(self):
        names = ["C++", "C#", "Java", "Python"]
        del names[1]

        self.assertEqual(names, ["C++", "Java", "Python"])

    def test_get_min_value_from_list(self):
        nums = [9,1,0,2,8,5,4,6,3]
        min_value = min(nums)

        self.assertEqual(min_value, 0)

    def test_list_supports_different_data_type_elements(self):
        list1 = [1, 5.5, 'a']

        self.assertEqual(list1[0], 1)
        self.assertEqual(list1[1], 5.5)   
        self.assertEqual(list1[2], 'a')

    def test_list_supports_list_as_elements(self):
        sub_list = [5, 9, 2]
        list1 = [sub_list]                          #makes sub_list an element of list1

        self.assertEqual(list1[0], [5, 9, 2])

