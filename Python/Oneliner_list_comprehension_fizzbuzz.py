# A single-liner FizzBuzz in python, using list comprehension and a for loop (to print a line at a time)
# Author: @moisesjsalmeida

for i in ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1,101)]: print(i)
