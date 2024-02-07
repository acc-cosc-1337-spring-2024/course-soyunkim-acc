def test_config():
    return True

#boolean operators AND, OR, NOT and == (!=)

def get_and_result(bool1, bool2):
    result = bool1 and bool2
    return result

def get_or_result(bool1, bool2):
    result = bool1 or bool2
    return result

def get_not_result(bool1):
    result = not bool1
    return result

# == equality operator, comparison, returns t/f

def is_even(num):
    remainder = num % 2 #remainder of (even n)/2 = 0
    return remainder == 0 #0 == 0

def is_odd(num):
    remainder = num % 2 #remainder of (odd n)/2 = 1
    return remainder == 1 

def is_vowel(letter):
    result = letter = 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'
    return result