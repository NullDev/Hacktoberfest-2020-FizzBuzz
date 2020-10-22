# using rand int get a random integer between 1-100.

import random


def fizz_buzz(in_number):
    print("Number is {}.".format(in_number))
    if (in_number % 3 == 0) and (in_number % 5 == 0):
        return "FizzBuzz"
    elif in_number % 5 == 0:
        return "Buzz"
    elif in_number % 3 == 0:
        return "Fizz"
    return f"Other Than {in_number}."


print(fizz_buzz(random.randint(1, 100)))
