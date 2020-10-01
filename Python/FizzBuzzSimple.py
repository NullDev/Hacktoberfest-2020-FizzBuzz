// FizzBuzz Solution
// MishManners, Hacktoberfest starting point

import sys

inputs = sys.argv
inputs.pop(0)

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print ('fizzbuzz')
    elif n % 3 == 0:
        print ('fizz')
    elif n % 5 == 0:
        print ('buzz')
    else:
        print(n)

# inputs = input().split()
for input in inputs:
    input = int(input)
    fizzbuzz(input)
