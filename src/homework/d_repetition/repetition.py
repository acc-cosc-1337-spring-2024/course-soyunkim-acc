def get_factorial(num):

    factorial = 1

    if factorial <= num:
        for n in range(1, num + 1):
            factorial = factorial * n

    return factorial

def sum_odd_numbers(num):

    i = 1
    sum = 0

    while(i <= num):
        sum += i
        i += 2

    return sum