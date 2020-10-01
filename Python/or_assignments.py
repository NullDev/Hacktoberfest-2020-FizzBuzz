# Minimal solution using Python OR syntax for assignments
# Author: @CrsiX

print(*[(""if x%15else"FizzBuzz")or(""if x%5else"Buzz")or(""if x%3else"Fizz")or x for x in range(1,101)])

