def students_in_base_basket(set1, set2):
    print('Students in baseball and basketball')
    print(set1.union(set2))

def students_in_base_not_basket(set1, set2):
    print('Students in baseball not basketball')
    print(set1.difference(set2))

def students_in_basket_not_base(set1, set2):
    print('Students in basketball not baseball')
    print(set2.difference(set1))

def students_play_only_one_sport(set1, set2):
    print('Students who play only one sport')
    print(set1.symmetric_difference(set2))