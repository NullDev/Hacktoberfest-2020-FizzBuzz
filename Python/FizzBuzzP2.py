// Another method for creating FizzBuzz
// MishManners

import sys

inputs = sys.argv
inputs.pop(0)


def fizzbuzz(n):
    # for n in range(n, num, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print ('fizzbuzz')
        elif n % 3 == 0:
            print ('fizz')
        elif n % 5 == 0:
            print ('buzz')
        else: print(n)

for arg in sys.argv:
    fizzbuzz(int(arg))
