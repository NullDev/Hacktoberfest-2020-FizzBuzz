# simple fizzbuzz implementation with the special case of only using one single string and printing its parts as needed
# Author: @ladokp

fizzbuzz = "FizzBuzz"

for n in range(1, 101):
    if n % 15 == 0:
        print(fizzbuzz)
    elif n % 3 == 0:
        print(fizzbuzz[:4])
    elif n % 5 == 0:
        print(fizzbuzz[4:])
    else:
        print(n)
