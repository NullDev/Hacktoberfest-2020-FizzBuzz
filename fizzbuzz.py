# Author : Benjamin Parsons
# Prints a list of numbers with correct subsitions of fizz, buzz, and fizzbuzz
# from 1 to 100

result = []
def fizzbuzz (number):
    for num in range(1, number):
        if num % 3 == 0:
            result.append('fizz')
        elif num % 5 == 0:
            result.append('buzz')
        elif num % 3 == 0 and num % 5 == 0:
            result.append(num)
        else:
            result.append(num)
    return result

print(fizzbuzz(101))
