import input_process_output

input_process_output.display_output()

input_process_output.say_hello("Python learners")
#name now has the value "Python learners"

#create variable in main.py file, use it in function
result = input_process_output.add_values(5, 5)
print(result)

#Can reuse variables without causing error

result = "Python is flexible with reusing variables"
print(result)

result = 10.99
result = result + 1.50
print(result)

#same as
#result = input_process_output.add_values(5, 5)
#print(result)

#"n" allows python to treat n as sequence of characters 
result = "10.99"
result = result + "1.50"
print(result)

#Bringing data from the keyboard

value = input("Enter value: ") # reads values from keyboard as strings(alphanumeric)
print(value)

result = input_process_output.add_values(value, value)
print(result)

#convert alphanumeric to int(whole number)
result = input_process_output.add_values(int(value), int(value))
print(result)

#convert alphanumeric to float(decimal number)
result = input_process_output.add_values(float(value), float(value))
print(result)

val1 = input("Enter value 1: ")
val2 = input("Enter value 2: ")

result = input_process_output.floating_point_division(int(val1), int(val2))
print(result)

val1 = input("Enter value 1: ")
val2 = input("Enter value 2: ")

result = input_process_output.integer_division(int(val1), int(val2))
print(result)

#can put int(eger) when defining the variable
val1 = int(input("Enter value 1: "))
val2 = int(input("Enter value 2: "))
val3 = int(input("Enter value 3: "))

result = input_process_output.operator_precedence_1(val1, val2, val3)
print(result)

result = input_process_output.operator_precedence_2(val1, val2, val3)
print(result)

#exponent
val1 = int(input("Enter value 1: "))
exponent = int(input("Enter exponent: "))

result = input_process_output.power_function(val1, exponent)
print(result)

val1 = int(input("Enter value 1: "))
val2 = int(input("Enter value 2: "))

result = input_process_output.get_remainder(val1, val2)

print(result)