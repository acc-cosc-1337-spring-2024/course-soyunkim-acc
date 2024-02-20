#main program
import void_functions, value_return_functions

void_functions.say_hello(Python)

void_functions.use_global_variable()

void_functions.change_global_variable()

void_functions.use_global_variables_w_param(10)
print("Global: ", void_functions.val2)

num1 = 5
num2 = 10
result = value_return_functions.get_product(num1, num2)

print(result)
#involves 4 variables. num1 & num 2 and num1 & num2 in get_product()