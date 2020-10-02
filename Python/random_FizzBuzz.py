# Random FizzBuzz Algorithm
# Author: @felipeMarajo

import random

def FB():
    numbers = []

    while len(numbers) < 100:

        auxNumber = random.randint(1, 100)

        if auxNumber not in numbers:
            numbers.append(auxNumber)
            if auxNumber%3 == 0 and auxNumber%5 == 0:
                print("FizzBuzz")
            elif auxNumber%3 == 0:
                print("Fizz")
            elif auxNumber % 5 == 0:
                print("Buzz")
            else:
                print(auxNumber)

FB()