import dictionaries

dictionaries.create_dictionary()

prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}

key = input("Enter key: ")

dictionaries.find_keys_in_dictionary_with_in(key, prog_langs)


key = input("Enter key: ")
value = input('Enter value: ')

dictionaries.add_key_pairs_to_dictionary(key, value, prog_langs)

dictionaries.run_menu(prog_langs)