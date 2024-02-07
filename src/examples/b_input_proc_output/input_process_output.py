#output comments variables input calculations output constants
def display_output():
    print('hello')

def test_config():
    return True

#creating variable in writing function
def say_hello(name):
    display_value = "Hello " + name
    #display_value holds the value Hello name
    print(display_value)

def add_values(num1, num2):
    result = num1 + num2 
    return result

def floating_point_division(val1, val2):
    result = val1 / val2
    return result 
    #gives decimal values 

def integer_division(val1, val2):
    result = val1 // val2
    return result
    #ignores the remainder from division, working with only whole numbers

def operator_precedence_1(val1, val2, val3):
    result = val1 + val2 / val3
    return result

def operator_precedence_2(val1, val2, val3):
    result = (val1 + val2) / val3
    return result

def power_function(val1, exponent):
    result = val1 ** exponent
    return result

def get_remainder(val1, val2):
    result = val1 % val2 
    return result 