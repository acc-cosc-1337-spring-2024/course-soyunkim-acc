import lists

even_numbers = [2,4,6,8,10]

lists.display_list()
lists.display_list_while(even_numbers)
lists.display_list_for_range(even_numbers)
lists.display_list_for(even_numbers)

prods = ["V475", "F987", "Q143", "R666"]
item = input("Enter item number: ")

result = lists.find_item_in_list(item, prods)

if(result):                                         #is true
    print("item found")
else:
    print("Item not in list")


#creating lists and appending items to the list while loop 
names = []
option = "y"

while option.upper() == "Y":

    item = input("Enter name: ")

    names.append(item)

for name in names:
    print(name)

#modify specific item on the list using index
item = input("Enter name: ")
index = names.index(item)

names[index] = "Modified"

for name in names:
    print(name)

#removing items from list
nums = [9,1,0,2,8,5,4,6,3]

item = int(input("Enter number: "))

if item in nums:
    nums.remove(item)
    print("item removed")
else:
    print("Item not in list")

for num in nums:
    print(num)


lists.copy_list()
lists.two_dimensional_lists()
