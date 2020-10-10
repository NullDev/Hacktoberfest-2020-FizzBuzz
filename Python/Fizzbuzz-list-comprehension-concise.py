# Python solution to the fizzbuzz problem using a list comprehension

print(["fizzbuzz" if x % 15 == 0 else "fizz" if x %
       3 == 0 else "buzz" if x % 5 == 0 else x for x in range(1, 101)])
