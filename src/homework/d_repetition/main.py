import repetition

def Homework_3_Menu():
    print("Homework 3 Menu")
    print("1 - Factorial")
    print("2 - Sum odd numbers")
    print("3 - Exit")

option = "0"

while option != "3":   
    Homework_3_Menu()
    option = input("Enter the number for the needed function: ")

    if option == "1":
        num = 0
            
        while(not(0 < int(num) < 10)):
            num = input("Enter a number (1-9): ")

            if(num.isnumeric()):
                num = int(num)

                if 0 < num < 10:
                    print("Factorial: ",repetition.get_factorial(num))

                else:           
                    print("Invalid number. Please enter a number between 1 and 9")

            else:
                print("Invalid number. Please enter a number between 1 and 9")
                    
    elif option == "2":
        num = 0
            
        while(not(0 < int(num) < 100)):
            num = input("Enter a number(1-99): ")

            if num.isnumeric:
                 num = int(num)

            if(0 < num < 100 ):
                print("Sum: ", repetition.sum_odd_numbers(num))

            else: 
                print("Invalid number. Please enter a number between 1 and 99: ")

    elif option != "3":
        print("Invalid option")

        Homework_3_Menu()
        option = input("Enter the number for the needed function: ")


    if option == "3":
        continue_exit = input("Do you want to exit? (yes/no): ")

        if continue_exit == "no":
            option = "0"
            
        elif continue_exit == "yes":
            print("Exiting...")