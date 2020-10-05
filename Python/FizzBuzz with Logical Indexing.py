# FizzBuzz program in Python 3, to print numbers from 1 to 100 (with "Fizz" instead of multiples of 3, "Buzz" in place of multiples of 5, "FizzBuzz" against multiples of both 3 and 5 (i.e., multiples of 15))
# Author: @Git-Harshit

# One way for logical indexing (done with list)
for i in range(1, 100+1):
    print(
        [ i, [ "Buzz", ["Fizz", "FizzBuzz"][i%5==0] ][i%3 == 0] ][not(i%3 and i%5)]
    )

print()     # Just a newline separator

# Another way of logical indexing (done with tuple)
for i in range(1, 100+1):
    print(
        ( (i, "Buzz")[i%5==0], ("Fizz", "FizzBuzz")[i%5==0] )[i%3==0]
    )
