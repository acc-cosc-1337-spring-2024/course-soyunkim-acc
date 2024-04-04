def test_list_supports_different_data_type_elements(self):
    list1 = [1, 5.5, 'a']

    self.assertEqual(list1[0], 1)
    self.assertEqual(list1[1], 5.5)   
    self.assertEqual(list1[2], 'a')

def test_list_supports_list_as_elements(self):
    sub_list = [5, 9, 2]
    list1 = [sub_list]   #makes sub_list an element of list1

    self.assertEqual(list1[0], [5, 9, 2])