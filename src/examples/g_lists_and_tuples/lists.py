#List

#lists are mutable

def display_list():
    even_numbers = [2, 4, 6, 8, 10]
    print(even_numbers[2])                                  #index of list 

def display_list_while(list1):
    index = 0
    size = len(list1)

    print("Loops\tIndex\tSize\tindex\tlist1[index]")        #header

    while(index < size):
        print(str(index+1) + "\t" + str(index) + "\t" + str(size) + "\t" + str(index<size) + "\t" + str(list1[index]))
        print(list1[index])
        index += 1

def display_list_for_range(list1):

    for index in range(0, len(list1)):
        print(list1[index])

def display_list_for(list1):

    for list_item in list1:
        print(list_item)

def list_parameter(list1):
    list1[0] = 0                                             #when list modified, uses 1 same list 
    
def list_parameter_return(list1):
    list1[0] = 0
    return list1
