#A simple Python code to implement FizzBuzz
#Author @pranay-ar

# this for loop is run in range 0 to 100 because we know for loops is allways run from 0 not 1 and end with the  one digit befor 

for fizzbuzz in range(101):  ## for fizzbuzz in range(0,101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
