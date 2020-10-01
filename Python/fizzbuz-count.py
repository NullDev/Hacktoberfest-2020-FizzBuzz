# [The multiples of 3 and 5 print "fizzbuz, fizz or buz"]
# Author: @leslymx

for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print(f"FizzBuz, {number} is a multiple of BOTH 3 AND 5")
    elif number % 3 == 0 :
        print(f"Fizz, {number} is a multiple of 3")
    elif number % 5 == 0:
        print(f"Buzz, {number} is a multiple of 5")
    else:
        print(number)
