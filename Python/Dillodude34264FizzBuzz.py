"""
I used a for loop to print 1 through 100, and
using the math module along with a few if/else
statements I singled out the multiples of 3 and 5.
"""
# Author: @Dillodude34264
import math
for x in range(1, 101):
    if math.fmod(x, 3) == 0:
        if math.fmod(x, 5) == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
        if math.fmod(x, 5) == 0:
            print("Buzz")
        else:
            print(x)
