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