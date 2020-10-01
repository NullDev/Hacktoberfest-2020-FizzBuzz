; FizzBuzz not-so-optimized code in Python
; Author: @nchiarappa


aString = ""

for fizzbuzz in range(1,101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        aString += "FizzBuzz"
        print(aString)
        aString = ""
        continue
    elif fizzbuzz % 3 == 0:
        aString += "Fizz"
        print(aString)
        aString = ""
        continue
    elif fizzbuzz % 5 == 0:
        aString += "Buzz"
        print(aString)
        aString = ""
        continue
    print(fizzbuzz)