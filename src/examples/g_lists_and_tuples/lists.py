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

def find_item_in_list(item, list1):
    result = item in list1
    return result


def copy_list():
    list1 = [1,2,3,4]
    print(list1)

    list2 = list1
    list2[0] = -1                                           #modifying list 2 but also modifies list 1 

    print(list1)
    print(list2)
#working with same list
    
def copy_lists_manually():
    list1 = [1,2,3,4]
    list2 = []
    print(list1)

    for num in list1:
        list2.append(num)                                   #manually iterate & copy, create a new variable

    list2[0] = -1
    print(list1)
    print(list2)
#two different lists


def two_dimensional_lists():
    student = [['Joe', 'Kim'],['Sam', 'Sue'],['Kelly', 'Chris']]
    print(student[0])
    print(student[1])
    print(student[2])

    print('Select one name')

    print(student[1][1])                                    #sue
    print(student[2][0])                                    #kelly


    print('use loop to display')
    
    for i in range(0, len(student)):
        for j in range(0, len(student[i])):
            print(student[i][j])
