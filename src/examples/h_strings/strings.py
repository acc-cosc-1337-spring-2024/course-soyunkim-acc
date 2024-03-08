def loop_string_w_while(str):
    index = 0
    size = len(str)                     #size of the string

    while(index < size):
        print(str(index))
        index += 1

def loop_string_w_for_range(str):

    size = len(str)
    for index in range(0, size):        #don't need to create index variable, implicitly created in for in range
        print(str[index])

def loop_strings_w_for(str):
    for ch in str:
        ch = '9'                        #can modify each characters but doesn't affect the string itself
        print(ch)

def concat_strings(str1, str2):
    return str1 + str2

def concat_string_w_plus_equal(str1, str2):
    str1 += str2
    return str1

def string_params(str):
    str = "Python"

def string_return_value(lang):
    str = "Python"
    return str

def get_length_of_string(str):
    return len(str)

def get_number_of_ch_in_string(str, ch):
    index = 0
    count = 0

    while index < len(str):
        if str[index] == ch:
            count += 1

        index += 1

    return count