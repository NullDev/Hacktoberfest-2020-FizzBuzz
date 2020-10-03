#  A modular FizzBuzz solution. Accepts any range of numbers upon calling.
#  Author: @PanosVl

def multiple_of_3(number):
    return number%3 == 0

def multiple_of_5(number):
    return number%5 == 0

def multiple_of_both(number):
    return multiple_of_5(number) and multiple_of_3(number)

def fizzbuzz(total_numbers):
    for i in range(1, total_numbers+1):
        if multiple_of_both(i):
            print("FizzBuzz")
        elif multiple_of_3(i):
            print("Fizz")
        elif multiple_of_5(i):
            print("Buzz")
        else:
            print(i)

fizzbuzz(100)