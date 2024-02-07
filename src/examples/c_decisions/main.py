import decisions

#conditional statement 
#if, else, elif

num = int(input("Enter a number: "))

result = decisions.is_even(num)

if(result == True):
    print("Even", result)
else:
    print("Number is not Even")

result = decisions.is_odd(num)

#don't need the ""== True" part because result already uses boolean operator in is.even/is.odd
# can also say result == false and then use if, else 

if(result):
    print("Odd", result)
else:
    print("Number is not Odd")


num = int(input("Enter a number: "))

overtime = decisions.is_overtime(num)

if(overtime):
    print("You earned overtime.")
else:
    print("No overtime.")


year = int(input("Enter a year: "))

generation = decisions.get_generation(year)

print(year, " is ", generation)