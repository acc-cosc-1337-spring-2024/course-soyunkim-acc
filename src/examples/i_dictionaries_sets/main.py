import dictionaries

dictionaries.create_dictionary()

prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}

key = input("Enter key: ")

dictionaries.find_keys_in_dictionary_with_in(key, prog_langs)


key = input("Enter key: ")
value = input('Enter value: ')

dictionaries.add_key_pairs_to_dictionary(key, value, prog_langs)

dictionaries.run_menu(prog_langs)

dictionaries.loop_dictionary_for()
dictionaries.get_dictionary_keys()

import sets


my_set = set(['a', 'b', 'c'])
my_set = set('abc')
#create the same sets

print(myset) #unordered set
print(len(myset))

my_set = set()
my_set.add('a')
my_set.add('b')
my_set.add('c')

my_set.remove('a')

baseball = set(['Jodi', 'CArmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

sets.students_in_base_basket(baseball, basketball)

sets.students_in_base_not_basket(baseball, basketball)

sets.students_in_basket_not_base(baseball, basketball)

sets.students_play_only_one_sport(baseball, basketball)